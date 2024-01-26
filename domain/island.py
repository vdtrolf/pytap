import random
from datetime import datetime

from domain.penguin import *
from domain.cell import *
from domain.fish import *
from domain.garbage import *
from domain.gem import *
from utilities.util import *
from interpreter import *

islands = {}

class Island :
  
    def build_island(self,size):
        """build islands in the world"""
        tmpland = []
        for i in range(size) :
            lane =[]
            for j in range(size):
                 lane.append(0)
            tmpland.append(lane)
        
        # add some mountains     
        for i in range(int(size / 3)):
            v = 1 + random.randint(0,size-3)
            h = 1 + random.randint(0,size-3)
            tmpland[v][h] = 15
       
        # add some land around the mountains 
        for i in range(4) :
            for j in range(int(size * i)):
                v = 1 + random.randint(0,size-3)
                h = 1 + random.randint(0,size-3)
                if tmpland[v][h] == 0 and (tmpland[v][h+1] > 0 or tmpland[v][h-1] > 0 or tmpland[v+1][h] > 0 or tmpland[v-1][h] > 0 ) :
                     tmpland[v][h] = 15-i*3
                
        # remove the lakes and the istmes        
        for i in range(size -2):
            for j in range(size -2):
                v=i+1
                h=j+1
                if tmpland[v][h] == 0 :
                    cnt = 0
                    if tmpland[v][h+1] > 0 :
                        cnt += 1
                    if tmpland[v][h-1] > 0 :
                        cnt += 1
                    if tmpland[v+1][h] > 0 :
                        cnt += 1
                    if tmpland[v-1][h] > 0:
                        cnt += 1
                    if cnt > 2 :
                        tmpland[v][h] = 1
            
        for i in range(size):   
            tmplane = []
            for j in range(size):
                tmplane.append(Cell(i,j,tmpland[i][j]))
            self.cells.append(tmplane)
                
        # add some penguins
        cntpenguins=0
        while cntpenguins < size / 2 :
            v = random.randint(1,size-2)
            h = random.randint(1,size-2)
            if self.cells[v][h].isGround() and not self.penguins.get(v*100+h):
                self.penguins[v*100+h]=Penguin(cntpenguins + 1,v,h)
                cntpenguins +=1

        # add some garbage
        cntgarbages=0
        while cntgarbages < size / 4 :
            v = random.randint(0,size-1)
            h = random.randint(0,size-1)
            if self.cells[v][h].isSea() and (v == 0 or v == size-1 or h==0 or h == size-1):
                self.garbages[v*100+h]=Garbage(v,h)
                cntgarbages +=1
                
        # add some fishes
        cntfishes=0
        while cntfishes < size / 2 :
            v = random.randint(0,size-1)
            h = random.randint(0,size-1)
            if self.cells[v][h].isSea():
                self.fishes[v*100+h]=Fish(v,h)
                cntfishes +=1
                
    def __init__(self,size):
        """Initiate an island instance"""
        self.key = get_next_key()
        self.id = random.randint(0,99999)
        self.size = size
        self.name = generate_island_name()
        self.cells = []
        self.penguins = {}
        self.fishes = {}
        self.gems = {}
        self.garbages = {}
        self.counter = 0
        self.build_island(size)   
        weather = random_weather(0,0,True)    
        self.weather = weather[0]
        self.weather_age = weather[1]
        self.weather_name = weather[2]
        self.year = 2000
        self.evolution_speed = 1
        self.game_ongoing = True
        self.game_end_datetime = None

    def cleanGems(self):
        """ gems become_older, notably to make them smelt over time """
        tmpgems = {}
        for gem in self.gems.values():
            gem.become_older(self.cells)
            if gem.age > 0 and not gem.isTaken:
                tmpgems[gem.vpos*100+gem.hpos]=gem
        self.gems = tmpgems

    def cleanFishes(self):
        """ fishes become_older, notably to make them move """
        tmpfishes = {}
        for fish in self.fishes.values():
            fish.become_older(self.cells,self.garbages,self.size)
            if not fish.isDead:
                tmpfishes[fish.vpos*100+fish.hpos]=fish
        self.fishes = tmpfishes

    def cleanGarbages(self):
        """ garabge become_older, notably to make some of them change shape """
        tmpgarbages = {}
        for garbage in self.garbages.values():
            garbage.become_older()
            if not garbage.isTaken:
                tmpgarbages[garbage.vpos*100+garbage.hpos]=garbage
        self.garbages = tmpgarbages

        
    def become_older(self,force=False):
        """
        Makes the island, penguins and artifacts older
        The speed of the evolution raises according to the variable 'counter'        
        """

        if self.game_ongoing :

            self.counter += 1
            self.evolution_speed = int(self.counter/40) + 1
            if self.evolution_speed > 5:
                self.evolution_speed = 5

            self.year += 0.05
            
            weather = random_weather(self.year,self.weather,self.weather_age)    
            self.weather = weather[0]
            self.weather_age = weather[1]
            self.weather_name = weather[2]    

            # cells become_older, notably to make them smelt over time
            for v in range(1,self.size -1):
                for h in range(1, self.size -1):
                    self.cells[v][h].become_older(self.cells,self.size,self.weather,self.evolution_speed)       

            # penguins become_older, notably to make them older, execute commands and get childs
            tmppenguins = {}
            childCounter = len(self.penguins) + 1
            for penguin in self.penguins.values():
                hasChild = penguin.become_older(self.cells,self.size,self.penguins,tmppenguins,self.fishes,self.gems,self.garbages,self.weather,self.evolution_speed,force)
                if penguin.alive or penguin.deadAge < 6:
                    tmppenguins[penguin.vpos*100+penguin.hpos]=penguin
                if hasChild: 
                    counter = 0
                    while counter < 10:
                        v = random.randint(1,self.size-2)
                        h = random.randint(1,self.size-2)
                        if self.cells[v][h].isGround() and not self.penguins.get(v*100+h) and not self.gems.get(v*100+h):
                            tmppenguins[v*100+h]=Penguin(childCounter,v,h)
                            childCounter += 1
                            break
                        counter += 1    

            self.penguins = tmppenguins

            self.cleanFishes()

            # add some fishes
            cntfishes=len(self.fishes)
            try_counter = 0
            while cntfishes < self.size / 2 and try_counter < 20:
                v = random.randint(0,self.size-1)
                h = random.randint(0,self.size-1)
                if self.cells[v][h].isSea() and not self.fishes.get(v*100+h) and not self.garbages.get(v*100+h):
                    self.fishes[v*100+h]=Fish(v,h)
                    cntfishes +=1
                try_counter += 1
                    
            self.cleanGems()
            self.cleanGarbages()

            # add some extra garbage - must be next another garbage
            # gets more chances to happen if the evolution speed raises
            if self.evolution_speed > 1:
                for i in range(self.evolution_speed - 1) :
                    v = random.randint(0,self.size-1)
                    h = random.randint(0,self.size-1)
                    if self.cells[v][h].isSea() and not self.fishes.get(v*100+h) and (self.garbages.get((v+1)*100+h) or self.garbages.get((v-1)*100+h) or self.garbages.get(v*100+h+1) or self.garbages.get(v*100+h-1)):
                        self.garbages[v*100+h]=Garbage(v,h)
                        
            # quick check to see if any alive penguins -> if not then the game is over
            self.game_ongoing = False
            for penguin in self.penguins.values():
                if penguin.alive : 
                    self.game_ongoing = True
                    break        

            if not self.game_ongoing and self.game_end_datetime == None:
                self.game_end_datetime = datetime.now()
                print(f'##### ENDGAME AT {self.game_end_datetime} #####')    

            if len(self.gems) < self.size:
                v = random.randint(0,self.size-1)
                h = random.randint(0,self.size-1)
                hasShowel = random.randint(0,10) > 8
                if self.cells[v][h].isIce() and not self.penguins.get(v*100+h) and not self.gems.get(v*100+h):
                    self.gems[v*100+h]=Gem(v,h,hasShowel)

    def execute_commands(self) :
        for penguin in self.penguins.values():
            penguin.execute_commands(self.cells,self.size,self.penguins,self.penguins,self.fishes,self.gems,self.garbages)
        
        # penguins become_older, notably to make them older, execute commands and get childs
        tmppenguins = {}
        for penguin in self.penguins.values():
            if penguin.alive or penguin.deadAge < 6:
                tmppenguins[penguin.vpos*100+penguin.hpos]=penguin
        self.penguins = tmppenguins;

    def transmit_commands(self,penguin_id,commands) :
        """Search a penguin by id and return the two lines info"""
        for penguin in self.penguins.values():
            if penguin.id == penguin_id or penguin.key == penguin_id:
                penguin.receive_commands(commands)
                command = interpret_commands(commands,0,0,self.cells,self.fishes,self.gems,self.garbages)
                # print(command)
                append_event_to_log(f"{penguin.name.title()}: {command['activityName']} {command['directionName']}")    
                
    def get_data(self,islandList):
        
        penguinsData = []
        for penguin in self.penguins.values():
            penguinsData.append(penguin.get_data())

        fishesData = []
        for fish in self.fishes.values():
            fishesData.append(fish.get_data())
            
        gemsData = []
        for gem in self.gems.values():
            gemsData.append(gem.get_data())

        garbagesData = []
        for garbage in self.garbages.values():
            garbagesData.append(garbage.get_data())

        cellsData = []
        for vpos in range(self.size):
            for hpos in range(self.size):
                cellsData.append(self.cells[vpos][hpos].get_data())
                        
        islandData = {
            'key' : self.key,
            'id' : self.id,
            'size': self.size,
            'name' : self.name,
            'counter' : self.counter,
            'weather' : self.weather,
            'year' : self.year,
            'evolutionSpeed' : self.evolution_speed,
            'onGoing' : self.game_ongoing,
            'penguins' : penguinsData,
            'fishes' : fishesData,
            'gems' : gemsData,
            'garbages' : garbagesData,
            'cells' : cellsData,
            'islands' : islandList
        }
        return islandData

