from src.ingestion.loader import load_pdf_document
from src.ingestion.splitter import split_documents

from src.ingestion.inspector import (
    print_chunk,
    print_chunk_preview,
    print_chunk_summary,
)


def main():
    document = load_pdf_document("data/raw/pdf/Pathfinder_Core_Rulebook.pdf")
    chunks = split_documents(document)

    print_chunk(chunks)
    print_chunk_preview(chunks)
    print_chunk_summary(chunks)


if __name__ == "__main__":
    main()
