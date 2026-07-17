"""
Axion application settings.

Central configuration layer.

All modules should obtain configuration
through Vault instead of reading environment
variables directly.
"""

from __future__ import annotations

import os


class ADBSettings:
    """
    Android Debug Bridge configuration.
    """

    path: str = os.getenv(
        "ADB_PATH",
        "adb",
    )


class LLMSettings:
    """
    Language model configuration.
    """

    model: str = "llama3"

    ollama_url: str = (
        "http://localhost:11434/api/generate"
    )


class SpeechSettings:
    """
    Speech subsystem configuration.
    """

    wake_word: str = "axion"

    mic_index: int | None = None


class Settings:
    """
    Root Axion configuration.

    Provides access to all configuration groups.
    """

    adb = ADBSettings()
    llm = LLMSettings()
    speech = SpeechSettings()


settings = Settings()