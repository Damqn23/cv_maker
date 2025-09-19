# app/main.py
from app import parser, analyzer, updater, exporter

def main():
    job_desc = parser.load_job_description("data/sample_job.txt")
    cv_text = parser.load_cv("data/sample_cv.pdf")

    job_skills = analyzer.extract_skills(job_desc)
    cv_skills = analyzer.extract_skills(cv_text)

    print("Job skills:", job_skills)
    print("CV skills:", cv_skills)

    missing = analyzer.find_missing_skills(job_skills, cv_skills)
    print("Missing skills:", missing)

    updated_cv = updater.update_cv(cv_text, missing)
    exporter.to_pdf(updated_cv, "data/output_cv.pdf")

if __name__ == "__main__":
    main()
