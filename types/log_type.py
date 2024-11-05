from dataclasses import dataclass

@dataclass
class Log:
    """Class for keeping track of a log"""
    key: int
    entries: list[str]
