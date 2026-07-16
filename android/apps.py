from android.adb import ADB


class Apps:

    APPS = {
        "youtube": "com.google.android.youtube",
        "whatsapp": "com.whatsapp",
        "chrome": "com.android.chrome",
        "spotify": "com.spotify.music",
        "camera": "com.android.camera",
    }

    @classmethod
    def open(cls, app_name: str):

        package = cls.APPS.get(app_name.lower())

        if not package:
            raise ValueError(f"Unknown app: {app_name}")

        ADB.shell(f"monkey -p {package} 1")