import os
import json
import logging

import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

# =====================================
# LOGGING
# =====================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# =====================================
# CONFIG
# =====================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

INDEX_PATH = os.path.join(
    BASE_DIR,
    "indexes",
    "skills.index"
)

METADATA_PATH = os.path.join(
    BASE_DIR,
    "indexes",
    "metadata.json"
)

TOP_K = 3

SIMILARITY_THRESHOLD = 0.20

# =====================================
# VALIDATION
# =====================================

if not os.path.exists(INDEX_PATH):
    raise FileNotFoundError(
        f"Index not found: {INDEX_PATH}"
    )

if not os.path.exists(METADATA_PATH):
    raise FileNotFoundError(
        f"Metadata not found: {METADATA_PATH}"
    )

# =====================================
# LOAD MODEL
# =====================================

logging.info(
    "Loading embedding model..."
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

logging.info(
    "Loading FAISS index..."
)

index = faiss.read_index(
    INDEX_PATH
)

with open(
    METADATA_PATH,
    "r",
    encoding="utf-8"
) as f:

    metadata = json.load(f)

logging.info(
    f"Loaded {len(metadata)} documents"
)

# =====================================
# SEARCH FUNCTION
# =====================================

def search_skill(
    query: str,
    top_k: int = TOP_K
):

    query = query.strip()

    if not query:
        raise ValueError(
            "Query cannot be empty"
        )

    logging.info(
        f"Searching for: {query}"
    )

    query_embedding = model.encode(
        [query],
        normalize_embeddings=True
    )

    query_embedding = np.array(
        query_embedding,
        dtype=np.float32
    )

    k = min(
        top_k,
        len(metadata)
    )

    similarities, indices = index.search(
        query_embedding,
        k
    )

    results = []

    seen_files = set()

    for rank, idx in enumerate(
        indices[0]
    ):

        if idx < 0:
            continue

        item = metadata[idx]

        source = item["file"]

        similarity = float(
            similarities[0][rank]
        )

        if similarity < SIMILARITY_THRESHOLD:
            continue

        if source in seen_files:
            continue

        seen_files.add(source)

        results.append(
            {
                "rank": len(results) + 1,
                "similarity": round(
                    similarity * 100,
                    2
                ),
                "source": source,
                "text": item["text"]
            }
        )

    return results

# =====================================
# CHECK IF SKILL EXISTS
# =====================================

def skill_exists(
    skill: str
):

    results = search_skill(
        skill,
        top_k=1
    )

    return len(results) > 0

# =====================================
# CLI TEST
# =====================================

if __name__ == "__main__":

    while True:

        query = input(
            "\nEnter skill (q to quit): "
        ).strip()

        if query.lower() == "q":
            break

        try:

            results = search_skill(
                query
            )

            if not results:

                print(
                    "\nSkill not found in knowledge base."
                )

                continue

            print(
                "\nTop Results\n"
            )

            for item in results:

                print("=" * 70)

                print(
                    f"Rank       : {item['rank']}"
                )

                print(
                    f"Similarity : {item['similarity']}%"
                )

                print(
                    f"Source     : {item['source']}"
                )

                print("\nContent:\n")

                print(
                    item["text"]
                )

                print()

        except Exception as e:

            logging.error(
                str(e)
            )