import typer
from get_papers.fetch import fetch_pubmed_ids, fetch_pubmed_details
import pandas as pd
from typing import Optional

app = typer.Typer()

def main():
    typer.run(get_papers_list)

def get_papers_list():
    query = typer.prompt("Enter your PubMed search query (e.g., Cancer AND 2024)")
    file = typer.prompt("Enter the output file name (e.g., results.csv)", default=None)
    debug = typer.confirm("Enable debug mode?", default=False)

    if debug:
        typer.echo(f"[DEBUG] Searching PubMed for query: {query}")

    ids = fetch_pubmed_ids(query)

    if debug:
        typer.echo(f"[DEBUG] Found {len(ids)} paper IDs")

    papers = fetch_pubmed_details(ids)

    if debug:
        typer.echo(f"[DEBUG] {len(papers)} papers have non-academic authors")

    if papers:
        df = pd.DataFrame(papers)
        if file:
            df.to_csv(file, index=False)
            typer.echo(f"✅ Results saved to: {file}")
        else:
            typer.echo(df.to_string(index=False))
    else:
        typer.echo("❌ No matching papers found.")

if __name__ == "__main__":
    main()
