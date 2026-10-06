from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
        splits the loaded document to chunks
    Args:
        documents (_type_): _description_

    Returns:
        _type_: _description_
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    return splitter.split_documents(documents)
