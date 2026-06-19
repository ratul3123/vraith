from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from vraith.prompts import rag_prompt
from vraith.utils.llm import get_llm

def format_docs(docs):
    """Flattens retrieved metadata/documents arrays into a raw textual context."""
    return "\n\n".join([doc.page_content for doc in docs])


def get_rag_chain(retriever):
    """
    Factory function that accepts a dynamic database retriever 
    and returns a unique, configured LangChain LCEL sequence.
    """
    return (
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough()
        }
        | rag_prompt 
        | get_llm()
        | StrOutputParser()
    )