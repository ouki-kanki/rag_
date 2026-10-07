from src.ingestion.loader import load_pdf_document
from src.ingestion.splitter import split_documents

from src.ingestion.inspector import (
    print_chunk,
    print_chunk_preview,
    print_chunk_summary,
)
from src.retrieval.retriever import build_retriever
from src.llm.rag_chain import RagChain

from vector_store.chroma_store import create_vector_store


def main():
    document = load_pdf_document("data/raw/pdf/Pathfinder_Core_Rulebook.pdf")
    chunks = split_documents(document)

    print_chunk(chunks)
    print_chunk_preview(chunks)
    print_chunk_summary(chunks)

    vector_store = create_vector_store(chunks)
    retriever = build_retriever(vector_store)

    rag = RagChain(retriever)

    result = rag.ask("what is a Wizard")

    print(result["answer"])

    # test the embedder and vector_db
    # results = vector_store.similarity_search("Tell me about the Wizard class", k=3)
    # results = retriever.invoke("Tell me about the wizard class")

    # for i, doc in enumerate(results):
    #     print(f"\nResult #{i + 1}")
    #     print(f"Metadata: {doc.metadata}")
    #     print(doc.page_content[:500])


if __name__ == "__main__":
    main()
