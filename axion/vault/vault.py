"""
Legacy compatibility layer.

New code should use:
    from axion.vault import settings

Old imports remain supported during migration.
"""

from __future__ import annotations

from axion.vault.settings import settings


class Config:
    """
    Backwards compatible configuration interface.

    Deprecated:
        Use axion.vault.settings instead.
    """

    ADB_PATH = settings.adb.path

    LLM_MODEL = settings.llm.model

    OLLAMA_URL = settings.llm.ollama_url

    WAKE_WORD = settings.speech.wake_word

    MIC_INDEX = settings.speech.mic_index