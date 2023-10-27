from util import *

def get_direction(command, activity):
    """Returns a direction based on an order - in the form of vpos/hpos coords"""
    if command.title()[0:1] == "U":
        move = directions[DIRECTION_UP]
        return {'activity': activity,'activityName' : activity_names[activity], 'direction':DIRECTION_UP,'vmove':move[0],'hmove':move[1],'directionName':direction_names[DIRECTION_UP]}
    elif command.title()[0:1] == "D":
        move = directions[DIRECTION_DOWN]
        return {'activity': activity,'activityName' : activity_names[activity],'direction':DIRECTION_DOWN,'vmove':move[0],'hmove':move[1],'directionName':direction_names[DIRECTION_DOWN]}
    elif command.title()[0:1] == "L":
        move = directions[DIRECTION_LEFT]
        return {'activity': activity,'activityName' : activity_names[activity],'direction':DIRECTION_LEFT,'vmove':move[0],'hmove':move[1],'directionName':direction_names[DIRECTION_LEFT]}
    elif command.title()[0:1] == "R":
        move = directions[DIRECTION_RIGHT]
        return {'activity': activity,'activityName' : activity_names[activity],'direction':DIRECTION_RIGHT,'vmove':move[0],'hmove':move[1],'directionName':direction_names[DIRECTION_RIGHT]}

def interpret_commands(commands):
    """returns the given activity as a CONSTANT value"""
    if len(commands) == 1:
        if commands[0].title()[0:1] == "E":
            return {'activity':ACTIVITY_EATING,'activityName':activity_names[ACTIVITY_EATING],'vmove':0,'hmove':0,'directionName':''} 
        else :
            return get_direction(commands[0],ACTIVITY_MOVING)
    elif len(commands) == 2:
        if commands[0].title()[0:1] == "F":
            return get_direction(commands[1],{'activity':ACTIVITY_FISHING})
        elif commands[0].title()[0:1] == "G":
            return get_direction(commands[1],{'activity':ACTIVITY_GETING})
    return {'activity':ACTIVITY_NONE,'activityName':'','vmove':0,'hmove':0,'directionName':''}
