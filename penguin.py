import random
from json import JSONEncoder
from util import *

genders=("M","F")
asciiEyes = ("**","11","22","33","44","55","66","77","88")
asciiImg1 = {"M":"[","F":"("}
asciiImg2 = {"M":"]","F":")"}
activities = {ACTIVITY_NONE:"",ACTIVITY_EATING:"Eating",ACTIVITY_FISHING:"Fishing",ACTIVITY_LOVING:"Loving",ACTIVITY_GETING:"Diging",ACTIVITY_BUILDING:"Build",ACTIVITY_MOVING:"Move"}
activities_ascii = {ACTIVITY_NONE: "\\/",ACTIVITY_EATING: "<>", ACTIVITY_FISHING: "/|", ACTIVITY_LOVING: "<3", ACTIVITY_GETING: "-^",ACTIVITY_BUILDING : "-#", ACTIVITY_MOVING:"\\/"}
figures = {0:"Slim", 1:"Fit", 2:"Fat"}


class Penguin:
    
    def __init__(self,id,vpos,hpos):
        """Initiate a penguin with it's id and his position"""
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
        self.activityTime = 0
        self.activityTarget = 0
        self.orders = []
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
                append_event_to_log(f'{self.name.title()} died (age)')
                return
            elif self.temp > 99:
                self.alive = False
                append_event_to_log(f'{self.name.title()} died (cold)')
                return
            elif self.hunger > 99:
                self.alive = False
                append_event_to_log(f'{self.name.title()} died (hunger)')    
                return
            elif cells[self.vpos][self.hpos].cellType == 0:
                self.alive = False
                append_event_to_log(f'{self.name.title()} died (sunk)')
                return

            # Is there an order to execute
            if self.activityTime > 0:
                self.activityTime -= 1
                if self.activityTime == 0:
                    if self.activity == ACTIVITY_FISHING:
                        self.hasFish = True
                        self.activity = ACTIVITY_NONE
                        fishes[self.acivityTarget].isDead = True
                    elif self.activity == ACTIVITY_GETING:
                        self.hasGem = True
                        self.activity = ACTIVITY_NONE
                        gems[self.acivityTarget].isTaken = True
            elif len(self.orders) > 0:
                activity = get_activity(self.orders)
                if activity == ACTIVITY_MOVING:
                    direction = get_direction(self.vpos,self.hpos,self.orders[0],f"{self.id} move")
                    coord = direction['vpos']*100 + direction['hpos']
                    if direction['vpos'] > 0 and direction['vpos'] < size and direction['hpos'] > 0 and direction['hpos'] < size and not penguins.get(coord) and not newpenguins.get(coord):
                        self.vpos = direction['vpos']
                        self.hpos = direction['hpos']
                elif activity == ACTIVITY_FISHING:
                    direction = get_direction(self.vpos,self.hpos,self.orders[1],f"{self.id} fish")
                    coord = direction['vpos']*100 + direction['hpos']
                    if fishes.get(coord):
                        fishes[coord].onHook=True
                        self.activityTime = 3
                        self.activity = activity
                        self.acivityTarget = coord
                elif activity == ACTIVITY_GETING:
                    direction = get_direction(self.vpos,self.hpos,self.orders[1],f"{self.id} dig")
                    coord = direction['vpos']*100 + direction['hpos']
                    if gems.get(coord):
                        self.activityTime = 3  
                        self.activity = activity      
                        self.acivityTarget = coord
                self.orders = []
            # if not and if the penguin is on smelting ice: try to escape
            elif cells[self.vpos][self.hpos].cellType < 3 :
                direction = random_direction(self.vpos,self.hpos)
                coord = direction['vpos']*100 + direction['hpos']
                if direction['vpos'] > 0 and direction['vpos'] < size and direction['hpos'] > 0 and direction['hpos'] < size and cells[direction['vpos']][direction['hpos']].cellType > cells[self.vpos][self.hpos].cellType and not penguins.get(coord) and not newpenguins.get(coord):
                    self.vpos = direction['vpos']
                    self.hpos = direction['hpos']
        else :
            self.deadAge += 1

    def receive_order(self,orders) :
        """Receives an order to move or perform an activity"""
        for order in orders:
            self.orders.append(order)
     
    def get_ascii(self):
        """Returns the ascii image of the penguin """
        color = COLOR_PENGUIN_OK
        if self.temp > 70 or self.hunger > 70:
            color = COLOR_PENGUIN_CRITIC
        elif self.temp > 50 or self.hunger > 50:
            color = COLOR_PENGUIN_BAD
        if self.alive:
            return [asciiImg1[self.gender] + asciiEyes[self.id] + asciiImg2[self.gender],f" {activities_ascii[self.activity]} ",color,color]
        elif self.deadAge < 6:
            return ["(xx)",f" \\/ ",15,15]
            
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
                return [f'{convert_to_alpha(self.id)}:{self.name.title()} {activities[self.activity]}                    ',f'  {self.gender}/{int(self.age)}/{figures[self.figure]}   '[0:11],tempText,hungerText,carries,tempColor, hungerColor]     
            else:
                return [f'{convert_to_alpha(self.id)}:{self.name.title()} - Dead                  ',f'  {self.gender}/{int(self.age)}/{figures[self.figure]}   '[0:11],tempText,hungerText,carries,COLOR_TEXT, COLOR_TEXT]     
        else:
            return ["","","","","",""]  

class PenguinEncoder(JSONEncoder):
    def default(self,object):
        if isinstance(object,Penguin):
            return object.__dict__
        else:
            return json.JSONEncoder.default(self,object)