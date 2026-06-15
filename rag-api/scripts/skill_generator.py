import os

from scripts.build_index import build_index


def create_skill_file(
    skill: str,
    roadmap: str
):
    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    data_dir = os.path.join(
        base_dir,
        "data"
    )

    os.makedirs(
        data_dir,
        exist_ok=True
    )

    file_path = os.path.join(
        data_dir,
        f"{skill.lower()}.txt"
    )

    if not os.path.exists(
        file_path
    ):
        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(roadmap)

        print(
            f"Created: {file_path}"
        )

        build_index()

    return file_path