from colorama import Fore

def get_fish_ascii(fish):
    """ returns the ascii image of the fish """
    if fish.onHook :
        return [[Fore.LIGHTBLUE_EX + "   __ ",Fore.LIGHTBLUE_EX + "|\\/ x\\",Fore.LIGHTBLUE_EX + "|/\\__/"],[Fore.LIGHTBLUE_EX + " __   ",Fore.LIGHTBLUE_EX + "/x \\/|",Fore.LIGHTBLUE_EX + "\\__/\\|",]][fish.angle]
    else :
        return [[Fore.LIGHTBLUE_EX + "   __ ",Fore.LIGHTBLUE_EX + "|\\/ o\\",Fore.LIGHTBLUE_EX + "|/\\__/"],[Fore.LIGHTBLUE_EX + " __   ",Fore.LIGHTBLUE_EX + "/o \\/|",Fore.LIGHTBLUE_EX + "\\__/\\|",]][fish.angle]
    
