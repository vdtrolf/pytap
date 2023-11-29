from dataclasses import dataclass

@dataclass
class Gem:
    """Class for keeping track of a gemitam on the island board"""
    key: int
    vpos: int 
    hpos: int        
    age: int
    isTaken: bool = False 