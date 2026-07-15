import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Model
MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")

# Project Paths
DOCUMENTS_PATH = "documents"
VECTOR_DB_PATH = "vector_db"

# Validation
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

if not WEATHER_API_KEY:
    raise ValueError("WEATHER_API_KEY not found in .env file")