"""
Axion runtime path management.

Vault owns all runtime directories used by Axion.

No subsystem should create runtime folders directly.
"""

from __future__ import annotations

from pathlib import Path


class RuntimePaths:
    """
    Provides centralized runtime filesystem paths.
    """

    def __init__(self) -> None:
        self.root = Path(".axion")

        self.logs = self.root / "logs"
        self.cache = self.root / "cache"
        self.config = self.root / "config"
        self.temp = self.root / "temp"
        self.reports = self.root / "reports"
        self.workflows = self.root / "workflows"
        self.plugins = self.root / "plugins"
        self.sessions = self.root / "sessions"

    def initialize(self) -> None:
        """
        Create required runtime directories.
        """

        directories = [
            self.root,
            self.logs,
            self.cache,
            self.config,
            self.temp,
            self.reports,
            self.workflows,
            self.plugins,
            self.sessions,
        ]

        for directory in directories:
            directory.mkdir(
                parents=True,
                exist_ok=True,
            )

paths = RuntimePaths()
paths.initialize()