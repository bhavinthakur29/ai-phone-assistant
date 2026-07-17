import shlex
from android.adb import ADBController
from android.apps import AppManager
from android.media import MediaManager
from android.youtube import YouTubeManager



class CommandDispatcher:
    """Dynamically routes text commands to their underlying execution functions."""
    
    def __init__(self):
        self.registry = {}
        self._register_core_commands()

    def register(self, command_name: str, func):
        """Binds a command keyword to a specific Python function."""
        self.registry[command_name] = func

    def _register_core_commands(self):
        """Pre-loads the standard Axion engine commands."""
        # Hardware & Navigation
        self.register("home", lambda: ADBController.keyevent("KEYCODE_HOME"))
        self.register("back", lambda: ADBController.keyevent("KEYCODE_BACK"))
        self.register("power", lambda: ADBController.keyevent("KEYCODE_POWER"))
        
        # Screen Inputs
        self.register("tap", lambda x, y: ADBController.tap(x, y))
        self.register("type", lambda *args: ADBController.type_text(" ".join(args)))
        self.register("swipe", lambda x1, y1, x2, y2: ADBController.swipe(x1, y1, x2, y2))
        
        # App Lifecycle
        self.register("open", lambda pkg: AppManager.open_app(pkg))
        self.register("close", lambda pkg: AppManager.close_app(pkg))
        self.register("browse", lambda url: AppManager.browse(url))

        # Add these inside _register_core_commands()
        self.register("play", lambda: MediaManager.play_pause())
        self.register("next", lambda: MediaManager.next_track())
        self.register("yt", lambda query: YouTubeManager.search(query))
        
        # Extended Interactions
        self.register("scroll", lambda direction: ADBController.scroll(direction))
        self.register("clear", lambda: ADBController.clear_text())
        
        # System Queries
        self.register("battery", lambda: ADBController.get_battery())
        self.register("screen", lambda: ADBController.get_screen_size())
        

    def dispatch(self, user_input: str) -> str:
        """Parses a raw string and triggers the registered function."""
        parts = shlex.split(user_input)
        if not parts:
            return ""
        
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd in self.registry:
            try:
                result = self.registry[cmd](*args)
                # Output 'Success' if the ADB command returns an empty string on execution
                return result if result else f"Command '{cmd}' executed successfully."
            except TypeError as e:
                return f"Execution Error: Incorrect arguments for '{cmd}'. Details: {e}"
            except Exception as e:
                return f"Execution Error: {e}"
        else:
            return f"Engine Error: Unknown command '{cmd}'."
        
