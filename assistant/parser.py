class Parser:

    @staticmethod
    def parse(text: str):

        text = text.lower().strip()

        if text.startswith("open "):

            app = text.replace("open ", "")

            return {
                "action": "open_app",
                "app": app
            }

        raise ValueError("Unknown command")