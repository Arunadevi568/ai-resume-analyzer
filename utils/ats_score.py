def calculate_ats_score(found_skills, total_skills, resume_text):
    
    # Skill Matching Score (70 marks)
    if len(total_skills) > 0:
        skill_percentage = len(found_skills) / len(total_skills)
    else:
        skill_percentage = 0

    skill_score = skill_percentage * 70


    # Resume Content Score (30 marks)
    content_score = 0

    resume_text = resume_text.lower()

    important_sections = [
        "education",
        "skills",
        "project",
        "experience",
        "certification"
    ]

    for section in important_sections:
        if section in resume_text:
            content_score += 6


    # Final ATS Score
    ats_score = skill_score + content_score

    if ats_score > 100:
        ats_score = 100

    return round(ats_score, 2)