import random
from json import JSONEncoder
import json

from util import random_direction

class Fish:

    def __init__(self,vpos,hpos):
        self.vpos = vpos
        self.hpos = hpos
    
    def get_ascii(self):
        """ returns the ascii image of thr fish """
        return ["><ò>","~~~~",15,239]
        
    def become_older(self,cells,size):
        """makes the fish move and become older"""
        dir = random_direction(self.vpos,self.hpos)
        if dir[0] > 0 and dir[0] < size and dir[1] > 0 and dir[1] < size and cells[dir[0]][dir[1]].isSea():
            self.vpos = dir[0]
            self.hpos = dir[1]
            
class FishEncoder(JSONEncoder):
    def default(self,object):
        if isinstance(object,Fish):
            return object.__dict__
        else:
            return json.JSONEncoder.default(self,object)