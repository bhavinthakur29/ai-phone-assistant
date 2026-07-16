from android.apps import Apps


class Dispatcher:

    def execute(self, action: dict):

        action_type = action["action"]

        if action_type == "open_app":
            Apps.open(action["app"])
            return

        raise ValueError("Unknown action")