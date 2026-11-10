import os
from dotenv import load_dotenv

load_dotenv()

# For Gemini API
GEMINI_MODEL = 'gemini-3.1-flash-lite'
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Model hyperparameters
TEMPERATURE = 0.15
MAX_OUT_TOKENS = 3000
TOP_K = 2