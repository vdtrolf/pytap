import random
from json import JSONEncoder
import json

from util import *

class Fish:

    def __init__(self,vpos,hpos):
        self.vpos = vpos
        self.hpos = hpos
        self.onHook = False
        self.isDead = False

    def get_ascii(self):
        """ returns the ascii image of the fish """
        if self.onHook :
            return ["><x>","    ",COLOR_FISH_ONHOOK,239]
        else :
            return ["><ò>","    ",COLOR_FISH_OK,239]
        
    def become_older(self,cells,size):
        """makes the fish move and become older"""
        if self.onHook :
            return
        else :
            direction = random_direction(self.vpos,self.hpos)
            if random.randint(0,FISH_LETARGY) == 0 and direction['vpos'] > 0 and direction['vpos'] < size and direction['hpos'] > 0 and direction['hpos'] < size and cells[direction['vpos']][direction['hpos']].isSea():
                self.vpos = direction['vpos']
                self.hpos = direction['hpos']
            
    def get_data(self):
        return {
            'vpos' : self.vpos,
            'hpos' : self.hpos,
            'onHook' : self.onHook,
            'isDead' : self.isDead
        }
