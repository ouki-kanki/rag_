from langchain_chroma import Chroma

from src.embedding.embedder import (
    get_embedding_model,
)

from src.config import CHROMA_DB_PATH


def create_vector_store(chunks):
    embedding_model = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=str(CHROMA_DB_PATH),
    )

    return vector_store
