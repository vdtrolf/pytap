import random
from json import JSONEncoder
import json

from util import random_direction

class Gem:

    def __init__(self,vpos,hpos):
        self.vpos = vpos
        self.hpos = hpos
        self.age = 10
    
    def get_ascii(self):
        """ returns the ascii image of the gem """
        if self.age > 5:
            return ["//\\\\","\\\\//",15,15]
        else :
            return [" /\\ ", " \\/ ", 15,15]

    def become_older(self):
        """makes the gem becoming older"""
        if self.age > 0:
            self.age -= 1
        
