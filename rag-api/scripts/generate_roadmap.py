import os

from dotenv import load_dotenv
import google.generativeai as genai

from scripts.search import search_skill
from scripts.auto_learn import save_skill

# =====================================
# LOAD ENVIRONMENT VARIABLES
# =====================================

load_dotenv()

api_key = os.getenv(
    "GEMINI_API_KEY"
)

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found"
    )

# =====================================
# CONFIGURE GEMINI
# =====================================

genai.configure(
    api_key=api_key
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# =====================================
# GENERATE ROADMAP
# =====================================

def generate_roadmap(
    skill: str
) -> str:

    results = search_skill(
        query=skill,
        top_k=3
    )

    # =====================================
    # SKILL FOUND IN FAISS
    # =====================================

    if results:

        context = "\n\n".join(
            item["text"]
            for item in results
        )

        prompt = f"""
You are an expert software mentor.

Skill:
{skill}

Knowledge Base:
{context}

Create a detailed roadmap.

Include:

1. Skill Overview

2. Beginner Level
- Topics
- Resources
- Practice

3. Intermediate Level
- Topics
- Projects

4. Advanced Level
- Topics
- Real World Usage

5. Interview Questions

6. Portfolio Projects

7. 30 Day Learning Plan

Keep the roadmap practical and structured.
"""

        response = model.generate_content(
            prompt
        )

        return response.text

    # =====================================
    # SKILL NOT FOUND
    # =====================================

    print(
        f"{skill} not found in knowledge base."
    )

    prompt = f"""
You are an expert software mentor.

Create a complete roadmap for:

{skill}

Include:

1. Skill Overview

2. Beginner Level
- Topics
- Resources
- Practice

3. Intermediate Level
- Topics
- Projects

4. Advanced Level
- Topics
- Real World Usage

5. Interview Questions

6. Portfolio Projects

7. 30 Day Learning Plan

Keep the roadmap practical and structured.
"""

    response = model.generate_content(
        prompt
    )

    roadmap = response.text

    # Save skill automatically
    save_skill(
        skill,
        roadmap
    )

    print(
        f"Saved new skill: {skill}"
    )

    return roadmap


# =====================================
# CLI TEST
# =====================================

if __name__ == "__main__":

    skill = input(
        "\nEnter skill: "
    ).strip()

    try:

        roadmap = generate_roadmap(
            skill
        )

        print("\n")
        print("=" * 60)
        print("ROADMAP")
        print("=" * 60)
        print(roadmap)

    except Exception as e:

        print(
            f"\nError: {e}"
        )