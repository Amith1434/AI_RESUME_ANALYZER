# AI Resume Analyzer

An AI-powered resume analysis system that evaluates a resume against a job description and provides ATS-style scoring, skill matching, missing skills, strengths, and improvement suggestions.

## Current Progress

### Day 1
- Project structure created
- Python virtual environment configured
- PyMuPDF integrated
- PDF text extraction implemented

## Tech Stack

- Python
- PyMuPDF
- FastAPI
- scikit-learn
- LLM API
- HTML/CSS/JavaScript

## Project Structure

```text
AI_RESUME_ANALYZER/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── pdf_parser.py
│
├── data/
├── tests/
├── requirements.txt
├── .gitignore
└── README.md


## Day 2 — Resume Skill Extraction

Added basic resume skill extraction.

### What it does

* Converts resume text to lowercase.
* Searches for known technical skills.
* Returns the detected skills as a list.

### Pipeline

```text
PDF → Text Extraction → Skill Extraction → Skills List
```

### Example

```text
Input:
"Experience with Python, PyTorch and SQL"

Output:
["python", "sql", "pytorch"]
```

### Current Limitation

Uses keyword matching, so it may miss skills written using abbreviations, synonyms, or descriptions.

**Day 2 complete:** Basic resume skill extraction implemented and tested.
