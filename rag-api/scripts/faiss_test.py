import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# ==========================================
# Load Embedding Model
# ==========================================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# ==========================================
# Documents
# ==========================================

documents = [
    "Docker is a containerization platform",
    "React is a frontend library",
    "AWS provides cloud services",
]

# ==========================================
# Create Embeddings
# ==========================================

embeddings = model.encode(documents)

print("=" * 50)
print("EMBEDDING SHAPE")
print("=" * 50)

print(embeddings.shape)

print("\n")

print("=" * 50)
print("FIRST DOCUMENT EMBEDDING")
print("=" * 50)

print(embeddings[0][:20])

print("\n")

# ==========================================
# Create FAISS Index
# ==========================================

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

# ==========================================
# Add Embeddings to FAISS
# ==========================================

index.add(
    np.array(
        embeddings
    ).astype(
        "float32"
    )
)

print("=" * 50)
print("FAISS INFO")
print("=" * 50)

print(
    "Total Vectors:",
    index.ntotal
)

print("\n")

# ==========================================
# Retrieve Vector from FAISS
# ==========================================

stored_vector = index.reconstruct(0)

print("=" * 50)
print("VECTOR STORED INSIDE FAISS")
print("=" * 50)

print(stored_vector[:20])

print("\n")

# ==========================================
# Query
# ==========================================

query = (
    "How do containers work?"
)

query_embedding = model.encode(
    [query]
)

print("=" * 50)
print("QUERY EMBEDDING")
print("=" * 50)

print(
    query_embedding[0][:20]
)

print("\n")

# ==========================================
# Search
# ==========================================

distances, indices = index.search(
    np.array(
        query_embedding
    ).astype(
        "float32"
    ),
    k=2
)

# ==========================================
# Results
# ==========================================

print("=" * 50)
print("QUERY")
print("=" * 50)

print(query)

print("\n")

print("=" * 50)
print("DISTANCES")
print("=" * 50)

print(distances)

print("\n")

print("=" * 50)
print("INDICES")
print("=" * 50)

print(indices)

print("\n")

print("=" * 50)
print("TOP MATCHES")
print("=" * 50)

for rank, idx in enumerate(
    indices[0]
):
    print(
        f"{rank + 1}.",
        documents[idx]
    )