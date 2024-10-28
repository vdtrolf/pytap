from colorama import Fore

garbageTypes1 = ('x xxxx', 'xxx  x', 'xxxx  ', 'xx xx ','x  xxx')
garbageTypes2 = ('xxxx  ', 'x xx  ', 'x x xx', 'x xxx ',' xxx x') 
garbageTypes3 = ('x  xxx', 'xx xx ', 'x xx x', 'xx xxx','x x xx')
    
def get_garbage_ascii(self):
    """ returns the ascii image of the garbage """
    return [Fore.LIGHTBLACK_EX + garbageTypes1[self.kind],Fore.LIGHTBLACK_EX + garbageTypes2[self.kind],Fore.LIGHTBLACK_EX + garbageTypes3[self.kind],231,231]
