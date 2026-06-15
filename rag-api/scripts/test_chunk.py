from chunker import chunk_text

with open("data/docker.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = chunk_text(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk)