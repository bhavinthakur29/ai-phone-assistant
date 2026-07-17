import os

class Config:
    """Central configuration for the Axion Engine."""
    # ADB Settings
    ADB_PATH = os.getenv("ADB_PATH", "adb")
    
    # NLP / LLM Settings (For Future Milestones)
    LLM_MODEL = "llama3" # Example local model 
    OLLAMA_URL = "http://localhost:11434/api/generate"
    
    # Speech Settings (For Final Phase)
    WAKE_WORD = "axion"
    MIC_INDEX = None