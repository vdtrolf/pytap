import random
from json import JSONEncoder
import json

from util import *

cellTypes1 = ("~~~~","~~ ~"," ~ ~","  ~ ","  ~ ","  ~ ","    ","    ","    ","    ","    ","    ","    ","    ")
cellTypes2 = ("~~~~","~ ~~","~ ~ "," ~  "," ~  ","    "," ~  ","    ","    ","    ","    ","    ","    ","    ")

cellfg = (239,239,239,0,0,0,0,0,0,0,0,0,0,0,0)
cellbg = (COLOR_WATER,COLOR_ICE1,COLOR_ICE1,COLOR_ICE1,COLOR_ICE2,COLOR_ICE2,COLOR_ICE3,COLOR_ICE3,COLOR_ICE4,COLOR_ICE4,COLOR_GROUND1,COLOR_GROUND2,COLOR_GROUND3)

class Cell:
    cellType=0
    
    def __init__(self,cellType):
        self.cellType=cellType
        
    def get_ascii(self):
        """ returns the ascii image of the cell """
        return [cellTypes1[self.cellType],cellTypes2[self.cellType],cellfg[self.cellType],cellfg[self.cellType]]
        
    def get_bg(self):
        return cellbg[self.cellType]
        
    def isGround(self):
        return self.cellType > 0
        
    def isMount(self):
        return self.cellType > 9
        
    def isSea(self):
        return self.cellType == 0
        
    def become_older(self,weather):
        """makes the fish move and become older"""
        if weather == 0 and self.cellType > 0 and self.cellType < 9 :
            self.cellType -= 1
        elif weather == 2 and self.cellType > 0 and self.cellType < 8 :
            self.cellType += 1    

class CellEncoder(JSONEncoder):
    def default(self,object):
        if isinstance(object,Cell):
            return object.__dict__
        else:
            return json.JSONEncoder.default(self,object)
