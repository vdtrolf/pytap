import random
from json import JSONEncoder
import json

from util import *

class Fish:

    def __init__(self,vpos,hpos):
        self.key = get_next_key()
        self.vpos = vpos
        self.hpos = hpos
        self.onHook = False
        self.isDead = False
        self.direction = DIRECTION_NONE

    def get_ascii(self):
        """ returns the ascii image of the fish """
        if self.onHook :
            return ["|\\/ x\\","|/\\__/","      ",COLOR_FISH_ONHOOK,239]
        else :
            return ["|\\/ o\\","|/\\__/","      ",COLOR_FISH_OK,239]
        
    def become_older(self,cells,size):
        """makes the fish move and become older"""
        if self.onHook :
            return
        else :
            move = random_direction(self.vpos,self.hpos)
            if random.randint(0,FISH_LETARGY) == 0 and move['vpos'] > 0 and move['vpos'] < size and move['hpos'] > 0 and move['hpos'] < size and cells[move['vpos']][move['hpos']].isSea():
                self.vpos = move['vpos']
                self.hpos = move['hpos']
                self.direction = move['direction']
            else:
                self.direction = DIRECTION_NONE
            
    def get_data(self):
        return {
            'key' : self.key,
            'vpos' : self.vpos,
            'hpos' : self.hpos,
            'onHook' : self.onHook,
            'isDead' : self.isDead,
            'direction' : self.direction
        }
