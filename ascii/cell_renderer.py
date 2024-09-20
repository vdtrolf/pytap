from utilities.util import *

cellTypes1 = ('      ', f'{SHADE_L}  {SHADE_L}  ',f'{SHADE_L}  {SHADE_L}  ',f'  {SHADE_L} {SHADE_L} ',f'{SHADE_L} {SHADE_L} {SHADE_L} ', f'{SHADE_L} {SHADE_L} {SHADE_L} ',f'{SHADE_L} {SHADE_L} {SHADE_L} ', SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_M, SHADES_M, SHADES_M, SHADES_M)
cellTypes2 = ('      ', f'  {SHADE_L}  {SHADE_L}',f'  {SHADE_L}  {SHADE_L}',f' {SHADE_L}   {SHADE_L}',f' {SHADE_L} {SHADE_L} {SHADE_L}', f' {SHADE_L} {SHADE_L} {SHADE_L}',f' {SHADE_L} {SHADE_L} {SHADE_L}', SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_M, SHADES_M, SHADES_M, SHADES_M)
cellTypes3 = ('      ', f'{SHADE_L}  {SHADE_L}  ',f'{SHADE_L}  {SHADE_L}  ',f'  {SHADE_L} {SHADE_L} ',f'{SHADE_L} {SHADE_L} {SHADE_L} ', f'{SHADE_L} {SHADE_L} {SHADE_L} ',f'{SHADE_L} {SHADE_L} {SHADE_L} ', SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_L, SHADES_M, SHADES_M, SHADES_M, SHADES_M)

cellbg = ('[green on black]', '[black on grey30]','[black on grey35]','[black on grey39]','[black on grey42]','[black on grey46]','[black on grey50]','[black on grey54]','[black on grey58]','[black on grey66]','[black on grey70]','[black on grey74]','[black on grey78]','[black on grey82]','[black on grey85]','[black on grey89]','[black on grey93]')
cellbg_h = ('[green on black]', '[red on grey30]','[red on grey35]','[red on grey39]','[red on grey42]','[red on grey46]','[red on grey50]','[red on grey54]','[red on grey58]','[red on grey66]','[red on grey70]','[red on grey74]','[red on grey78]','[red on grey82]','[red on grey85]','[red on grey89]','[red on grey93]')


def get_cell_ascii(cell,cellSize):
    """ returns the ascii image of the cell """
    # return [
    #    '[blue on black]' + cellTypes1[cell.cellType][:cellSize], '[blue]' + cellTypes2[cell.cellType][:cellSize], '[blue]' + cellTypes3[cell.cellType][:cellSize]
    # ]

    return [
       cellbg[cell.cellType] + "      "[:cellSize], cellbg[cell.cellType] +"      "[:cellSize], cellbg[cell.cellType] + "      "[:cellSize]
    ]



def get_cell_bg(cell):
    """Returns the left and right characters to be used as background"""
    return cellbg[cell.cellType]
    # return [cellTypes1[cell.cellType][0:1],cellTypes1[cell.cellType][5:4],cellTypes2[cell.cellType][0:1],cellTypes2[cell.cellType][5:4],cellTypes3[cell.cellType][0:1],cellTypes3[cell.cellType][5:4]]

def get_cell_bg_h(cell):
    """Returns the left and right characters to be used as background"""
    return cellbg_h[cell.cellType]