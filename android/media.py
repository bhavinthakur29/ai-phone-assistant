from .adb import ADBController

class MediaManager:
    """Handles media playback and volume controls."""
    
    @staticmethod
    def play_pause() -> str:
        return ADBController.keyevent("KEYCODE_MEDIA_PLAY_PAUSE")

    @staticmethod
    def next_track() -> str:
        return ADBController.keyevent("KEYCODE_MEDIA_NEXT")

    @staticmethod
    def volume_up() -> str:
        return ADBController.keyevent("KEYCODE_VOLUME_UP")

    @staticmethod
    def volume_down() -> str:
        return ADBController.keyevent("KEYCODE_VOLUME_DOWN")