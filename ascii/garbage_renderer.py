garbageTypes1 = ('x xxxx', 'xxx  x', 'xxxx  ', 'xx xx ','x  xxx')
garbageTypes2 = ('xxxx  ', 'x xx  ', 'x x xx', 'x xxx ',' xxx x') 
garbageTypes3 = ('x  xxx', 'xx xx ', 'x xx x', 'xx xxx','x x xx')
    
def get_garbage_ascii(self,cellSize):
    """ returns the ascii image of the garbage """
    return ['[orange4]' + garbageTypes1[self.kind][:cellSize],'[orange4]' + garbageTypes2[self.kind][:cellSize],'[orange4]' + garbageTypes3[self.kind][:cellSize],231,231]
