from colorama import Fore

def get_fish_ascii(fish):
    """ returns the ascii image of the fish """
    if fish.onHook :
        return [[Fore.BLUE + "   __ ",Fore.BLUE + "|\\/ x\\",Fore.BLUE + "|/\\__/"],[Fore.BLUE + " __   ",Fore.BLUE + "/x \\/|",Fore.BLUE + "\\__/\\|",]][fish.angle]
    else :
        return [[Fore.BLUE + "   __ ",Fore.BLUE + "|\\/ o\\",Fore.BLUE + "|/\\__/"],[Fore.BLUE + " __   ",Fore.BLUE + "/o \\/|",Fore.BLUE + "\\__/\\|",]][fish.angle]
    
