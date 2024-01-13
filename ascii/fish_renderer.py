def get_fish_ascii(fish):
    """ returns the ascii image of the fish """
    if fish.onHook :
        return [["   __ ","|\\/ x\\","|/\\__/"],[" __   ","/x \\/|","\\__/\\|",]][fish.angle]
    else :
        return [["   __ ","|\\/ o\\","|/\\__/"],[" __   ","/o \\/|","\\__/\\|",]][fish.angle]
    
