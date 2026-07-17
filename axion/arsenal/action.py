"""
Base action interface.
"""

from abc import ABC, abstractmethod
from typing import Any


class Action(ABC):
    """
    Base class for all Axion actions.
    """

    @abstractmethod
    def execute(
        self,
        **kwargs: Any,
    ) -> Any:
        """
        Execute action.
        """
        pass