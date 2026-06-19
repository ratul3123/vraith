import whisper
from vraith.config.settings import WHISPER_MODEL
from vraith.services.transcription.translator import translate_with_sarvam

_model = None

def load_model():
    global _model

    if _model is None:
        print(f"Loading Whisper Model: {WHISPER_MODEL} ...")
        _model = whisper.load_model(WHISPER_MODEL)
        print("Whisper Model Loaded.")
    return _model

def transcribe_with_whisper(chunk_path: str) -> str:
    model = load_model()
    result = model.transcribe(chunk_path, task="transcribe")
    return result["text"]

def transcribe_chunk(chunk_path: str, language: str = "english") -> str:
    """
    Route one chunk to Whisper or Sarvam depending on language choice.
    - english  → Whisper (local model)
    - banglish → Sarvam (translates to English while transcribing)
    """
    if language.lower() == "banglish":
        return translate_with_sarvam(chunk_path)
    return transcribe_with_whisper(chunk_path)

def transcribe_chunks(chunks: list, language: str = "english") -> str:
    full_transcription = ""

    engine = "Sarvam AI" if language.lower() == "banglish" else "Whisper"
    print(f"Using {engine} for transcription.")

    for i, chunk in enumerate(chunks):
        print(f"Transcribing Chunk {i + 1}/{len(chunks)}...")
        text = transcribe_chunk(chunk, language=language)
        full_transcription += text + " "

    print("Transcription Completed.")
    return full_transcription.strip()