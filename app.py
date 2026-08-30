from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills

from flask import Flask, render_template, request
import os


app = Flask(__name__)


# Upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Create uploads folder if it does not exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Upload and analyze resume
@app.route("/upload", methods=["POST"])
def upload():

    # Check whether resume is uploaded
    if "resume" not in request.files:
        return "No file selected"

    file = request.files["resume"]

    # Check whether a file is selected
    if file.filename == "":
        return "Please select a file"

    # Get job description from form
    job_description = request.form.get("job_description")

    # Check whether job description is entered
    if not job_description:
        return "Please enter a job description"

    # Create file path
    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    # Save uploaded resume
    file.save(filepath)

    # Extract text from PDF
    text = extract_text_from_pdf(filepath)

    # Extract skills from resume
    resume_skills = extract_skills(text)

    # Extract skills from job description
    job_skills = extract_skills(job_description)

    # Find matched skills
    matched_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)

    # Find missing skills
    missing_skills = []

    for skill in job_skills:
        if skill not in resume_skills:
            missing_skills.append(skill)

    # Calculate match score
    if len(job_skills) > 0:
        score = (
            len(matched_skills) / len(job_skills)
        ) * 100
    else:
        score = 0

    # Display result
    return render_template(
        "result.html",
        filename=file.filename,
        resume_text=text,
        skills=matched_skills,
        missing_skills=missing_skills,
        score=round(score, 2)
    )


# Run application
if __name__ == "__main__":
    app.run(debug=True)