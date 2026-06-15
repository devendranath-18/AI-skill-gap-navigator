import os




def save_skill(skill: str, roadmap: str):

    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    DATA_DIR = os.path.join(
        BASE_DIR,
        "data"
    )

    os.makedirs(
        DATA_DIR,
        exist_ok=True
    )

    filename = (
        skill.lower()
        .replace(" ", "_")
        + ".txt"
    )

    filepath = os.path.join(
        DATA_DIR,
        filename
    )

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(roadmap)

    print(
        f"Saved knowledge: {filepath}"
    )