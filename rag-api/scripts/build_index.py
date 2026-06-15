import os
import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

# =====================================
# PATHS
# =====================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

INDEX_DIR = os.path.join(
    BASE_DIR,
    "indexes"
)

INDEX_PATH = os.path.join(
    INDEX_DIR,
    "skills.index"
)

METADATA_PATH = os.path.join(
    INDEX_DIR,
    "metadata.json"
)

# =====================================
# BUILD INDEX
# =====================================

def build_index():

    if not os.path.exists(DATA_DIR):
        raise FileNotFoundError(
            f"Data folder not found: {DATA_DIR}"
        )

    os.makedirs(
        INDEX_DIR,
        exist_ok=True
    )

    print(
        "\nLoading embedding model..."
    )

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    documents = []
    metadata = []

    txt_files = sorted(
        [
            file
            for file in os.listdir(DATA_DIR)
            if file.endswith(".txt")
        ]
    )

    if not txt_files:
        raise ValueError(
            "No .txt files found in data folder"
        )

    print(
        f"Found {len(txt_files)} files"
    )

    for filename in txt_files:

        path = os.path.join(
            DATA_DIR,
            filename
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            text = f.read().strip()

        if not text:

            print(
                f"Skipping empty file: {filename}"
            )

            continue

        print(
            f"{filename}: indexed"
        )

        documents.append(
            text
        )

        metadata.append(
            {
                "file": filename,
                "text": text
            }
        )

    if not documents:
        raise ValueError(
            "No documents found"
        )

    print(
        f"\nGenerating embeddings for {len(documents)} documents..."
    )

    embeddings = model.encode(
        documents,
        show_progress_bar=True,
        normalize_embeddings=True
    )

    embeddings = np.array(
        embeddings,
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(
        dimension
    )

    index.add(
        embeddings
    )

    faiss.write_index(
        index,
        INDEX_PATH
    )

    with open(
        METADATA_PATH,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            metadata,
            f,
            indent=2,
            ensure_ascii=False
        )

    print("\nBuild Complete")

    print(
        f"Files Processed: {len(txt_files)}"
    )

    print(
        f"Documents Indexed: {len(documents)}"
    )

    print(
        f"Index Saved: {INDEX_PATH}"
    )

    print(
        f"Metadata Saved: {METADATA_PATH}"
    )

    return {
        "files": len(txt_files),
        "documents": len(documents)
    }


if __name__ == "__main__":
    build_index()