import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")
SARVAM_STT_TRANSLATE_URL = "https://api.sarvam.ai/speech-to-text-translate"

if not SARVAM_API_KEY:
    raise ValueError("SARVAM_STT_MODEL is not set in the environment variables.")