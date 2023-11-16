# from xtermcolor import colorize

from island import *
from util import *

boardSize = BOARDSIZE

initiate_names()

def show_island(an_island):
    headerLine = DL_DR
    numberedLine = DL_VR
    downLine = DL_UR
    for i in range(boardSize):
          headerLine += DL_H_STR[0:6]
          downLine += DL_H_STR[0:6]
          numberedLine += f"{DL_H_STR[0:2]}{convert_to_alpha(i)}{DL_H_STR[0:3]}"
    headerLine += f"{DL_HD}{DL_H_STR}{DL_DL}"
    numberedLine += f"{DL_VH}{DL_H_STR}{DL_VL}"
    downLine += f"{DL_HU}{DL_H_STR}{DL_UL}"

    """Displays an image of the island in ascii format"""
    print(headerLine)
    print(f"{DL_V} {island.get_info()}"[0:boardSize * 6 + 1] +
                 f"{DL_V} Penguins             {DL_V}")
    print(numberedLine)
    infoList = []
    penguinCnt = 0
    for penguin in an_island.penguins.values():
        if penguin.alive or penguin.deadAge < 6:
            infoList.append(f'{DL_V}{penguin.get_info()[0][0:22]}{DL_V}')
            infoList.append(f'{DL_V}{penguin.get_info()[1][0:11]}{(penguin.get_info()[2]+ "             ")[0:11]}{DL_V}')
            penguinCnt += 1
    infoList.append(f"{DL_VR}{DL_H_STR}{DL_VL}")
    cntlog = 1
    while cntlog < 27 - penguinCnt * 2 :
        infoList.append(f'{DL_V}{get_event_log(cntlog)[0:22]}{DL_V}')
        cntlog += 1
    
    for i in range(boardSize):
        lane1 = DL_V
        lane2 = f'{convert_to_alpha(i)}'
        lane3 = DL_V
        for j in range(boardSize):
            bg = an_island.get_cell_bg(i, j)
            lane1 += an_island.get_cell_ascii(i, j)[0]
            lane2 += an_island.get_cell_ascii(i, j)[1]
            lane3 += an_island.get_cell_ascii(i, j)[2]                     
                              
        
        lane1 += f'{infoList[i*3]}'
        lane2 += f'{infoList[i*3 +1]}'
        lane3 += f'{infoList[i*3 +2]}'

        print(lane1)
        print(lane2)
        print(lane3)
    print(downLine)


# print_format_table(
island = Island(boardSize)
# print(island.get_data())

show_island(island)

while True:
    command = input("? ")
    commands = command.split(" ")

    if len(commands) == 1 and len(commands[0]) == 2:
        tmpcommands = []
        tmpcommands.append(commands[0][0:1])
        tmpcommands.append(commands[0][1:2])
        commands = tmpcommands

    if commands[0] == "q":
        break
    elif commands[0] == "n":
        if len(commands) > 1 and commands[1].isdigit():
            boardSize = int(commands[1])
        island = Island(boardSize)
        show_island(island)
    elif commands[0].isdigit():
        if int(commands[0]) > 0:
            if len(commands) > 1:
                island.transmit_commands(int(commands[0]), commands[1:])
                
                show_island(island)
            else:
                island.show_penguin_details(int(commands[0]))
    else:
        island.become_older(True)
        show_island(island)

