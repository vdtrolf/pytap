from domain.penguin import *

genders=("M","F")
asciiEyes = {"M":"[oo]","F":"(00)","m":"oo","f":"00"}
deadEyes = {"M":"[xx]","F":"(xx)","m":" xx ","f":" xx "}
activities_ascii = {ACTIVITY_NONE: "--",ACTIVITY_EATING: "<>", ACTIVITY_FISHING: "-x", ACTIVITY_LOVING: "<3", ACTIVITY_GETING: "-^",ACTIVITY_BUILDING : "-#",ACTIVITY_CLEANING : "-u", ACTIVITY_FLEE: "()", ACTIVITY_MOVING:"--"}
activities_child_ascii = {ACTIVITY_NONE: "()",ACTIVITY_EATING: "<>", ACTIVITY_FISHING: "-x", ACTIVITY_LOVING: "()", ACTIVITY_GETING: "()",ACTIVITY_BUILDING : "()",ACTIVITY_CLEANING : "()", ACTIVITY_FLEE: "()", ACTIVITY_MOVING:"()"}
figures = {0:"Slim", 1:"Fit", 2:"Fat"}


def get_penguin_details(penguin):
    """Returns the details of the penguin (name,age...)"""
    return f'{penguin.name.title()} ({penguin.gender}/{penguin.age})'

def get_penguin_ascii(penguin,cell_bg):
    """Returns the ascii image of the penguin """
    carries = " "
    if penguin.hasFish and penguin.hasGem :
        carries = "§"
    elif penguin.hasFish :
        carries = "~"
    elif penguin.hasGem :
        carries = "^"
    gender = penguin.gender
    if penguin.isChild : 
            gender = gender.lower()
    if penguin.alive:
        if penguin.isChild : 
            return [f'{cell_bg[0]}{cell_bg[0]}{asciiEyes[gender]}{cell_bg[0]}{cell_bg[0]}',f"{cell_bg[0]}<{activities_child_ascii[penguin.activity]}>{cell_bg[0]}",f"{cell_bg[4]}{cell_bg[4]}|{penguin.id}{cell_bg[4]}{cell_bg[4]}"]
        else : 
            return [f'{cell_bg[0]}{asciiEyes[gender]}{cell_bg[0]}',f"/({activities_ascii[penguin.activity]})\\",f"{cell_bg[4]}|{penguin.id}{carries}|{cell_bg[4]}"]        
    elif penguin.deadAge < 6:
        return [f'{cell_bg[0]}{deadEyes[gender]}{cell_bg[0]}',"/(\\/)\\",f"{cell_bg[4]}|{penguin.id} |{cell_bg[4]}"]
        
def get_penguin_info(penguin):
    """Returns the two lines info of the penguin (name,age...)"""
    if penguin.alive or penguin.deadAge < 6:
        tempText = "T++"
        if penguin.temp > 80:
            tempText = "T--"
        elif penguin.temp > 60:
            tempText = "T- " 
        elif penguin.temp > 40:
            tempText = "T+-" 
        elif penguin.temp > 20:
            tempText = "T+ " 
        hungerText = "H++"
        if penguin.hunger > 80:
            hungerText = "H--"
        elif penguin.hunger > 60:
            hungerText = "H- "  
        elif penguin.hunger > 40:
            hungerText = "H+-"  
        elif penguin.hunger > 20:
            hungerText = "H+ "  
        carries = "   "
        if penguin.hasFish and penguin.hasGem:
            carries = " ^~"
        elif penguin.hasFish:
            carries = " ~ "
        elif penguin.hasGem:
            carries = " ^ "
        
        gender = penguin.gender
        if penguin.isChild < 4 : 
            gender = gender.lower()        

        if penguin.alive:
            #  print(f'%%%% {penguin.activity}')
            return [f'{convert_to_alpha(penguin.id)}:{penguin.name.title()} {activity_names[penguin.activity]}                    ',f'  {gender}/{int(penguin.age)}/{figures[penguin.figure]}   '[0:11],f'{tempText} {hungerText} {carries}']     
        else:
            return [f'{convert_to_alpha(penguin.id)}:{penguin.name.title()} - Dead                  ',f'  {gender}/{int(penguin.age)}/{figures[penguin.figure]}   '[0:11],f'{tempText} {hungerText} {carries}']     
    else:
        return ["","","","","",""]  

 

