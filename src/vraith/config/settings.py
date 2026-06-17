import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
WHISPER_MODEL = os.getenv("WHISPER_MODEL", "small")
SARVAM_STT_MODEL = os.getenv("SARVAM_STT_MODEL", "saaras:v3")
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")
SARVAM_STT_TRANSLATE_URL = "https://api.sarvam.ai/speech-to-text-translate"

MODEL_NAME = "mistral-small-latest"
MODEL_TEMPERATURE = 0.3

if not MISTRAL_API_KEY:
    raise ValueError("MISTRAL_API_KEY is not set in the environment variables.")

if not SARVAM_API_KEY:
    raise ValueError("SARVAM_API_KEY is not set in the environment variables.")