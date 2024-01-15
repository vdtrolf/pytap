from utilities.util import *
from colorama import Fore
    
def get_gem_ascii(gem,cell_bg):
    """ returns the ascii image of the gem """
    color = Fore.CYAN
    if gem.hasShowel : color = Fore.WHITE


    if gem.age > 6:
        return [f'{Fore.GREEN}{cell_bg[0]}{Fore.CYAN}/{color}/\\{Fore.CYAN}\\{Fore.GREEN}{cell_bg[0]}',f'{Fore.GREEN}{cell_bg[2]}{Fore.CYAN}\\{color}\\/{Fore.CYAN}/{Fore.GREEN}{cell_bg[2]}',f'{Fore.GREEN}{cell_bg[4]}{cell_bg[4]}{cell_bg[4]}{cell_bg[4]}{cell_bg[4]}{cell_bg[4]}',231,231]
    else :
        return [f'{Fore.GREEN}{cell_bg[0]}{cell_bg[0]}{color}/\\{Fore.GREEN}{cell_bg[0]}{cell_bg[0]}',f'{Fore.GREEN}{cell_bg[2]}{cell_bg[2]}{color}\\/{Fore.GREEN}{cell_bg[2]}{cell_bg[2]}',f'{Fore.GREEN}{cell_bg[4]}{cell_bg[4]}{cell_bg[4]}{cell_bg[4]}{cell_bg[4]}{cell_bg[4]}',231,231]

    # if self.age > 6:
    #     return [f'{cell_bg[0]}{DL_DR}{DL_DR}{DL_DL}{DL_DL}{cell_bg[0]}',f'{cell_bg[2]}{DL_V}{DL_V}{DL_V}{DL_V}{cell_bg[2]}',f'{cell_bg[4]}{DL_UR}{DL_UR}{DL_UL}{DL_UL}{cell_bg[4]}',231,231]
    # else :
    #     return [f'{cell_bg[0]}{cell_bg[0]}{DL_DR}{DL_DL}{cell_bg[0]}{cell_bg[0]}',f'{cell_bg[2]}{cell_bg[2]}{DL_V}{DL_V}{cell_bg[2]}{cell_bg[2]}',f'{cell_bg[4]}{cell_bg[4]}{DL_UR}{DL_UL}{cell_bg[4]}{cell_bg[4]}',231,231]
