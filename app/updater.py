# app/updater.py
def update_cv(cv_text: str, missing_skills: list) -> str:
    """Append missing skills to a Skills section in the CV text."""
    if not missing_skills:
        return cv_text
    
    updated = cv_text + "\n\nSkills (Added for Job Match):\n"
    updated += ", ".join(missing_skills)
    return updated
