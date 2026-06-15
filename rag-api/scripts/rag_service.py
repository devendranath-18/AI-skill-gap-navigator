from generate_roadmap import generate_roadmap

skills = [
    "Docker",
    "AWS"
]

all_roadmaps = {}

for skill in skills:

    roadmap = generate_roadmap(skill)

    all_roadmaps[skill] = roadmap

print(all_roadmaps)