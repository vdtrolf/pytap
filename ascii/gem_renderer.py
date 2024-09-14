from utilities.util import *
from colorama import Fore
    
def get_gem_ascii(gem,cell_bg,cellSize):
    """ returns the ascii image of the gem """
    color ='[bright_cyan]'
    if gem.hasShowel : color = '[bright_white]'

    if cellSize == 4:
        if gem.age > 6:
            return [f'{cell_bg}\u2571\u2571\u2572\u2572',f'{cell_bg}\u2572\u2572\u2571\u2571','',231,231]
        else :
            return [f'{cell_bg} \u2571\u2572 ',f'{cell_bg} \u2572\u2571 ','',231,231]
    else:
        if gem.age > 6:
            return [f'{cell_bg} [bright_cyan]/{color}/\\[bright_cyan]\\ ',f'{cell_bg} \\\\// ',f'{cell_bg}      ',231,231]
        else :
            return [f'{cell_bg}  /\\  ',f'{cell_bg}  \\/  ',f'{cell_bg}      ',231,231]

    # if self.age > 6:
    #     return [f'{cell_bg[0]}{DL_DR}{DL_DR}{DL_DL}{DL_DL}{cell_bg[0]}',f'{cell_bg[2]}{DL_V}{DL_V}{DL_V}{DL_V}{cell_bg[2]}',f'{cell_bg[4]}{DL_UR}{DL_UR}{DL_UL}{DL_UL}{cell_bg[4]}',231,231]
    # else :
    #     return [f'{cell_bg[0]}{cell_bg[0]}{DL_DR}{DL_DL}{cell_bg[0]}{cell_bg[0]}',f'{cell_bg[2]}{cell_bg[2]}{DL_V}{DL_V}{cell_bg[2]}{cell_bg[2]}',f'{cell_bg[4]}{cell_bg[4]}{DL_UR}{DL_UL}{cell_bg[4]}{cell_bg[4]}',231,231]
