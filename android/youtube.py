from .adb import ADBController

class YouTubeManager:
    """Handles specific intents for the YouTube application."""
    
    @staticmethod
    def search(query: str) -> str:
        """Opens YouTube directly to a search results page."""
        escaped_query = query.replace(" ", "+")
        intent_url = f"https://www.youtube.com/results?search_query={escaped_query}"
        # Forces the intent to open specifically in the YouTube app package
        return ADBController.execute(
            f"am start -a android.intent.action.VIEW -d '{intent_url}' -p com.google.android.youtube"
        )