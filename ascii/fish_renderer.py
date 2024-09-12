from colorama import Fore

def get_fish_ascii(fish,cellSize):
	""" returns the ascii image of the fish """
	if cellSize == 4 :
		if fish.onHook :
			return [[Fore.BLUE + "\\/x\\",Fore.BLUE + "/\\_/",''],[Fore.BLUE + "/x\\/",Fore.BLUE + "\\_/\\",'']][fish.angle]
		else:
			return [[Fore.BLUE + "\\/o\\",Fore.BLUE + "/\\_/",''],[Fore.BLUE + "/o\\/",Fore.BLUE + "\\_/\\",'']][fish.angle]
	else :
		if fish.onHook :
			return [[Fore.BLUE + "   __ ",Fore.BLUE + "|\\/ x\\",Fore.BLUE + "|/\\__/"],[Fore.BLUE + " __   ",Fore.BLUE + "/x \\/|",Fore.BLUE + "\\__/\\|",]][fish.angle]
		else :
			return [[Fore.BLUE + "   __ ",Fore.BLUE + "|\\/ o\\",Fore.BLUE + "|/\\__/"],[Fore.BLUE + " __   ",Fore.BLUE + "/o \\/|",Fore.BLUE + "\\__/\\|",]][fish.angle]
    
