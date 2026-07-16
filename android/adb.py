import subprocess


class ADB:

    @staticmethod
    def run(command: list[str]) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["adb"] + command,
            capture_output=True,
            text=True
        )

    @staticmethod
    def shell(command: str):

        result = subprocess.run(
            ["adb", "shell", command],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr)

        return result.stdout.strip()