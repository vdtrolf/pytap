from dataclasses import dataclass

@dataclass
class Garbage:
    """Class for keeping track of a garbage itam on the island board"""
    key: int
    vpos: int 
    hpos: int        
    kind: int
    isTaken: bool = False 
