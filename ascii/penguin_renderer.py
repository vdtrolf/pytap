from domain.penguin import *


genders=("M","F")
gender_text= {"M":"Male","F":"Female","m":"male","f":"female"}
asciiEyes = {"M":"OO","F":"00","m":"oo","f":"oo"}
deadEyes = {"M":"xx","F":"xx","m":" xx ","f":" xx "}
activities_ascii = {ACTIVITY_NONE: "--",ACTIVITY_EATING: "<>", ACTIVITY_FISHING: "-x", ACTIVITY_LOVING: "<3", ACTIVITY_GETING: "-^",ACTIVITY_BUILDING : "-#",ACTIVITY_CLEANING : "-u", ACTIVITY_FLEE: "()", ACTIVITY_MOVING:"--"}
activities_child_ascii = {ACTIVITY_NONE: "()",ACTIVITY_EATING: "<>", ACTIVITY_FISHING: "-x", ACTIVITY_LOVING: "()", ACTIVITY_GETING: "()",ACTIVITY_BUILDING : "()",ACTIVITY_CLEANING : "()", ACTIVITY_FLEE: "()", ACTIVITY_MOVING:"()"}
activities_short = {ACTIVITY_NONE: "   ",ACTIVITY_EATING: "Eat", ACTIVITY_FISHING: "Fsh", ACTIVITY_LOVING: "Lov", ACTIVITY_GETING: "Get",ACTIVITY_BUILDING : "Bld",ACTIVITY_CLEANING : "Cln", ACTIVITY_FLEE: "Fle", ACTIVITY_MOVING:"MOv"}
figures = {0:"Slim", 1:"Fit", 2:"Fat"}


def get_penguin_details(penguin):
    """Returns the details of the penguin (name,age...)"""
    return f'{penguin.name.title()} ({penguin.gender}/{penguin.age})'

def get_penguin_ascii(penguin,cell_bg,cell_bg_h, selected_penguin,cellSize):
    """Returns the ascii image of the penguin """
    carries = " "
    
    color = cell_bg
    if penguin.id == selected_penguin:
        color = cell_bg_h
    if penguin.hasFish and penguin.hasGem :
        carries = "§"
    elif penguin.hasFish :
        carries = "~"
    elif penguin.hasGem :
        carries = "^"
    gender = penguin.gender
    if penguin.isChild : 
            gender = gender.lower()

    ascii_img = []        
    if cellSize == 4:
        if penguin.alive:
            if penguin.isChild : 
                ascii_img = [f'{color} {asciiEyes[gender]} ',f'{color} |{penguin.id} ','']
            else : 
                if penguin.activity > 0 :
                    ascii_img = [f'{color} {asciiEyes[gender]} ',f'{color}|{activities_ascii[penguin.activity]}|','']     
                else:
                    ascii_img = [f'{color} {asciiEyes[gender]} ',f'{color}|{penguin.id}{carries}|','']     
           
        elif penguin.deadAge < 6:
            ascii_img = [f'{color} {deadEyes[gender]} ',f'{color}|{penguin.id} |','']
    else:
        if penguin.alive:
            if penguin.isChild : 
                ascii_img = [f'{color}  {asciiEyes[gender]}  ',f'{color}<{activities_child_ascii[penguin.activity]}> ',f'{color}  {color}|{penguin.id}  ']
            else : 
                ascii_img = [f'{color} |{asciiEyes[gender]}| ',f'{color}<({activities_ascii[penguin.activity]})>',f'{color}{color}|{penguin.id}{carries}|']        
        elif penguin.deadAge < 6:
            ascii_img = [f'{color} |{deadEyes[gender]}| ',"{color}<(\\/)>",f"{color} |{penguin.id} | "]

    return ascii_img

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
 

