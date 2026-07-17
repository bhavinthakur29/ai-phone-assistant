import subprocess
import shlex

class ADBController:
    """Core wrapper for executing ADB commands over the established connection."""
    
    @staticmethod
    def execute(command: str) -> str:
        """Executes a raw adb shell command and returns the output."""
        full_command = f"adb shell {command}"
        try:
            result = subprocess.run(shlex.split(full_command), capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f"ADB Error: {e.stderr.strip()}"

    @staticmethod
    def tap(x: int | str, y: int | str) -> str:
        """Simulates a touch event at coordinates."""
        return ADBController.execute(f"input tap {x} {y}")

    @staticmethod
    def type_text(text: str) -> str:
        """Simulates text input, handling spaces properly for the ADB shell."""
        escaped_text = text.replace(" ", "%s").replace("'", "\\'")
        return ADBController.execute(f"input text '{escaped_text}'")

    @staticmethod
    def keyevent(keycode: str) -> str:
        """Sends a hardware keyevent."""
        return ADBController.execute(f"input keyevent {keycode}")

    @staticmethod
    def swipe(x1: int | str, y1: int | str, x2: int | str, y2: int | str, duration: int | str = 300) -> str:
        """Simulates a swipe gesture."""
        return ADBController.execute(f"input swipe {x1} {y1} {x2} {y2} {duration}")
    
    @staticmethod
    def get_battery() -> str:
        """Fetches the current battery level from dumpsys."""
        output = ADBController.execute("dumpsys battery")
        level = "Unknown"
        for line in output.splitlines():
            if "level:" in line:
                level = line.split(":")[1].strip()
        return f"Battery Level: {level}%"

    @staticmethod
    def get_screen_size() -> str:
        """Fetches the physical screen resolution via the window manager."""
        return ADBController.execute("wm size")

    @staticmethod
    def scroll(direction: str) -> str:
        """Simulates a directional swipe for scrolling."""
        direction = direction.lower()
        if direction == "up":
            # Swipe down on the glass to scroll the view up
            return ADBController.swipe(500, 500, 500, 1500)
        elif direction == "down":
            # Swipe up on the glass to scroll the view down
            return ADBController.swipe(500, 1500, 500, 500)
        elif direction == "left":
            return ADBController.swipe(100, 1000, 900, 1000)
        elif direction == "right":
            return ADBController.swipe(900, 1000, 100, 1000)
        return f"Invalid direction: '{direction}'. Use up, down, left, or right."

    @staticmethod
    def clear_text() -> str:
        """Clears text using an ADB keyevent macro."""
        # KEYCODE_MOVE_END (123) jumps to the end of the line.
        # KEYCODE_DEL (67) is the backspace key. We send a batch of backspaces.
        ADBController.execute("input keyevent 123")
        return ADBController.execute("input keyevent " + "67 " * 50)