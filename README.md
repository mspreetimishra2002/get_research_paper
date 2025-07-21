# get-papers

##  Project Description

`get-papers` is a command-line tool that searches PubMed for research papers based on a given query and extracts only those papers that have at least one non-academic (biotech/pharma) author. The tool outputs the results in a CSV file.

This project was developed as part of the take-home assignment for Aganitha Cognitive Solutions.

---

##  Features

- Accepts PubMed search query from user
- Uses PubMed API to fetch articles
- Filters for papers with non-academic affiliations (e.g., containing keywords like Pharma, Inc, Ltd, Biotech)
- Extracts the following fields:
  - PubMed ID
  - Title
  - Publication Date
  - Non-academic Authors
  - Company Affiliations
  - Corresponding Author Email
- Offers debug mode for development transparency
- Saves results to CSV file or prints to console

---

## Tech Stack & Tools

- **Python 3.10+**
- [Typer](https://typer.tiangolo.com/) – for building the CLI
- [Pandas](https://pandas.pydata.org/) – for working with data and CSV
- [Requests](https://docs.python-requests.org/) – for calling PubMed API
- [Poetry](https://python-poetry.org/) – for dependency and virtual environment management

---

## How to Run

> Make sure Python 3.10+ and Poetry are installed.

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/get-papers.git
cd get-papers
```

_Or extract the project ZIP file._

### 2. Install dependencies

```bash
poetry install
```

### 3. Run the CLI tool

```bash
poetry run python cli.py
```

You will be prompted to:

- Enter a PubMed query (e.g., `Cancer AND 2024`)
- Enter output file name (e.g., `results.csv`)
- Choose whether to enable debug mode

---

## Project Structure

```
get-papers/
├── cli.py                     # Main CLI logic
├── get_papers/
│   ├── __init__.py
│   └── fetch.py               # Functions for API and filtering
├── pyproject.toml             # Poetry config (dependencies & CLI script)
├── README.md                  # Project description and instructions
```

---

## Notes

- Filtering for non-academic authors is done heuristically based on keywords like `"Pharma"`, `"Inc"`, `"Ltd"`, `"Biotech"`, etc.
- Debug mode prints internal steps such as query, paper count, filtered authors, and final result info.
- All PubMed API requests respect their default rate limits and query structure.

---

## Candidate Info

- **Candidate ID:** Naukri072025  
- **Submission for:** Take-Home CLI Assignment  
- **Company:** Aganitha Cognitive Solutions

---

## Example

Here’s how it looks when you run the tool:

```
Enter your PubMed search query (e.g., Cancer AND 2024): Cancer AND 2024
Enter the output file name (e.g., results.csv): cancer_results.csv
Enable debug mode? [y/N]: y

[DEBUG] Searching PubMed for query: Cancer AND 2024
[DEBUG] Found 100 paper IDs
[DEBUG] 5 papers have non-academic authors
✅ Results saved to: cancer_results.csv
```

---

## ✅ Status

✅ Assignment complete
