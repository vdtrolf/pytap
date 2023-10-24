
import time
import sys
from xtermcolor import colorize

from island import *
from util import *

boardSize = 12
# int(input("size ? :"))

initiate_names()						

headerLine = DL_DR
numberedLine = DL_VR
downLine = DL_UR
for i in range(boardSize) : 
    headerLine += DL_H_STR[0:4]
    downLine += DL_H_STR[0:4]
    numberedLine += f"{DL_H_STR[0:1]}{convert_to_alpha(i)}{DL_H_STR[0:2]}"
headerLine += f"{DL_HD}{DL_H_STR}{DL_DL}"
numberedLine += f"{DL_VH}{DL_H_STR}{DL_VL}"
downLine += f"{DL_HU}{DL_H_STR}{DL_UL}"

def show_island(an_island) :
    """Displays an image of the island in ascii format"""
    print(colorize(headerLine,ansi=245,ansi_bg=232))
    print(colorize(f"{DL_V} {island.get_info()}"[0:boardSize*4 +1] + f"{DL_V} Penguins           {DL_V}",ansi=245,ansi_bg=232))
    print(colorize(numberedLine,ansi=245,ansi_bg=232))
    isInList = True
    penguinList = []
    for penguin in an_island.penguins.values():
        if penguin.alive or penguin.deadAge < 6:
            penguinList.append(penguin)
    cntlog=0
    for i in range(boardSize			) : 
        lane1 = colorize(f'{convert_to_alpha(i)}',ansi=245,ansi_bg=232)
        lane2 = colorize(DL_V,ansi=245,ansi_bg=232)
        for j in range(boardSize):
            bg = an_island.get_cell_bg(i,j)
            lane1 += colorize(an_island.get_cell_ascii(i,j)[0],ansi=an_island.get_cell_ascii(i,j)[2],ansi_bg=bg)
            lane2 += colorize(an_island.get_cell_ascii(i,j)[1],ansi=an_island.get_cell_ascii(i,j)[3],ansi_bg=bg)
        if i < len(penguinList) :    
            lane1 += colorize(f'{DL_V}{penguinList[i].get_info()[0][0:20]}{DL_V}',ansi=245,ansi_bg=232)
            lane2 += colorize(f'{DL_V}{penguinList[i].get_info()[1]}',ansi=245,ansi_bg=232)
            lane2 += colorize('T:',ansi=245,ansi_bg=232)
            lane2 += colorize(f'{penguinList[i].get_info()[2]}',ansi_bg=penguinList[i].get_info()[4],ansi=232)
            lane2 += colorize(' H:',ansi=245,ansi_bg=232)
            lane2 += colorize(f'{penguinList[i].get_info()[3]}',ansi_bg=penguinList[i].get_info()[5],ansi=232)
            lane2 += colorize(DL_V,ansi=245,ansi_bg=232)
        else :
            if isInList :
                lane1 += colorize(f"{DL_VR}{DL_H_STR}{DL_VL}",ansi=245,ansi_bg=232) 
                isInList = False
            else :        
                lane1 += colorize(f'{DL_V}{get_event_log(cntlog)[0:20]}{DL_V}',ansi=245,ansi_bg=232)
            lane2 += colorize(f'{DL_V}{get_event_log(cntlog+1)[0:20]}{DL_V}',ansi=245,ansi_bg=232)
            cntlog +=2
        print(lane1)
        print(lane2)
    print(colorize(downLine,ansi=245,ansi_bg=232))    
     
# print_format_table()    
                      
island = Island(boardSize)
show_island(island)

while True :
    command = input("? ")
    commands = command.split(" ")
    if commands[0] ==  "q":
        break
    elif commands[0]== "n":
        island = Island(boardSize)
        show_island(island)
    elif commands[0].isdigit() :
        if int(commands[0]) > 0 :
            if len(commands) > 1:
                island.transmit_orders(int(commands[0]),commands[1])
            else :
                island.show_penguin_details(int(commands[0]))        
    else:
        island.become_older()
        show_island(island)
        

