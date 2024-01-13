import random
from utilities.util import *

class Garbage:

    def __init__(self,vpos,hpos):
        self.key = get_next_key()
        self.vpos = vpos
        self.hpos = hpos
        self.kind = random.randint(0,4)
        self.isTaken = False
        
    def become_older(self):
        """makes the garbage becoming older - sometimes it chnages shape"""
        if random.randint(0,30) == 0:
            self.kind = random.randint(0,4)
            
    def get_data(self):
        return {
            'key' : self.key,
            'vpos' : self.vpos,
            'hpos' : self.hpos,
            'kind' : self.kind,
            'isTaken' : self.isTaken
        }
        
