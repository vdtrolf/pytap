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
        direction = random_direction(self.vpos,self.hpos)
        if direction['vpos'] > 0 and direction['vpos'] < size and direction['hpos'] > 0 and direction['hpos'] < size and cells[direction['vpos']][direction['hpos']].isSea():
            self.vpos = direction['vpos']
            self.hpos = direction['hpos']
            
class FishEncoder(JSONEncoder):
    def default(self,object):
        if isinstance(object,Fish):
            return object.__dict__
        else:
            return json.JSONEncoder.default(self,object)