garbageTypes1 = ('  xx  ', '   xx ', ' xxx  ', '   xx ','  xxx ')
garbageTypes2 = (' xxx  ', '  xx  ', '  xx  ', '  xxx ',' xxx  ') 
garbageTypes3 = ('    x ', '   xx ', ' xx   ', '   xx ','  x x ')
    
def get_garbage_ascii(self):
    """ returns the ascii image of the garbage """
    return [garbageTypes1[self.kind],garbageTypes2[self.kind],garbageTypes3[self.kind],231,231]
