import random
from json import JSONEncoder
from util import *

genders=("M","F")
asciiEyes = ("**","oo","öö","ōō","øø","ôô","òó","óò","@@")
asciiImg1 = {"M":"[","F":"("}
asciiImg2 = {"M":"]","F":")"}
activities = {ACTIVITY_NONE:"",ACTIVITY_EATING:"Eating",ACTIVITY_FISHING:"Fishing",ACTIVITY_LOVING:"Loving",ACTIVITY_DIGING:"Diging",ACTIVITY_BUILDING:"Build"}
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
        self.orders = []
        self.hasFish = False
        self.hasGem = False

    def become_older(self,cells,size,penguins,newpenguins,weather):
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
            if len(self.orders) > 0:
                dir = get_direction(self.vpos,self.hpos,self.orders[0])
                coord = dir[0]*100 + dir[1]
                if dir[0] > 0 and dir[0] < size and dir[1] > 0 and dir[1] < size and not penguins.get(coord) and not newpenguins.get(coord):
                    self.vpos = dir[0]
                    self.hpos = dir[1]
            elif cells[self.vpos][self.hpos].cellType < 3 :
                dir = random_direction(self.vpos,self.hpos)
                coord = dir[0]*100 + dir[1]
                if dir[0] > 0 and dir[0] < size and dir[1] > 0 and dir[1] < size and cells[dir[0]][dir[1]].cellType > cells[self.vpos][self.hpos].cellType and not penguins.get(coord) and not newpenguins.get(coord):
                    self.vpos = dir[0]
                    self.hpos = dir[1]
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
            return [asciiImg1[self.gender] + asciiEyes[self.id] + asciiImg2[self.gender],f"±\\/{convert_to_alpha(self.id)}",color,color]
        elif self.deadAge < 6:
            return ["(xx)",f" \\/{convert_to_alpha(self.id)}",15,15]
            
    def get_details(self):
        """Returns the details of the penguin (name,age...)"""

        return f'{self.name.title()} ({self.gender}/{self.age})'
        
    def get_info(self):
        """Returns the two lines info of the penguin (name,age...)"""
        if self.alive or self.deadAge < 6:
            tempColor = COLOR_SPOT_GOOD
            tempText = "++"
            if self.temp > 80:
                tempColor = COLOR_SPOT_CRITIC
                tempText = "--"
            elif self.temp > 60:
                tempColor = COLOR_SPOT_BAD 
                tempText = "- " 
            elif self.temp > 40:
                tempColor = COLOR_SPOT_MID 
                tempText = "+-" 
            elif self.temp > 20:
                tempColor = COLOR_SPOT_OK 
                tempText = "+ " 
            hungerColor = COLOR_SPOT_GOOD
            hungerText = "++"
            if self.hunger > 80:
                hungerColor = COLOR_SPOT_CRITIC
                hungerText = "--"
            elif self.hunger > 60:
                hungerColor = COLOR_SPOT_BAD
                hungerText = "- "  
            elif self.hunger > 40:
                hungerColor = COLOR_SPOT_MID
                hungerText = "+-"  
            elif self.hunger > 20:
                hungerColor = COLOR_SPOT_OK
                hungerText = "+ "  

            if self.alive:
                return [f'{convert_to_alpha(self.id)}:{self.name.title()} {activities[self.activity]}                    ',f'  {self.gender}/{int(self.age)}/{figures[self.figure]}   '[0:11],f'{tempText}',f'{hungerText}',tempColor, hungerColor]     
            else:
                return [f'{convert_to_alpha(self.id)}:{self.name.title()} - Dead                  ',f'  {self.gender}/{int(self.age)}/{figures[self.figure]}   '[0:11],f'{tempText}',f'{hungerText}',tempColor, hungerColor]     
        else:
            return ["","","","","",""]  

class PenguinEncoder(JSONEncoder):
    def default(self,object):
        if isinstance(object,Penguin):
            return object.__dict__
        else:
            return json.JSONEncoder.default(self,object)