from utilities.util import *
from domain.island import *
from ascii.island_proxy import *
from ascii.penguin_renderer import *
import os
from pytimedinput import *
from rich.console import Console

# this is the local terminal version

boardSize = BOARDSIZE
cellSize = 6
if boardSize == 12 :
    cellSize = 4
selected_penguin = 0
timed = False

initiate_names()

def show_island(an_island):
    global selected_penguin
    # console.print(selected_penguin)
    console = Console()

    if timed : os.system('clear')
    island_proxy = Island_proxy(an_island) 

    headerLine = f'[bright_black]{DL_DR}'
    numberedLine = f'[bright_black]{DL_VR}'
    downLine = f'[bright_black]{DL_UR}'
    for i in range(boardSize):
          headerLine += DL_H_STR[0:cellSize]
          downLine += DL_H_STR[0:cellSize]
          numberedLine += f"{DL_H_STR[0:2]}{convert_to_alpha(i)}{DL_H_STR[0:3]}"[:cellSize]
    headerLine += f"{DL_HD}{DL_H_STR}{DL_DL}"
    numberedLine += f"{DL_VH}{DL_H_STR}{DL_VL}"
    downLine += f"{DL_HU}{DL_H_STR}{DL_UL}"

    """Displays an image of the island in ascii format"""
    console.print(headerLine)
    console.print(f'[bright_black]{DL_V} {island_proxy.get_info()[0:boardSize * cellSize + -2]} {DL_V} Penguins             {DL_V}')
    console.print(numberedLine)
    infoList = []
    penguinCnt = 0

    selected_line0 = ""
    selected_line1 = ""
    selected_line2 = ""

    for penguin in an_island.penguins.values():
        if penguin.alive or penguin.deadAge < 6:
            color = '[cyan]'
            if penguin.id == selected_penguin : color = '[white]'
            infoList.append(f'[bright_black]{DL_V}{color}{get_penguin_oneliner(penguin)[0][0:22]}[bright_black]{DL_V}')
            penguinCnt += 1     
            
        if penguin.id == selected_penguin:
            if penguin.alive:
                selected_line0 = f' {penguin.name.title()} ({penguin.id})                       '
                selected_line1 = get_penguin_info(penguin)[0]
                selected_line2 = get_penguin_info(penguin)[1]
            else:
                selected_penguin = 0
    
    infoList.append(f"[bright_black]{DL_VR}{DL_H_STR}{DL_VL}")
    
    if selected_penguin > 0 :
        infoList.append(f"[bright_black]{DL_V}[white]{selected_line0[0:22]}[bright_black]{DL_V}")
        infoList.append(f"[bright_black]{DL_V}[white]{selected_line1[0:22]}[bright_black]{DL_V}")
        infoList.append(f"[bright_black]{DL_V}[white]{selected_line2[0:22]}[bright_black]{DL_V}")
        infoList.append(f"[bright_black]{DL_VR}{DL_H_STR}{DL_VL}")
        penguinCnt += 4
    

    infoList.append(f"[bright_black]{DL_V} Log                  {DL_V}")
    infoList.append(f"[bright_black]{DL_VR}{DL_H_STR}{DL_VL}")
    cntlog = 1
    while cntlog < 25 - penguinCnt :
        infoList.append(f'[bright_black]{DL_V}[cyan] {get_event_log(cntlog)[0:21]}[bright_black]{DL_V}')
        cntlog += 1
    
    if cellSize == 4:
        for i in range(boardSize):
            lane1 = f'[bright_black]{DL_V}'
            lane2 = f'[bright_black]{convert_to_alpha(i)}'
            for j in range(boardSize):
                bg = island_proxy.get_cell_bg(i, j)
                lane1 += island_proxy.get_cell_ascii(i, j, selected_penguin,cellSize)[0]
                lane2 += island_proxy.get_cell_ascii(i, j, selected_penguin,cellSize)[1]
                                     
            lane1 += f'{infoList[i*2]}'
            lane2 += f'{infoList[i*2 +1]}'

            console.print(lane1)
            console.print(lane2)
    else:        
        for i in range(boardSize):
            lane1 = f'[bright_black]{DL_V}'
            lane2 = f'[bright_black]{convert_to_alpha(i)}'
            lane3 = f'[bright_black]{DL_V}'
            for j in range(boardSize):
                bg = island_proxy.get_cell_bg(i, j)
                lane1 += island_proxy.get_cell_ascii(i, j, selected_penguin,cellSize)[0]
                lane2 += island_proxy.get_cell_ascii(i, j, selected_penguin,cellSize)[1]
                lane3 += island_proxy.get_cell_ascii(i, j, selected_penguin,cellSize)[2]                     
                                     
            lane1 += f'{infoList[i*3]}'
            lane2 += f'{infoList[i*3 +1]}'
            lane3 += f'{infoList[i*3 +2]}'

            console.print(lane1)
            console.print(lane2)
            console.print(lane3)
    console.print(downLine)


# console.print_format_table(
island = Island(boardSize)

# console.print(island.get_data())
show_island(island)

while True:

    if timed:
        command,_ = timedInput("? ",timeout=1)
    else:
        command = input("? ")
    
    commands = command.split(" ")

    if len(commands) == 1 and len(commands[0]) == 2:
        tmpcommands = []
        tmpcommands.append(commands[0][0:1])
        tmpcommands.append(commands[0][1:2])
        commands = tmpcommands

    if commands[0] == "q":
        break
    if commands[0] == "t":
        timed = not timed
    elif commands[0] == "n":
        if len(commands) > 1 and commands[1].isdigit():
            boardSize = int(commands[1])
        selected_penguin = 0
        island = Island(boardSize)
        show_island(island)
    elif commands[0].isdigit():
        if int(commands[0]) > 0:
            if len(commands) > 1:
                island.transmit_commands(int(commands[0]), commands[1:])
                selected_penguin = int(commands[0])
                show_island(island)
            else:
                if int(commands[0]) == selected_penguin:
                    selected_penguin = 0
                else:
                    selected_penguin = int(commands[0])
                if not timed:
                    island.become_older(True)
                show_island(island)
    elif len(commands) == 1 and len(commands[0]) == 1  and selected_penguin > 0:
        island.transmit_commands(selected_penguin, commands[0])
        if not timed:
            island.become_older(True)
        show_island(island)
    else:
        island.become_older(True)
        show_island(island)

