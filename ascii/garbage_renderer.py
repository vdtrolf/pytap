from colorama import Fore

garbageTypes1 = ('  xx  ', '   xx ', ' xxx  ', '   xx ','  xxx ')
garbageTypes2 = (' xxx  ', '  xx  ', '  xx  ', '  xxx ',' xxx  ') 
garbageTypes3 = ('    x ', '   xx ', ' xx   ', '   xx ','  x x ')
    
def get_garbage_ascii(self):
    """ returns the ascii image of the garbage """
    return [Fore.MAGENTA + garbageTypes1[self.kind],Fore.MAGENTA + garbageTypes2[self.kind],Fore.MAGENTA + garbageTypes3[self.kind],231,231]
