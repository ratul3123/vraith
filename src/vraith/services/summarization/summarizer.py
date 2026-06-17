from langchain_text_splitters import RecursiveCharacterTextSplitter

from vraith.chains.map_chain import map_chain
from vraith.chains.combine_chain import combine_chain
from vraith.chains.title_chain import title_chain

def split_transcript(transcript: str) -> list:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 3000,
        chunk_overlap = 200
    )
    
    return splitter.split_text(transcript)

def summarize(transcript: str) -> str:
    chunks = split_transcript(transcript)
    chunk_summaries = [map_chain.invoke({"text": chunk}) for chunk in chunks]
    combined = "\n".join(chunk_summaries)
    
    return combine_chain.invoke(combined)

def generate_title(transcript: str) -> str:    
    return title_chain.invoke(transcript[:2000])