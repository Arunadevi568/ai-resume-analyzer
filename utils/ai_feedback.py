def generate_feedback(score, similarity_score, missing_skills):

    feedback = []

    # ATS Score Feedback
    if score >= 80:
        feedback.append(
            "Your resume has a strong ATS score."
        )

    elif score >= 60:
        feedback.append(
            "Your resume is good, but there is room for improvement."
        )

    else:
        feedback.append(
            "Your resume needs improvement to increase ATS compatibility."
        )


    # Job Match Feedback
    if similarity_score >= 75:
        feedback.append(
            "Your resume strongly matches the provided job description."
        )

    elif similarity_score >= 50:
        feedback.append(
            "Your resume partially matches the job description. Add more relevant keywords."
        )

    else:
        feedback.append(
            "Your resume has a low match with the job description. Customize it for this role."
        )


    # Missing Skills Feedback
    if missing_skills:
        skills_text = ", ".join(missing_skills[:5])

        feedback.append(
            f"Consider adding relevant skills: {skills_text}"
        )

    else:
        feedback.append(
            "Great! All skills from the current skill database were found."
        )


    return feedback