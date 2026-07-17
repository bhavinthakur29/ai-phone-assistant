class IntentParser:
    """Translates natural language into Axion engine commands."""
    
    @staticmethod
    def parse(raw_text: str) -> str:
        # TODO: Implement NLP logic or Regex mapping here later
        # For now, it just passes the raw text through
        return raw_text.strip()