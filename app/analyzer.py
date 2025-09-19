# app/analyzer.py
import re

SKILLS = ["Python", "SQL", "Excel", "Machine Learning", "Communication", "Teamwork"]

def extract_skills(text: str) -> list:
    """Find known skills in the text (case-insensitive)."""
    found = []
    for skill in SKILLS:
        if re.search(rf"\b{skill}\b", text, flags=re.IGNORECASE):
            found.append(skill)
    return found

def find_missing_skills(job_skills: list, cv_skills: list) -> list:
    """Return skills required by job but missing in CV."""
    return [s for s in job_skills if s not in cv_skills]
