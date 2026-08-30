# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer that analyzes a candidate's resume and compares it with a job description.

The application extracts skills from the uploaded resume, identifies skills required for the job, finds matched and missing skills, and calculates a Resume Match Score.

---

## 🚀 Features

- 📄 Upload Resume in PDF format
- 🔍 Extract text from PDF resumes
- 🧠 Extract technical skills from resumes
- 💼 Analyze Job Description
- ✅ Identify Matched Skills
- ❌ Identify Missing Skills
- 📊 Calculate Resume Match Score
- 🎨 Modern and Responsive User Interface

---

## 🛠️ Technologies Used

### Backend
- Python
- Flask

### Frontend
- HTML
- CSS
- JavaScript

### Libraries
- PyMuPDF
- CSV

---

## 📂 Project Structure

```text
ai-resume-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── skills.csv
│   └── job roles.csv
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── uploads/
│
└── utils/
    ├── pdf_reader.py
    ├── skill_extractor.py
    ├── ats_score.py
    ├── similarity.py
    ├── ai_feedback.py
    └── reporter_generator.py