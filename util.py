from pathlib import Path
import random

# CONSTANTS

BOARDSIZE = 9

BOARDSIZE_SMALL = 6
BOARDSIZE_MEDIUM = 9
BOARDSIZE_LARGE = 12

BOARDSIZES = (BOARDSIZE_SMALL,BOARDSIZE_MEDIUM,BOARDSIZE_LARGE)

PROBABILITY_SMELT = 3
PROBABILITY_RISE = 4

WEATHER_RAIN = 0
WEATHER_SUN = 1
WEATHER_COLD = 2
WEATHER_SNOW = 3

SEASON_SPRING = 1
SEASON_SUMMER = 2
SEASON_AUTUMN = 3
SEASON_WINTER = 4

FISH_LETARGY = 3

ACTIVITY_NONE = 0
ACTIVITY_EATING = 1
ACTIVITY_FISHING = 2
ACTIVITY_LOVING = 3
ACTIVITY_GETING = 4
ACTIVITY_BUILDING = 5
ACTIVITY_MOVING = 6
ACTIVITY_CLEANING = 7
ACTIVITY_FLEE = 8
ACTIVITY_DEAD = 9

DIRECTION_NONE = 0
DIRECTION_LEFT = 1
DIRECTION_RIGHT = 2
DIRECTION_UP = 3
DIRECTION_DOWN = 4

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

SHADE_L = "\u2591"
SHADE_M = "\u2592"
SHADE_H = "\u2593"

SHADES_L = "\u2591\u2591\u2591\u2591\u2591\u2591"
SHADES_M = "\u2592\u2592\u2592\u2592\u2592\u2592"
SHADES_H = "\u2593\u2593\u2593\u2593\u2593\u2593"

DL_H_STR = '\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550'

moves = {
    DIRECTION_NONE: [0,0],
    DIRECTION_LEFT: [0, -1],
    DIRECTION_RIGHT: [0, 1],
    DIRECTION_UP: [-1, 0],
    DIRECTION_DOWN: [1, 0]
}
direction_names = {
    DIRECTION_UP: "up",
    DIRECTION_DOWN: "down",
    DIRECTION_LEFT: "left",
    DIRECTION_RIGHT: "right"
}
activity_names = {
    ACTIVITY_NONE: "",
    ACTIVITY_EATING: "Eating",
    ACTIVITY_FISHING: "Fishing",
    ACTIVITY_LOVING: "Loving",
    ACTIVITY_GETING: "Diging",
    ACTIVITY_BUILDING: "Building",
    ACTIVITY_MOVING: "Going",
    ACTIVITY_CLEANING: "Cleaning",
    ACTIVITY_FLEE: "Flee",
    ACTIVITY_DEAD: "Dead"
}
weathers = {
    WEATHER_SUN: 'Sun',
    WEATHER_RAIN: 'Rain',
    WEATHER_SNOW: 'Snow',
    WEATHER_COLD: 'Cold'
}
letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
names_males = []
names_females = []
names_islands = []
events_log = []
keys = []

def initiate_names():
    """Reads the names into the _male, _female and _islands lists"""
    names_file = open('prenoms-hf.txt',
                      encoding="latin-1",
                      errors="surrogateescape")
    for entry in names_file:
        words = entry.rstrip().split(',')
        if len(words) > 1:
            if words[1] == 'm' and len(words[0]) < 9:
                names_males.append(words[0])
            elif words[1] == 'f' and len(words[0]) < 9:
                names_females.append(words[0])
    islands_file = open('iles.txt',
                        encoding="latin-1",
                        errors="surrogateescape")
    for entry in islands_file:
        names_islands.append(entry.rstrip())


def random_direction(vpos, hpos):
    """Returns a random direction in the form of vpos/hpos coords"""
    direction = random.randint(0, 3) + 1
    move = moves[direction]
    return {'vpos': vpos + move[0], 'hpos': hpos + move[1], 'direction': direction, 'directionNum' : direction}


def random_weather(year, weather, weather_age, force=False):
    """Returns a random weather inspired by the season in the form of weather number + name"""

    season_weather = int(year * 4) % 4

    if force or (weather != season_weather and (random.randint(0, 3) == 0 or weather_age > 8)):
        new_weather = season_weather
        return [new_weather, 0, weathers[new_weather]]
    else:
        return [weather, weather_age + 1, weathers[weather]]


def generate_penguin_name(gender):
    """Generates and returns a name for the given gender"""
    if gender == "M":
        return names_males[random.randint(0, len(names_males))]
    else:
        return names_females[random.randint(0, len(names_females))]


def generate_island_name():
    """Generates and returns an island name"""
    return names_islands[random.randint(0, len(names_islands) - 1)]


def get_next_key():
    """Returns the next available key"""
    while True :
        key = random.randint(0,999999) 
        if not key in keys:
            keys.append(key)
            return key


def convert_to_alpha(number):
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
    else:
        return '                                   '


def print_format_table():
    """Prints the available colors"""
    for i in range(16):
        colorStr = ""
        for j in range(16):
            fg = i * 16 + j
            # colorStr += colorize(str(1000 + fg)[1:4],ansi=233,ansi_bg=fg) + " "
        print(colorStr)


