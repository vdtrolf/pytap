from pathlib import Path
import json
import random
from xtermcolor import colorize

# CONSTANTS

PROBABILITY_SMELT = 3
PROBABILITY_RISE = 4

COLOR_GROUND1 = 250
COLOR_GROUND2 = 248
COLOR_GROUND3 = 246

COLOR_ICE1 = 68
COLOR_ICE2 = 69
COLOR_ICE3 = 153
COLOR_ICE4 = 195

COLOR_BG_LIGHT = 255
COLOR_BG_DARK = 232

COLOR_TEXT = 245
COLOR_BG=232

COLOR_SPOT_GOOD = 76
COLOR_SPOT_OK = 79
COLOR_SPOT_MID = 111
COLOR_SPOT_BAD = 222
COLOR_SPOT_CRITIC = 203

COLOR_PENGUIN_OK = 232
COLOR_PENGUIN_BAD = 175
COLOR_PENGUIN_CRITIC = 9

COLOR_WATER = 4

ACTIVITY_NONE = 0
ACTIVITY_EATING = 1
ACTIVITY_FISHING = 2
ACTIVITY_LOVING = 3
ACTIVITY_DIGING =4
ACTIVITY_BUILDING = 5
ACTIVITY_MOVING = 6

DL_V = '\u2551'
DL_DR = "\u2554"
DL_HD = "\u2566"
DL_UR = "\u255a"
DL_VH = "\u256c"
DL_DL = "\u2557"
DL_VL = "\u2563"
DL_UL = "\u255d"
DL_VR = "\u2560"
DL_HU = "\u2569"

DL_H_STR = '\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'

directions = {0:[-1,0],1:[1,0],2:[0,-1],3:[0,1]}
weathers = {0:'Sun',1:'Rain',2:'Snow',3:'Cold'}
letters = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
names_males = []
names_females = []
names_islands = []
events_log = []  

def initiate_names():
    """Reads the names into the _male, _female and _islands lists"""
    names_file = open('prenoms-hf.txt','r')
    for entry in names_file:
        words = entry.rstrip().split(',')
        if len(words) > 1:
            if words[1] == 'm' and len(words[0]) < 9:
                names_males.append(words[0])
            elif words[1] == 'f' and len(words[0]) < 9:
                names_females.append(words[0])
    islands_file = open('iles.txt','r')
    for entry in islands_file:
        names_islands.append(entry.rstrip())

def get_direction(vpos,hpos,order):
    """Returns a direction based on an order - in the form of vpos/hpos coords"""
    if order.title()[0:1] == "U":
        direction = directions[0]
        append_event_to_log("go up")
        return {'vpos':vpos+direction[0],'hpos':hpos+direction[1]}
    elif order.title()[0:1] == "D":
        direction = directions[1]
        append_event_to_log("go down")
        return {'vpos':vpos+direction[0],'hpos':hpos+direction[1]}
    elif order.title()[0:1] == "L":
        direction = directions[2]
        append_event_to_log("go left")
        return {'vpos':vpos+direction[0],'hpos':hpos+direction[1]}
    elif order.title()[0:1] == "R":
        direction = directions[3]
        append_event_to_log("go right")
        return {'vpos':vpos+direction[0],'hpos':hpos+direction[1]}

def get_activity(orders):
    """returns the givan action as a CONSTANT value"""
    if len(orders) == 2: 
        return ACTIVTY_MOVING
    elif orders[1].title[0] == "F":
        return ACTIVITY_FISHING
	elif orders[1].title[0] == "D"
    	return ACTIVITY_DIGING

def random_direction(vpos,hpos):
    """Returns a random direction in the form of vpos/hpos coords"""
    direction = directions[random.randint(0,3)]
    return {'vpos':vpos+direction[0],'hpos':hpos+direction[1]}
    
def random_weather(weather,weather_age, force = False):
    """Returns a random season in the form of season number + name"""
    if force or (weather_age > 4 and random.randint(0,3) == 0):
        new_weather = random.randint(0,3)
        return [new_weather,0,weathers[new_weather]]
    else:
        return [weather, weather_age + 1, weathers[weather]]
    
def generate_penguin_name(gender):
    """Generates and returns a name for the given gender"""
    if gender == "M":
        return names_males[random.randint(0,len(names_males))]
    else:
        return names_females[random.randint(0,len(names_females))]
        
def generate_island_name():
    """Generates and returns an island name"""
    return names_islands[random.randint(0,len(names_islands)-1)]

def convert_to_alpha(number) :
    """Converts a number to an alphannumeric representation"""
    if number < 10:
        return str(number)
    elif number < 36:
        return letters[number - 10]
    return '?' 

def append_event_to_log(event):
    """Appends an event to the event log"""
    events_log.append(event)

def get_event_log(cntlog):
    """Gets the n-1 event log"""
    if cntlog <= len(events_log):
        return events_log[cntlog * -1] + '                                 '
    else :
        return '                                   '

def print_format_table():
    """Prints the available colors"""
    for i in range(16):
        colorStr = ""
        for j in range(16):
            fg = i*16 + j
            colorStr += colorize(str(1000 + fg)[1:4],ansi=233,ansi_bg=fg) + " "
        print(colorStr) 



def dump_island(island):
    path = Path('island.json')
    path.write_text(island_dump)
    
    