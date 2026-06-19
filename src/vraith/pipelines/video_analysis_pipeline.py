from dotenv import load_dotenv
from vraith.services.audio.audio_processor import process_input
from vraith.services.transcription.transcriber import transcribe_chunks
from vraith.services.summarization.summarizer import summarize, generate_title
from vraith.services.extraction.extractor import extract_action_items, extract_decisions, extract_questions
from vraith.services.rag.rag_engine import build_rag_chain

load_dotenv()

def run_pipeline(source: str, language: str = "english") -> dict:
    print("Starting AI Video Assistant")
    
    chunks = process_input(source)
    
    transcript = transcribe_chunks(chunks, language)
    print(f"Raw Transcription (first 300 characters) {transcript[:300]}")
    
    title = generate_title(transcript)
    summary = summarize(transcript)
    action_items = extract_action_items(transcript)
    decisions = extract_decisions(transcript)
    questions = extract_questions(transcript)
    
    rag_chain = build_rag_chain(transcript)
    
    return {
        "title": title,
        "transcript": transcript,
        "summary": summary,
        "action_items": action_items,
        "key_decisions": decisions,
        "open_questions": questions,
        "rag_chain": rag_chain,
    }
    

    