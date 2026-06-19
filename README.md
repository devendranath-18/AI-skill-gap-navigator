# AI Skill Gap Navigator

An AI-powered Resume Skill Gap Analyzer that compares a user's resume against a job description and identifies missing skills along with learning resources.

## Live Demo

Frontend:
https://ai-skill-gap-navigator.vercel.app

Backend:
https://devendranath-18-ai-skill-gap-navigator.hf.space

---

## Features

* Upload PDF resumes
* Extract resume content automatically
* Compare resume skills against job descriptions
* Calculate skill match percentage
* Identify missing skills
* Recommend learning resources
* Semantic search using FAISS
* RAG-based skill matching
* Responsive frontend UI

---

## Tech Stack

Frontend:

* Next.js
* TypeScript
* Tailwind CSS

Backend:

* FastAPI
* Python
* FAISS
* Sentence Transformers

Deployment:

* Vercel
* Hugging Face Spaces
* Docker

---

## Project Architecture

Resume PDF
↓
PDF Text Extraction
↓
Skill Extraction
↓
Resume vs Job Description Comparison
↓
FAISS Semantic Search
↓
Missing Skill Detection
↓
Learning Resource Recommendation

---

## Installation

Clone repository:

```bash
git clone <repository-url>
```

Install frontend:

```bash
npm install
npm run dev
```

Install backend:

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

---

## Future Improvements

* Resume ATS score prediction
* Skill roadmap visualization
* AI-generated resume suggestions
* Authentication system
* Personalized learning plans

---

## Author

Devendranath Kapa

B.Tech CSE | Software Engineer | AI & Full Stack Developer
