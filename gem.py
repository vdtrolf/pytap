import random
from json import JSONEncoder
import json

from util import *

class Gem:

    def __init__(self,vpos,hpos):
        self.key = get_next_key()
        self.vpos = vpos
        self.hpos = hpos
        self.age = 12
        self.isTaken = False
    
    def get_ascii(self,cell_bg):
        """ returns the ascii image of the gem """
        if self.age > 6:
            return [f'{cell_bg[0]}{DL_DR}{DL_DR}{DL_DL}{DL_DL}{cell_bg[0]}',f'{cell_bg[2]}{DL_V}{DL_V}{DL_V}{DL_V}{cell_bg[2]}',f'{cell_bg[4]}{DL_UR}{DL_UR}{DL_UL}{DL_UL}{cell_bg[4]}',231,231]
        else :
            return [f'{cell_bg[0]}{cell_bg[0]}{DL_DR}{DL_DL}{cell_bg[0]}{cell_bg[0]}',f'{cell_bg[2]}{cell_bg[2]}{DL_V}{DL_V}{cell_bg[2]}{cell_bg[2]}',f'{cell_bg[4]}{cell_bg[4]}{DL_UR}{DL_UL}{cell_bg[4]}{cell_bg[4]}',231,231]

    def become_older(self,cells):
        """makes the gem becoming older"""
        if cells[self.vpos][self.hpos].isSea():
            self.age = 0
        elif self.age > 0:
            self.age -= 1
            
    def get_data(self):
        return {
            'key' : self.key,
            'vpos' : self.vpos,
            'hpos' : self.hpos,
            'age' : self.age,
            'isTaken' : self.isTaken
        }
        
