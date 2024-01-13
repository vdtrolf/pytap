import random
from utilities.util import *

class Gem:

    def __init__(self,vpos,hpos):
        self.key = get_next_key()
        self.vpos = vpos
        self.hpos = hpos
        self.age = 12
        self.isTaken = False

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
        
