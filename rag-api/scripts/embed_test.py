from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

text = "Docker is a containerization platform."

embedding = model.encode(text)

print("Vector Length:", len(embedding))
print("First 10 Values:")
print(embedding[:10])