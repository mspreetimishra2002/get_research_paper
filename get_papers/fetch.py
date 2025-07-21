from typing import List, Dict, Optional
import requests
import xml.etree.ElementTree as ET

def fetch_pubmed_ids(query: str, retmax: int = 100) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": retmax,
    } 
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])

def fetch_pubmed_details(pmid_list: List[str]) -> List[Dict]:
    if not pmid_list:
        return []

    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pmid_list),
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    root = ET.fromstring(response.content)

    papers = []
    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or "Unknown"
        authors = article.findall(".//Author")
        affiliations = []
        non_acad_authors = []
        company_names = []

        for author in authors:
            aff = author.findtext("AffiliationInfo/Affiliation")
            lastname = author.findtext("LastName")
            firstname = author.findtext("ForeName")
            name = f"{firstname or ''} {lastname or ''}".strip()

            if aff:
                affiliations.append(aff)
                if is_non_academic(aff):
                    non_acad_authors.append(name)
                    company_names.append(aff)

        email = extract_email(affiliations)

        if non_acad_authors:
            papers.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": "; ".join(non_acad_authors),
                "Company Affiliation(s)": "; ".join(company_names),
                "Corresponding Author Email": email or "Not found"
            })
    return papers

def is_non_academic(affiliation: str) -> bool:
    keywords = ["Inc", "Ltd", "LLC", "Pharma", "Biotech", "Corporation", "Company"]
    acad_keywords = ["University", "College", "Institute", "Hospital", "School", "Center", "Centre"]
    if any(kw in affiliation for kw in keywords) and not any(kw in affiliation for kw in acad_keywords):
        return True
    return False

def extract_email(affiliations: List[str]) -> Optional[str]:
    import re
    for aff in affiliations:
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}", aff)
        if emails:
            return emails[0]
    return None
