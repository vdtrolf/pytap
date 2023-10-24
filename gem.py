import random
from json import JSONEncoder
import json

from util import *

class Gem:

    def __init__(self,vpos,hpos):
        self.vpos = vpos
        self.hpos = hpos
        self.age = 10
    
    def get_ascii(self):
        """ returns the ascii image of the gem """
        if self.age > 5:
            return [f"{DL_DR}{DL_DR}{DL_DL}{DL_DL}",f"{DL_UR}{DL_UR}{DL_UL}{DL_UL}",231,231]
        else :
            return [f" {DL_DR}{DL_DL} ",f" {DL_UR}{DL_UL} ",231,231]

    def become_older(self,cells):
        """makes the gem becoming older"""
        if cells[self.vpos][self.hpos].isSea():
            self.age = 0
        elif self.age > 0:
            self.age -= 1
        
