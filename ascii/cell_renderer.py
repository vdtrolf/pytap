from utilities.util import *

cellTypes1 = ('      ', f'{SHADE_L}  {SHADE_L}  ',f'{SHADE_L}  {SHADE_L}  ',f'  {SHADE_L} {SHADE_L} ',f'{SHADE_L} {SHADE_L} {SHADE_L} ', f'{SHADE_L} {SHADE_L} {SHADE_L} ',f'{SHADE_L} {SHADE_L} {SHADE_L} ', SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_M, SHADES_M, SHADES_M, SHADES_M)
cellTypes2 = ('      ', f'  {SHADE_L}  {SHADE_L}',f'  {SHADE_L}  {SHADE_L}',f' {SHADE_L}   {SHADE_L}',f' {SHADE_L} {SHADE_L} {SHADE_L}', f' {SHADE_L} {SHADE_L} {SHADE_L}',f' {SHADE_L} {SHADE_L} {SHADE_L}', SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_M, SHADES_M, SHADES_M, SHADES_M)
cellTypes3 = ('      ', f'{SHADE_L}  {SHADE_L}  ',f'{SHADE_L}  {SHADE_L}  ',f'  {SHADE_L} {SHADE_L} ',f'{SHADE_L} {SHADE_L} {SHADE_L} ', f'{SHADE_L} {SHADE_L} {SHADE_L} ',f'{SHADE_L} {SHADE_L} {SHADE_L} ', SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_M, SHADES_M, SHADES_M, SHADES_M)

def get_cell_ascii(cell):
    """ returns the ascii image of the cell """
    return [
        cellTypes1[cell.cellType], cellTypes2[cell.cellType], cellTypes3[cell.cellType]
    ]

def get_cell_bg(cell):
    """Returns the left and right characters to be used as background"""
    return [cellTypes1[cell.cellType][0:1],cellTypes1[cell.cellType][5:4],cellTypes2[cell.cellType][0:1],cellTypes2[cell.cellType][5:4],cellTypes3[cell.cellType][0:1],cellTypes3[cell.cellType][5:4]]

