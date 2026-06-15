def parse_content(text):

    data = {
        "skill": "",
        "roadmap": "",
        "youtube": "",
        "documentation": "",
        "projects": []
    }

    current_section = None

    for raw_line in text.splitlines():

        line = raw_line.strip()

        if not line:
            continue

        # Skill
        if line.startswith("Skill:"):
            data["skill"] = (
                line.replace("Skill:", "")
                .strip()
            )
            current_section = None
            continue

        # Section Headers
        if line.startswith("Roadmap:"):
            current_section = "roadmap"
            continue

        if line.startswith("YouTube:"):
            current_section = "youtube"
            continue

        if line.startswith("Documentation:"):
            current_section = "documentation"
            continue

        if line.startswith("Projects:"):
            current_section = "projects"
            continue

        # Section Content
        if current_section == "roadmap":
            if not data["roadmap"]:
                data["roadmap"] = line

        elif current_section == "youtube":
            if not data["youtube"]:
                data["youtube"] = line

        elif current_section == "documentation":
            if not data["documentation"]:
                data["documentation"] = line

        elif current_section == "projects":

            if (
                line.startswith("Project")
                or line.startswith("Difficulty")
            ):
                continue

            if line not in data["projects"]:
                data["projects"].append(line)

    return data