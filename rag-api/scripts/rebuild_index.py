import subprocess
import sys


def rebuild_index():
    print("\nRebuilding FAISS index...")

    result = subprocess.run(
        [
            sys.executable,
            "scripts/build_index.py"
        ],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print(result.stderr)
        raise Exception(
            "Index rebuild failed"
        )

    print("Index rebuild complete.")