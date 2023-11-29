from dataclasses import dataclass

@dataclass
class Cell:
    """Class for keeping track of a cell on the island board"""
    key: int
    vpos: int 
    hpos: int        
    cellType: int
    angle: int
