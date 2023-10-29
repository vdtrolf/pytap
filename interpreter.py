from util import *


def get_direction(command, activity):
    """Returns a direction based on an order - in the form of vpos/hpos coords"""
    
    # print(command)
    # print(activity)
    
    if command.title()[0:1] == "U":
        move = moves[DIRECTION_UP]
        return {
            'activity': activity,
            'activityName': activity_names[activity],
            'direction': DIRECTION_UP,
            'vmove': move[0],
            'hmove': move[1],
            'directionName': direction_names[DIRECTION_UP]
        }
    elif command.title()[0:1] == "D":
        move = moves[DIRECTION_DOWN]
        return {
            'activity': activity,
            'activityName': activity_names[activity],
            'direction': DIRECTION_DOWN,
            'vmove': move[0],
            'hmove': move[1],
            'directionName': direction_names[DIRECTION_DOWN]
        }
    elif command.title()[0:1] == "L":
        move = moves[DIRECTION_LEFT]
        return {
            'activity': activity,
            'activityName': activity_names[activity],
            'direction': DIRECTION_LEFT,
            'vmove': move[0],
            'hmove': move[1],
            'directionName': direction_names[DIRECTION_LEFT]
        }
    elif command.title()[0:1] == "R":
        move = moves[DIRECTION_RIGHT]
        return {
            'activity': activity,
            'activityName': activity_names[activity],
            'direction': DIRECTION_RIGHT,
            'vmove': move[0],
            'hmove': move[1],
            'directionName': direction_names[DIRECTION_RIGHT]
        }


def findItem(vpos,hpos,items): 
    """ """
    for direction in range(4):
        coord = (vpos + moves[direction][0]) * 100 + hpos + moves[direction][1]
        if items.get(coord):
            return direction
    return -1


def interpret_commands(commands,vpos,hpos,fishes,gems):
    """returns the given activity as a CONSTANT value"""
    if len(commands) == 1:
        if commands[0].title()[0:1] == "E":
            return {
                'activity': ACTIVITY_EATING,
                'activityName': activity_names[ACTIVITY_EATING],
                'vmove': 0,
                'hmove': 0,
                'directionName': ''
            }
        elif commands[0].title()[0:1] == "F":
            foundDirection = findItem(vpos,hpos,fishes)
            if foundDirection >= 0 :
                move = moves[foundDirection]
                return {
                    'activity': ACTIVITY_FISHING,
                    'activityName': activity_names[ACTIVITY_EATING],
                    'direction': foundDirection,
                    'vmove': move[0],
                    'hmove': move[1],
                    'directionName': direction_names[foundDirection]
               }
        else:
            return get_direction(commands[0], ACTIVITY_MOVING)
    elif len(commands) == 2:
        if commands[0].title()[0:1] == "F":
            return get_direction(commands[1], ACTIVITY_FISHING)
        elif commands[0].title()[0:1] == "G":
            return get_direction(commands[1], ACTIVITY_GETING)
        elif commands[0].title()[0:1] == "B":
            return get_direction(commands[1], ACTIVITY_BUILDING)    
    return {
        'activity': ACTIVITY_NONE,
        'activityName': '',
        'vmove': 0,
        'hmove': 0,
        'directionName': ''
    }

