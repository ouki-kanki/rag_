from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_pdf_document(file_path: str | Path):
    """
    Load a PDF file and extracts its pages as LangChain Document objects

    Args:
        file_path (str | Path): _description_
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"No PDF file found at: {path}")

    print(f"[{path.name}] Loading document into memory")

    # Initialize the LangChain Pypdf loader
    loader = PyPDFLoader(str(path))

    # Load pages (returs a list of Document objects)
    docs = loader.load()

    print(f"[{path.name}] Successfully loaded {len(docs)} pages.")

    return docs
