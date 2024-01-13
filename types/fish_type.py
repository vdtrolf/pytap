from dataclasses import dataclass

@dataclass
class Fish:
    """Class for keeping track of a fish"""
    key: int
    vpos: int
    hpos: int
    onHook: bool  = False
    isDead: bool = False
    angle: int
    direction: int