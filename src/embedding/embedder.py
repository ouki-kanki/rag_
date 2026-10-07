from langchain_ollama import OllamaEmbeddings


def get_embedding_model():
    """creates and return an Ollama embedding model"""

    return OllamaEmbeddings(model="nomic-embed-text")
