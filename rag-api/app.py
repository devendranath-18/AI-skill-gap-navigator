from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import os
import re

from config.skills import SKILL_ALIASES
from scripts.parser import parse_content
from scripts.search import search_skill
from scripts.pdf_parser import extract_text_from_pdf


# ==================================================
# APP CONFIG
# ==================================================

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==================================================
# REQUEST MODEL
# ==================================================

class AnalyzeRequest(BaseModel):
    resume_text: str
    job_description: str


# ==================================================
# SKILL EXTRACTION
# ==================================================

def extract_skills(text: str):

    text = text.lower()

    found_skills = []

    for skill, aliases in SKILL_ALIASES.items():

        for alias in aliases:

            pattern = (
                r"\b"
                + re.escape(alias.lower())
                + r"\b"
            )

            if re.search(
                pattern,
                text
            ):

                found_skills.append(
                    skill
                )

                break

    return sorted(
        list(
            set(found_skills)
        )
    )


# ==================================================
# ANALYSIS LOGIC
# ==================================================

def analyze_resume_data(
    resume_text: str,
    job_description: str
):

    resume_skills = extract_skills(
        resume_text
    )

    jd_skills = extract_skills(
        job_description
    )

    print("=" * 50)

    print(
        "RESUME SKILLS:"
    )
    print(
        resume_skills
    )

    print(
        "JD SKILLS:"
    )
    print(
        jd_skills
    )

    print("=" * 50)

    matched_skills = []

    missing_skills = []

    for skill in jd_skills:

        if skill in resume_skills:

            matched_skills.append(
                skill
            )

        else:

            missing_skills.append(
                skill
            )

    if len(jd_skills) == 0:

        match_score = 0

    else:

        match_score = round(
            (
                len(
                    matched_skills
                )
                /
                len(
                    jd_skills
                )
            ) * 100,
            2
        )

    resources = {}

    for skill in missing_skills:

        try:

            result = search_skill(
                skill,
                top_k=1
            )

            if result:

                resources[
                    skill
                ] = {

                    "source":
                    result[0][
                        "source"
                    ],

                    "similarity":
                    result[0][
                        "similarity"
                    ],

                    "resource":
                    parse_content(
                        result[0][
                            "text"
                        ]
                    )
                }

            else:

                resources[
                    skill
                ] = {
                    "message":
                    "No resource found"
                }

        except Exception as e:

            resources[
                skill
            ] = {
                "error":
                str(e)
            }

    return {

        "match_score":
        match_score,

        "resume_skills":
        resume_skills,

        "job_skills":
        jd_skills,

        "matched_skills":
        matched_skills,

        "missing_skills":
        missing_skills,

        "resources":
        resources
    }


# ==================================================
# ROOT
# ==================================================

@app.get("/")
def home():

    return {
        "message":
        "Resume Analyzer API Running"
    }


# ==================================================
# TEXT ANALYSIS
# ==================================================

@app.post("/analyze")
def analyze(
    data: AnalyzeRequest
):

    return analyze_resume_data(
        data.resume_text,
        data.job_description
    )


# ==================================================
# PDF ANALYSIS
# ==================================================

@app.post("/analyze-pdf")
async def analyze_pdf(
    file: UploadFile = File(...),
    job_description: str = Form("")
):

    temp_path = (
        f"temp_{file.filename}"
    )

    with open(
        temp_path,
        "wb"
    ) as buffer:

        buffer.write(
            await file.read()
        )

    resume_text = (
        extract_text_from_pdf(
            temp_path
        )
    )

    os.remove(
        temp_path
    )

    return analyze_resume_data(
        resume_text,
        job_description
    )