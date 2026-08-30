import csv


def load_skills():
    skills = []

    with open("data/skills.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            skills.append(row["skill"].lower().strip())

    return skills


def extract_skills(resume_text):
    skills = load_skills()

    found_skills = []

    resume_text = resume_text.lower()

    for skill in skills:
        if skill in resume_text:
            found_skills.append(skill)

    return found_skills