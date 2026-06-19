from vraith.services.rag.vector_store import build_vector_store, load_vector_store, get_retriever
from vraith.chains.rag_chain import get_rag_chain

def build_rag_chain(transcript: str):
    vector_store = build_vector_store(transcript)
    retriever = get_retriever(vector_store, k=4)
    
    return get_rag_chain(retriever)

def load_rag_chain():
    vector_store = load_vector_store()
    retriever = get_retriever(vector_store, k=4)
    
    return get_rag_chain(retriever)

def ask_questions(rag_chain, question: str) -> str:
    print(f"Question: {question}")
    answer = rag_chain.invoke(question)
    print(f"Answer: {answer}") 
    return answer