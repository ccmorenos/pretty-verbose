"""Main file of the package with the imports and the aliases."""
from pretty_verbose.logger_classes import Logger
from pretty_verbose.messages_classes import VerboseMessages
from pretty_verbose.processes_classes import Process, Task
from pretty_verbose.error_classes import (
    RunningError, LoggerErrorBase, LoggerError, MissingLogFolderError
)

__all__ = [
    "VerboseMessages",
    "Task", "Process",
    "Logger",
    "RunningError", "LoggerError", "LoggerErrorBase", "MissingLogFolderError"
]
