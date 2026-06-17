import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

WHISPER_MODEL = os.getenv("WHISPER_MODEL", "small")
SARVAM_STT_MODEL = os.getenv("SARVAM_STT_MODEL", "saaras:v3")

if not WHISPER_MODEL:
    raise ValueError("MISTRAL_API_KEY is not set in the environment variables.")

if not SARVAM_STT_MODEL:
    raise ValueError("SARVAM_STT_MODEL is not set in the environment variables.")