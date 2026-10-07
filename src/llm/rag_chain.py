from langchain_ollama import ChatOllama


class RagChain:
    def __init__(self, retriever):
        self.retriever = retriever

        self.llm = ChatOllama(model="llama3.1:8b", temperature=0)

    def _build_context(self, documents):
        return "\n\n".join(doc.page_content for doc in documents)

    def ask(self, question: str):
        documents = self.retriever.invoke(question)

        context = self._build_context(documents)

        prompt = f"""
            Answer the question using only the provided context.

            Context:{context}
            Question:{question}
        """
        response = self.llm.invoke(prompt)

        return {
            "answer": response.content,
            "sources": documents,
        }
