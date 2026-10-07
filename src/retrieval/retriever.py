def build_retriever(vector_store):
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3},  # return the 3 most relevant chunks
    )
