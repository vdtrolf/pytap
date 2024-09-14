
def get_fish_ascii(fish,cellSize):
	""" returns the ascii image of the fish """
	if cellSize == 4 :
		if fish.onHook :
			return [['[dark_sea_green on black]\u2572\u2571x\u2572','[dark_sea_green on black]\u2571\u2572_\u2571',''],['[dark_sea_green on black]\u2571x\u2572\u2571','[dark_sea_green on black]\u2572_\u2571\u2572','']][fish.angle]
		else:
			return [['[dark_sea_green on black]\u2572\u2571o\u2572','[dark_sea_green on black]\u2571\u2572_\u2571',''],['[dark_sea_green on black]\u2571o\u2572\u2571','[dark_sea_green on black]\u2572_\u2571\u2572','']][fish.angle]
	else :
		if fish.onHook :
			return [['[dark_sea_green on black]' + "   __ ",'[dark_sea_green on black]' + "|\\/ x|",'[dark_sea_green on black]' + "|/\\__/"],['[dark_sea_green on black]' + " __   ",'[dark_sea_green on black]' + "|x \\/|",'[dark_sea_green on black] ' + "\\__/\\|",]][fish.angle]
		else :
			return [['[dark_sea_green on black]' + "   __ ",'[dark_sea_green on black]' + "|\\/ o|",'[dark_sea_green on black]' + "|/\\__/"],['[dark_sea_green on black]' + " __   ",'[dark_sea_green on black]' + "|o \\/|",'[dark_sea_green on black] ' + "\\__/\\|",]][fish.angle]
    
