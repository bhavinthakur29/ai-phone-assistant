from .config import Config

class LLMClient:
    """Handles communication with the local LLM."""
    
    @staticmethod
    def generate_response(prompt: str) -> str:
        # TODO: Implement local model connection (e.g., Ollama)
        pass