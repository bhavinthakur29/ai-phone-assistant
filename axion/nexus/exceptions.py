"""
Nexus exceptions.
"""


class NexusError(Exception):
    """
    Base Nexus communication error.
    """


class ADBError(NexusError):
    """
    Raised when ADB command execution fails.
    """