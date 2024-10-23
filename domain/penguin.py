import random
from utilities.util import *
from interpreter import *

genders=("M","F")

class Penguin:
    
    def __init__(self,id,vpos,hpos):
        """Initiate a penguin with it's id and his position"""
        self.key = get_next_key()
        self.id = id
        self.alive = True
        self.age = random.randint(1,3)
        self.isChild = True
        self.isOld = False
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
        self.goal = 0
        self.commands = []
        self.hasFish = False
        self.hasGem = False
        self.hasShowel = False
        self.showelCnt = 0
        self.inLove = False
        self.activity_done = False
        self.can_love = True
        self.love_time = 0

    def execute_commands(self,cells,size,penguins,newpenguins,fishes,gems,garbages):
        
        # Is there an order to execute
        if len(self.commands) > 0:
            command = interpret_commands(self.commands,self.vpos,self.hpos,cells,fishes,gems,garbages)
            print('@@@2')
            direction = {'vpos':self.vpos + command['vmove'],'hpos':self.hpos + command['hmove']}
            coord = direction['vpos']*100 + direction['hpos']
            if command['activity'] == ACTIVITY_MOVING:
                if direction['vpos'] > 0 and direction['vpos'] < size and direction['hpos'] > 0 and direction['hpos'] < size and not penguins.get(coord) and not newpenguins.get(coord):
                    self.vpos = direction['vpos']
                    self.hpos = direction['hpos']
                    self.activity = command['activity']
                    self.goal = command['activity']
                    self.activity_direction = command['directionNum']
                    self.activity_time = 1      
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
            elif command['activity'] == ACTIVITY_LOVING and not self.isChild and not self.isOld:
                if penguins.get(coord) and not penguins[coord].isChild and not penguins[coord].isOld:
                    # if penguins[coord].activity == ACTIVITY_NONE and penguins[coord].gender != self.gender and penguins[coord].age > 4 :
                    penguins[coord].activity_time = 3
                    penguins[coord].love_time = 10
                    penguins[coord].can_love = False
                    penguins[coord].activity = command['activity']
                    penguins[coord].goal = command['activity']
                    self.love_time = 10
                    self.can_love = False
                    self.inLove=True
                    self.activity_time = 3
                    self.activity = command['activity']
                    self.goal = command['activity']
                    self.acivityTarget = coord
                    self.activity_direction = command['directionNum']                       
                else:      
                    self.activity = ACTIVITY_NONE  
                    self.activity_direction = DIRECTION_NONE                        
            elif command['activity'] == ACTIVITY_GETING and not self.isChild and not self.isOld:
                if gems.get(coord):
                    self.activity_time = 3  
                    self.activity = command['activity']      
                    self.goal = command['activity']
                    self.acivityTarget = coord
                    self.activity_direction = command['directionNum']      
                else:      
                    self.activity = ACTIVITY_NONE
                    self.activity_direction = DIRECTION_NONE
            elif command['activity'] == ACTIVITY_CLEANING and not self.isChild and not self.isOld and self.hasShowel:
                if garbages.get(coord):
                    self.activity_time = 2  
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
            elif command['activity'] == ACTIVITY_BUILDING and not self.isChild and not self.isOld:
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


    def become_older(self,cells,size,penguins,newpenguins,fishes,gems,garbages,weather,evolution_speed,force):
        """
        makes the penguin move and become older
        age, temperature and hunger increase faster if the evolution_speed raises
        """
        # check if there is a neighbour
        hasNeighbour =  penguins.get((self.vpos+1)*100 + self.hpos) or penguins.get((self.vpos-1)*100 + self.hpos) or penguins.get(self.vpos*100 + self.hpos -1) or penguins.get(self.vpos*100 + self.hpos +1) 
        hasChild = False
        

        if self.activity_time > 0:
            self.activity_time -= 1
            if self.activity_time == 0:
                if self.activity == ACTIVITY_MOVING or self.activity == ACTIVITY_FLEE:
                    self.activity = ACTIVITY_NONE
                    self.activity_direction = DIRECTION_NONE
                elif self.activity == ACTIVITY_FISHING:
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
                        if gems[self.acivityTarget].hasShowel:
                            self.hasShowel = True
                            self.showelCnt = 2
                            gems[self.acivityTarget].hasShowel == False
                elif self.activity == ACTIVITY_CLEANING:
                    self.activity = ACTIVITY_NONE
                    self.activity_direction = DIRECTION_NONE
                    if garbages.get(self.acivityTarget):
                        garbages[self.acivityTarget].isTaken = True    
                    self.showelCnt -= 1
                    self.hasShowel = self.showelCnt > 0         
                elif self.activity == ACTIVITY_EATING:
                    self.hunger = 0
                    self.hasFish = False
                    self.activity = ACTIVITY_NONE
                    self.activity_direction = DIRECTION_NONE
                elif self.activity == ACTIVITY_LOVING:
                    self.temp = 0
                    self.hunger = 0
                    hasChild = self.inLove
                    self.inLove = False
                    self.activity = ACTIVITY_NONE
                    self.activity_direction = DIRECTION_NONE    
                elif self.hasGem and self.activity == ACTIVITY_BUILDING:
                    self.temp = 0
                    self.hasGem = False
                    cells[self.activityVPos][self.activityHPos].endBuilding()
                    self.activity = ACTIVITY_NONE 
                    self.activity_direction = DIRECTION_NONE  

                self.goal = ACTIVITY_NONE       
                self.activity_text = activity_names[self.activity]    

        if self.alive :
                     
            if (self.love_time > 0) :
                self.love_time -= 1
            else :
                self.can_love = True

            if self.isChild or self.isOld:
                self.age += 0.2
            else:    
                self.age += 0.05
            
            self.isChild = self.age <= 3 
            self.isOld = self.age > 13 
                            
            if not hasNeighbour :  
                self.temp += weather / (6 - evolution_speed)
            self.hunger += (self.figure + 1) / (6 - evolution_speed) 

            # Is the penguin dead ?
            if self.age > 20: 
                self.alive = False
                self.activity = ACTIVITY_DEAD
                self.activity_text = f'Died (age)'
                append_event_to_log(f'{self.name.title()} died (age)')
                return
            elif self.temp > 99:
                self.alive = False
                self.activity = ACTIVITY_DEAD
                self.activity_text = f'Died (cold)'
                append_event_to_log(f'{self.name.title()} died (cold)')
                return
            elif self.hunger > 99:
                self.alive = False
                self.activity = ACTIVITY_DEAD
                self.activity_text = f'Died (hunger)'
                append_event_to_log(f'{self.name.title()} died (hunger)')    
                return
            elif cells[self.vpos][self.hpos].cellType == 0:
                self.alive = False
                self.activity = ACTIVITY_DEAD
                self.activity_text = f'Died (sunk)'
                append_event_to_log(f'{self.name.title()} died (sunk)')
                return

            if force:
                    self.execute_commands(cells,size,penguins,newpenguins,fishes,gems,garbages)

            # if not and if the penguin is on smelting ice: try to escape
            if cells[self.vpos][self.hpos].cellType < 3 :
                direction = random_direction(self.vpos,self.hpos)
                coord = direction['vpos']*100 + direction['hpos']
                if direction['vpos'] > 0 and direction['vpos'] < size and direction['hpos'] > 0 and direction['hpos'] < size and cells[direction['vpos']][direction['hpos']].cellType > cells[self.vpos][self.hpos].cellType and not penguins.get(coord) and not newpenguins.get(coord):
                    self.vpos = direction['vpos']
                    self.hpos = direction['hpos']
                    self.activity = ACTIVITY_FLEE
                    self.goal = ACTIVITY_FLEE
                    self.activity_time = 1
                    self.activity_direction = direction['directionNum']
                    
        else :
            self.deadAge += 1
        return hasChild

    def receive_commands(self,commands) :
        """Receives an order to move or perform an activity"""
        for command in commands:
            if len(command) > 0:
                self.commands.append(command)
     
    def get_data(self):
        return {
            'key' : self.key,
            'vpos' : self.vpos,
            'hpos' : self.hpos,
            'id' : self.id,
            'alive' : self.alive,
            'age' : self.age,
            'isChild' : self.isChild,
            'isOld' : self.isOld,
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
            'activityDone' : self.activity_done,
            'goal' : self.goal,
            'hasFish' : self.hasFish,
            'hasGem' : self.hasGem,
            'hasShowel' : self.hasShowel,
            'canLove' : self.can_love            
        }
 

