def print_chunk_summary(chunks):
    print("\n=== Chunk Summary ===")
    print(f"Total chunks: {len(chunks)}")

    if chunks:
        avg_size = sum(len(chunk.page_content) for chunk in chunks) / len(chunks)
        print(f"Average chunk size: {avg_size:.0f} chars")


def print_chunk_preview(chunks, limit=3, preview_chars=300):
    print(f"\n=== First {limit} Chunks ===")

    for i, chunk in enumerate(chunks[:limit]):
        print(f"\nChunk #{i+1}")
        print(f"Characters: {len(chunk.page_content)}")
        print(f"Metadata: {chunk.metadata}")

        print("\nPreview:")
        print(chunk.page_content[:preview_chars])
        print("-" * 80)


def print_chunk(chunks, index=0):
    chunk = chunks[index]
    print(f"\nChunk #{index}")
    print(f"Metadata: {chunk.metadata}")
    print(f"Length: {len(chunk.page_content)}")
    print("\nContent:")
    print(chunk.page_content)
