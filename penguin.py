import random
from json import JSONEncoder
from util import *
from interpreter import *

genders=("M","F")
asciiEyes = ("**","11","22","33","44","55","66","77","88")
asciiImg1 = {"M":"[","F":"("}
asciiImg2 = {"M":"]","F":")"}
activities_ascii = {ACTIVITY_NONE: "\\/",ACTIVITY_EATING: "<>", ACTIVITY_FISHING: "/|", ACTIVITY_LOVING: "<3", ACTIVITY_GETING: "-^",ACTIVITY_BUILDING : "-#", ACTIVITY_MOVING:"\\/"}
figures = {0:"Slim", 1:"Fit", 2:"Fat"}


class Penguin:
    
    def __init__(self,id,vpos,hpos):
        """Initiate a penguin with it's id and his position"""
        self.key = get_next_key()
        self.id = id
        self.alive = True
        self.age = random.randint(3,6)
        self.deadAge = 0
        self.hunger = 0
        self.temp = 0
        self.figure = random.randint(0,2)
        self.vpos=vpos
        self.hpos=hpos
        self.gender = genders[random.randint(0,1)]
        self.name = generate_penguin_name(self.gender)
        self.activity = ACTIVITY_NONE
        self.activity_time = 0
        self.activity_direction = 0
        self.activity_target = 0
        self.activity_text = ""
        self.canMove = 0
        self.canFish = 0
        self.canGrab = 0
        self.canBuild = 0
        self.canLove = 0
        self.goal = 0
        self.commands = []
        self.hasFish = False
        self.hasGem = False

    def become_older(self,cells,size,penguins,newpenguins,fishes,gems,weather):
        """makes the penguin move and become older"""
        # check if there is a neighbour
        hasNeighbour =  penguins.get((self.vpos+1)*100 + self.hpos) or penguins.get((self.vpos-1)*100 + self.hpos) or penguins.get(self.vpos*100 + self.hpos -1) or penguins.get(self.vpos*100 + self.hpos +1) 

        if self.alive :
            self.age += 0.5
            if not hasNeighbour :  
                self.temp += weather
            self.hunger += (self.figure +1) * 2

            # Is the penguin dead ?
            if self.age > 20: 
                self.alive = False
                self.activity = ACTIVITY_DEAD
                self.activity_text = f'died (age)'
                append_event_to_log(f'{self.name.title()} died (age)')
                return
            elif self.temp > 99:
                self.alive = False
                self.activity = ACTIVITY_DEAD
                self.activity_text = f'died (cold)'
                append_event_to_log(f'{self.name.title()} died (cold)')
                return
            elif self.hunger > 99:
                self.alive = False
                self.activity = ACTIVITY_DEAD
                self.activity_text = f'died (hunger)'
                append_event_to_log(f'{self.name.title()} died (hunger)')    
                return
            elif cells[self.vpos][self.hpos].cellType == 0:
                self.alive = False
                self.activity = ACTIVITY_DEAD
                self.activity_text = f'died (sunk)'
                append_event_to_log(f'{self.name.title()} died (sunk)')
                return

            # Is there an order to execute
            if self.activity_time > 0:
                self.activity_time -= 1
                if self.activity_time == 0:
                    if self.activity == ACTIVITY_FISHING:
                        self.hasFish = True
                        self.activity = ACTIVITY_NONE
                        self.activity_direction = DIRECTION_NONE
                        fishes[self.acivityTarget].isDead = True
                    elif self.activity == ACTIVITY_GETING:
                        self.hasGem = True
                        self.activity = ACTIVITY_NONE
                        self.activity_direction = DIRECTION_NONE
                        if gems.get(self.acivityTarget):
                            gems[self.acivityTarget].isTaken = True
                    elif self.activity == ACTIVITY_EATING:
                        self.hunger = 0
                        self.hasFish = False
                        self.activity = ACTIVITY_NONE
                        self.activity_direction = DIRECTION_NONE
                    elif self.activity == ACTIVITY_BUILDING:
                        self.temp = 0
                        self.hasGem = False
                        cells[self.activityVPos][self.activityHPos].endBuilding()
                        self.activity = ACTIVITY_NONE 
                        self.activity_direction = DIRECTION_NONE  
                self.goal = ACTIVITY_NONE       
                self.activity_text = activity_names[self.activity]      
            elif len(self.commands) > 0:
                command = interpret_commands(self.commands,self.vpos,self.hpos,fishes,gems)
                direction = {'vpos':self.vpos + command['vmove'],'hpos':self.hpos + command['hmove']}
                coord = direction['vpos']*100 + direction['hpos']
                if command['activity'] == ACTIVITY_MOVING:
                    if direction['vpos'] > 0 and direction['vpos'] < size and direction['hpos'] > 0 and direction['hpos'] < size and not penguins.get(coord) and not newpenguins.get(coord):
                        self.vpos = direction['vpos']
                        self.hpos = direction['hpos']
                        self.activity = command['activity']
                        self.activity_direction = command['directionNum']
                elif command['activity'] == ACTIVITY_FISHING:
                    if fishes.get(coord):
                        fishes[coord].onHook=True
                        self.activity_time = 3
                        self.activity = command['activity']
                        self.goal = command['activity']
                        self.acivityTarget = coord
                        self.activity_direction = command['directionNum']
                    else:      
                        self.activity = ACTIVITY_NONE  
                        self.activity_direction = DIRECTION_NONE              
                elif command['activity'] == ACTIVITY_GETING:
                    if gems.get(coord):
                        self.activity_time = 3  
                        self.activity = command['activity']      
                        self.goal = command['activity']
                        self.acivityTarget = coord
                        self.activity_direction = command['directionNum']
                    else:      
                        self.activity = ACTIVITY_NONE
                        self.activity_direction = DIRECTION_NONE
                elif command['activity'] == ACTIVITY_EATING:
                    if self.hasFish :        
                        self.activity_time = 2  
                        self.activity = command['activity']
                        self.goal = command['activity']
                        self.activity_direction = command['directionNum']
                    else:      
                        self.activity = ACTIVITY_NONE
                        self.activity_direction = DIRECTION_NONE
                elif command['activity'] == ACTIVITY_BUILDING:
                    if self.hasGem and cells[direction['vpos']][direction['hpos']].isSea() :        
                        self.activity_time = 3  
                        self.activityVPos = direction['vpos']
                        self.activityHPos = direction['hpos']
                        cells[self.activityVPos][self.activityHPos].startBuilding()
                        self.activity = command['activity']
                        self.goal = command['activity']
                        self.activity_direction = command['directionNum']
                    else:      
                        self.activity = ACTIVITY_NONE    
                        self.activity_direction = DIRECTION_NONE
                else:
                    self.activity = ACTIVITY_NONE    
                    self.activity_direction = DIRECTION_NONE

                self.activity_text = activity_names[self.activity]                    
                self.commands = []
            # if not and if the penguin is on smelting ice: try to escape
            elif cells[self.vpos][self.hpos].cellType < 3 :
                direction = random_direction(self.vpos,self.hpos)
                coord = direction['vpos']*100 + direction['hpos']
                if direction['vpos'] > 0 and direction['vpos'] < size and direction['hpos'] > 0 and direction['hpos'] < size and cells[direction['vpos']][direction['hpos']].cellType > cells[self.vpos][self.hpos].cellType and not penguins.get(coord) and not newpenguins.get(coord):
                    self.vpos = direction['vpos']
                    self.hpos = direction['hpos']
                    self.activity_direction = direction['directionNum']
                    
        else :
            self.deadAge += 1

    def receive_commands(self,commands) :
        """Receives an order to move or perform an activity"""
        for command in commands:
            if len(command) > 0:
                self.commands.append(command)
     
    def get_ascii(self,cell_bg):
        """Returns the ascii image of the penguin """
        color = COLOR_PENGUIN_OK
        if self.temp > 70 or self.hunger > 70:
            color = COLOR_PENGUIN_CRITIC
        elif self.temp > 50 or self.hunger > 50:
            color = COLOR_PENGUIN_BAD
        if self.alive:
            return [f'{cell_bg[0]}{asciiImg1[self.gender]}{asciiEyes[self.id]}{asciiImg2[self.gender]}{cell_bg[0]}',f"/|{activities_ascii[self.activity]}|\\",f"{cell_bg[4]}|  |{cell_bg[4]}",color,color]
        elif self.deadAge < 6:
            return [f'{cell_bg[0]}{asciiImg1[self.gender]}xx{asciiImg2[self.gender]}{cell_bg[0]}',"/|\\/|\\",f"{cell_bg[4]}|  |{cell_bg[4]}",color,color]
            
    def get_details(self):
        """Returns the details of the penguin (name,age...)"""
        return f'{self.name.title()} ({self.gender}/{self.age})'
        
    def get_info(self):
        """Returns the two lines info of the penguin (name,age...)"""
        if self.alive or self.deadAge < 6:
            tempColor = COLOR_SPOT_GOOD
            tempText = "T++"
            if self.temp > 80:
                tempColor = COLOR_SPOT_CRITIC
                tempText = "T--"
            elif self.temp > 60:
                tempColor = COLOR_SPOT_BAD 
                tempText = "T- " 
            elif self.temp > 40:
                tempColor = COLOR_SPOT_MID 
                tempText = "T+-" 
            elif self.temp > 20:
                tempColor = COLOR_SPOT_OK 
                tempText = "T+ " 
            hungerColor = COLOR_SPOT_GOOD
            hungerText = "H++"
            if self.hunger > 80:
                hungerColor = COLOR_SPOT_CRITIC
                hungerText = "H--"
            elif self.hunger > 60:
                hungerColor = COLOR_SPOT_BAD
                hungerText = "H- "  
            elif self.hunger > 40:
                hungerColor = COLOR_SPOT_MID
                hungerText = "H+-"  
            elif self.hunger > 20:
                hungerColor = COLOR_SPOT_OK
                hungerText = "H+ "  
            carries = "   "
            if self.hasFish and self.hasGem:
                carries = " ^~"
            elif self.hasFish:
                carries = " ~ "
            elif self.hasGem:
                carries = " ^ "
        
            if self.alive:
                return [f'{convert_to_alpha(self.id)}:{self.name.title()} {activity_names[self.activity]}                    ',f'  {self.gender}/{int(self.age)}/{figures[self.figure]}   '[0:11],tempText,hungerText,carries,tempColor, hungerColor]     
            else:
                return [f'{convert_to_alpha(self.id)}:{self.name.title()} - Dead                  ',f'  {self.gender}/{int(self.age)}/{figures[self.figure]}   '[0:11],tempText,hungerText,carries,COLOR_TEXT, COLOR_TEXT]     
        else:
            return ["","","","","",""]  

    def get_data(self):
        return {
            'key' : self.key,
            'vpos' : self.vpos,
            'hpos' : self.hpos,
            'id' : self.id,
            'alive' : self.alive,
            'age' : self.age,
            'deadAge' : self.deadAge,
            'hunger' : self.hunger,
            'temp' : self.temp,
            'figure' : self.figure,
            'gender' : self.gender,
            'name' : self.name.title(),
            'activity' : self.activity,
            'activityTime' : self.activity_time,
            'activityTarget' : self.activity_target,
            'activityDirection' : self.activity_direction,
            'activityText' : self.activity_text,
            'goal' : self.goal,
            'canMove' : self.canMove,
            'canFish' : self.canFish, 
            'canGrab' : self.canGrab,
            'canBuild' : self.canBuild,
            'canLove' : self.canLove,
            'hasFish' : self.hasFish,
            'hasGem' : self.hasGem            
        }

           # self.commands = []
 

