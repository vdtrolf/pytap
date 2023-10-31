import random

from util import *


garbageTypes1 = ('      ', '   ## ', ' ###  ', '   ## ','  ### ')
garbageTypes2 = ('      ', '  ##  ', '  ##  ', '  ### ',' ###  ') 
garbageTypes3 = ('      ', '   ## ', ' ##   ', '   #  ','  # # ')

class Garbage:

    def __init__(self,vpos,hpos):
        self.key = get_next_key()
        self.vpos = vpos
        self.hpos = hpos
        self.kind = random.randint(0,4)
        self.isTaken = False
    
    def get_ascii(self):
        """ returns the ascii image of the garbage """
        return [garbageTypes1[self.kind],garbageTypes2[self.kind],garbageTypes3[self.kind],231,231]
        
    def become_older(self):
        """makes the gem becoming older"""
        if random.randint(0,8) == 0:
            self.kind = random.randint(0,4)
            
    def get_data(self):
        return {
            'key' : self.key,
            'vpos' : self.vpos,
            'hpos' : self.hpos,
            'kind' : self.kind,
            'isTaken' : self.isTaken
        }
        
