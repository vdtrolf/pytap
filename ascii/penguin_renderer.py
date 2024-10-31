from domain.penguin import *
from colorama import Fore

genders=("M","F")
gender_text= {"M":"Male","F":"Female","m":"male","f":"female"}
asciiEyes = {"M":"[oo]","F":"(00)","m":"oo","f":"00"}
deadEyes = {"M":"[xx]","F":"(xx)","m":" xx ","f":" xx "}
activities_ascii = {ACTIVITY_NONE: "--",ACTIVITY_EATING: "<>", ACTIVITY_FISHING: "-x", ACTIVITY_LOVING: "<3", ACTIVITY_GETING: "-^",ACTIVITY_BUILDING : "-#",ACTIVITY_CLEANING : "-u", ACTIVITY_FLEE: "()", ACTIVITY_MOVING:"--"}
activities_child_ascii = {ACTIVITY_NONE: "()",ACTIVITY_EATING: "<>", ACTIVITY_FISHING: "-x", ACTIVITY_LOVING: "()", ACTIVITY_GETING: "()",ACTIVITY_BUILDING : "()",ACTIVITY_CLEANING : "()", ACTIVITY_FLEE: "()", ACTIVITY_MOVING:"()"}
activities_short = {ACTIVITY_NONE: "   ",ACTIVITY_EATING: "Eat", ACTIVITY_FISHING: "Fsh", ACTIVITY_LOVING: "Lov", ACTIVITY_GETING: "Get",ACTIVITY_BUILDING : "Bld",ACTIVITY_CLEANING : "Cln", ACTIVITY_FLEE: "Fle", ACTIVITY_MOVING:"Mov"}
figures = {0:"Slim", 1:"Fit", 2:"Fat"}


def get_penguin_details(penguin):
    """Returns the details of the penguin (name,age...)"""
    return f'{penguin.name.title()} ({penguin.gender}/{penguin.age})'

def get_penguin_ascii(penguin,cell_bg, selected_penguin):
    """Returns the ascii image of the penguin """
    carries = " "
    color = Fore.CYAN
    if penguin.id == selected_penguin:
        color = Fore.WHITE
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
            return [f'{Fore.GREEN}{cell_bg[0]}{cell_bg[0]}{color}{asciiEyes[gender]}{Fore.GREEN}{cell_bg[0]}{cell_bg[0]}',f"{Fore.GREEN}{cell_bg[0]}{color}<{activities_child_ascii[penguin.activity]}>{Fore.GREEN}{cell_bg[0]}",f"{Fore.GREEN}{cell_bg[4]}{cell_bg[4]}{color}|{penguin.id}{Fore.GREEN}{cell_bg[4]}{cell_bg[4]}"]
        else : 
            return [f'{Fore.GREEN}{cell_bg[0]}{color}{asciiEyes[gender]}{Fore.GREEN}{cell_bg[0]}',f"{color}/({activities_ascii[penguin.activity]})\\",f"{Fore.GREEN}{cell_bg[4]}{color}|{penguin.id}{carries}|{Fore.GREEN}{cell_bg[4]}"]        
    elif penguin.deadAge < 6:
        return [f'{cell_bg[0]}{deadEyes[gender]}{cell_bg[0]}',"/(\\/)\\",f"{cell_bg[4]}|{penguin.id} |{cell_bg[4]}"]
        
def get_penguin_info(penguin):
    """Returns the two lines info of the penguin (name,age...)"""
    if penguin.alive or penguin.deadAge < 6:
        tempText = "Tmp++"
        if penguin.temp > 80:
            tempText = "Tmp--"
        elif penguin.temp > 60:
            tempText = "Tmp- " 
        elif penguin.temp > 40:
            tempText = "Tmp+-" 
        elif penguin.temp > 20:
            tempText = "Tmp+ " 
        hungerText = "Hng++"
        if penguin.hunger > 80:
            hungerText = "Hng--"
        elif penguin.hunger > 60:
            hungerText = "Hng- "  
        elif penguin.hunger > 40:
            hungerText = "Hng+-"  
        elif penguin.hunger > 20:
            hungerText = "Hng+ "  
        carries = "   "
        if penguin.hasFish and penguin.hasGem:
            carries = " <> >o"
        elif penguin.hasFish:
            carries = " >o "
        elif penguin.hasGem:
            carries = " <> "
        if penguin.hasShowel:
            carries += ' -u'
        else:
            carries += '  '    
        
        gender = penguin.gender
        if penguin.isChild: 
            gender = gender.lower()        

        if penguin.alive:
            #  print(f'%%%% {penguin.activity}')
            return [f' {gender_text[gender]}/{int(penguin.age)}y/{figures[penguin.figure]} {activity_names[penguin.activity]}                   ',f' {tempText} {hungerText} {carries}         ','']     
        else:
            return [f' {gender_text[gender]}/{int(penguin.age)}y/{figures[penguin.figure]} Dead                    ',f' {tempText} {hungerText} {carries}                     ','']     
    else:
        return ["","","","","",""]  

def get_penguin_oneliner(penguin):
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
        if penguin.hasShowel:
            carries += 'u'
        else:
            carries += ' '
        gender = penguin.gender
        if penguin.isChild < 4 : 
            gender = gender.lower()        

        if penguin.alive:
            #  print(f'%%%% {penguin.activity}')
            return [f' {convert_to_alpha(penguin.id)}:{gender}/{int(penguin.age)} {activities_short[penguin.activity]}     '[0:11] + f'{tempText} {hungerText} {carries}']     
        else:
            return [f' {convert_to_alpha(penguin.id)}:Dead    {tempText} {hungerText} {carries}']     
    else:
        return ["","","","","",""]  
 

