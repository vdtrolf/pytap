from utilities.util import *
from domain.island import *
from ascii.island_proxy import *
from ascii.penguin_renderer import *
import os
from pytimedinput import *
from colorama import Fore, init

boardSize = BOARDSIZE
selected_penguin = 0

init(autoreset=True)
initiate_names()

def show_island(an_island):
    os.system('clear')
    island_proxy = Island_proxy(an_island) 

    headerLine = Fore.GREEN + DL_DR
    numberedLine = Fore.GREEN + DL_VR
    downLine = Fore.GREEN + DL_UR
    for i in range(boardSize):
          headerLine += DL_H_STR[0:6]
          downLine += DL_H_STR[0:6]
          numberedLine += f"{DL_H_STR[0:2]}{convert_to_alpha(i)}{DL_H_STR[0:3]}"
    headerLine += f"{DL_HD}{DL_H_STR}{DL_DL}"
    numberedLine += f"{DL_VH}{DL_H_STR}{DL_VL}"
    downLine += f"{DL_HU}{DL_H_STR}{DL_UL}"

    """Displays an image of the island in ascii format"""
    print(headerLine)
    print(Fore.GREEN + f"{DL_V} {island_proxy.get_info()}"[0:boardSize * 6 + 1] +
                 f"{DL_V} Penguins             {DL_V}")
    print(numberedLine)
    infoList = []
    penguinCnt = 0

    selected_line0 = ""
    selected_line1 = ""
    selected_line2 = ""

    for penguin in an_island.penguins.values():
        if penguin.alive or penguin.deadAge < 6:
            infoList.append(f'{Fore.GREEN}{DL_V}{Fore.CYAN}{get_penguin_oneliner(penguin)[0][0:22]}{Fore.GREEN}{DL_V}')
            if penguin.id == selected_penguin:
                selected_line0 = f' {penguin.name.title()} ({penguin.id})                       '
                selected_line1 = get_penguin_info(penguin)[0]
                selected_line2 = get_penguin_info(penguin)[1]
            penguinCnt += 1
    infoList.append(f"{Fore.GREEN}{DL_VR}{DL_H_STR}{DL_VL}")
    
    if selected_penguin > 0 :
        infoList.append(f"{Fore.GREEN}{DL_V}{Fore.WHITE}{selected_line0[0:22]}{Fore.GREEN}{DL_V}")
        infoList.append(f"{Fore.GREEN}{DL_V}{Fore.WHITE}{selected_line1[0:22]}{Fore.GREEN}{DL_V}")
        infoList.append(f"{Fore.GREEN}{DL_V}{Fore.WHITE}{selected_line2[0:22]}{Fore.GREEN}{DL_V}")
        infoList.append(f"{Fore.GREEN}{DL_VR}{DL_H_STR}{DL_VL}")
        penguinCnt += 4
    
    cntlog = 1
    while cntlog < 27 - penguinCnt :
        infoList.append(f'{Fore.GREEN}{DL_V}{Fore.CYAN} {get_event_log(cntlog)[0:21]}{Fore.GREEN}{DL_V}')
        cntlog += 1
    
    for i in range(boardSize):
        lane1 = f'{Fore.GREEN}{DL_V}'
        lane2 = f'{Fore.GREEN}{convert_to_alpha(i)}'
        lane3 = f'{Fore.GREEN}{DL_V}'
        for j in range(boardSize):
            bg = island_proxy.get_cell_bg(i, j)
            lane1 += island_proxy.get_cell_ascii(i, j, selected_penguin)[0]
            lane2 += island_proxy.get_cell_ascii(i, j, selected_penguin)[1]
            lane3 += island_proxy.get_cell_ascii(i, j, selected_penguin)[2]                     
                                     
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

os.system('clear')
show_island(island)

timed = True

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
                show_island(island)
    elif len(commands) == 1 and len(commands[0]) == 1  and selected_penguin > 0:
        island.transmit_commands(selected_penguin, commands[0])
        show_island(island)
    else:
        island.become_older(True)
        show_island(island)

