import random
from json import JSONEncoder
import json

from penguin import *
from cell import *
from fish import *
from gem import *
from util import *

class Island :

    def get_cell_bg(self,vpos,hpos):
        """get the cell color scheme"""
        return self.cells[vpos][hpos].get_bg()

    def get_cell_ascii(self,vpos,hpos):
        """get the ascii value at a given position"""
        if self.penguins.get(vpos*100+hpos) :
            return self.penguins[vpos*100+hpos].get_ascii()
        elif self.fishes.get(vpos*100+hpos) :
            return self.fishes[vpos*100+hpos].get_ascii()
        elif self.gems.get(vpos*100+hpos) :
            return self.gems[vpos*100+hpos].get_ascii()
        else:   
            return self.cells[vpos][hpos].get_ascii()
      
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
            tmpland[v][h] = 12
       
        # add some land around the mountains 
        for i in range(6) :
            for j in range(size * i):
                v = 1 + random.randint(0,size-3)
                h = 1 + random.randint(0,size-3)
                if tmpland[v][h] == 0 and (tmpland[v][h+1] > 0 or tmpland[v][h-1] > 0 or tmpland[v+1][h] > 0 or tmpland[v-1][h] > 0 ) :
                     tmpland[v][h] = 12-i
                
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
                tmplane.append(Cell(tmpland[i][j]))
            self.cells.append(tmplane)
                
        # add some penguins
        cntpenguins=0
        while cntpenguins < size / 2 :
            v = random.randint(1,size-2)
            h = random.randint(1,size-2)
            if self.cells[v][h].isGround() and not self.penguins.get(v*100+h):
                self.penguins[v*100+h]=Penguin(cntpenguins + 1,v,h)
                cntpenguins +=1
                
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
        self.size = size
        self.name = generate_island_name()
        self.cells = []
        self.penguins = {}
        self.fishes = {}
        self.gems = {}
        self.counter = 0
        self.build_island(size)   
        weather = random_weather(0,0,True)    
        self.weather = weather[0]
        self.weather_age = weather[1]
        self.weather_name = weather[2]
        
    def become_older(self):
        """Makes the island and artifacts older"""
        self.counter += 1
        
        # check the surrounding for each penguin
        for peng in self.penguins.values():
            fish_dist,mount_dist = 9,9
            fish_v,fish_h,mount_v,mount_h = 0,0,0,0
            for v in range(peng.vpos-2,peng.vpos+2):
                for h in range(peng.hpos-2,peng.hpos+2):
                    if v>=0 and h>=0 and v<self.size and h<self.size and not self.penguins.get(v*100+h):
                        dist = abs(v-peng.vpos) + abs(h-peng.hpos)
                        if self.fishes.get(v*100+h) and fish_dist > dist:
                            fish_dist = dist
                            fish_v = v
                            fish_h = h
                        if self.cells[v][h].isMount() and mount_dist > dist:
                            mount_dist = dist
                            mount_v = v
                            mount_h = h

        weather = random_weather(self.weather,self.weather_age)    
        self.weather = weather[0]
        self.weather_age = weather[1]
        self.weather_name = weather[2]    

        for v in range(1,self.size -1):
            for h in range(1, self.size -1):
                self.cells[v][h].become_older(self.weather)       
        
        tmpfishes = {}
        for fish in self.fishes.values():
            fish.become_older(self.cells,self.size)
            tmpfishes[fish.vpos*100+fish.hpos]=fish
        self.fishes = tmpfishes
        		
        tmpgems = {}
        for gem in self.gems.values():
            gem.become_older(self.cells)
            if gem.age > 0:
                tmpgems[gem.vpos*100+gem.hpos]=gem
        self.gems = tmpgems

        tmppenguins = {}
        for penguin in self.penguins.values():
            penguin.become_older(self.cells,self.size,self.penguins,tmppenguins,self.fishes,self.gems,self.weather)
            if penguin.alive or penguin.deadAge < 6:
                tmppenguins[penguin.vpos*100+penguin.hpos]=penguin
        self.penguins = tmppenguins

        if len(self.gems) < self.size:
            v = random.randint(0,self.size-1)
            h = random.randint(0,self.size-1)
            if self.cells[v][h].isGround() and not self.penguins.get(v*100+h) and not self.gems.get(v*100+h):
                # append_event_to_log("new gem at " + str(v) + "/" + str(h))
                self.gems[v*100+h]=Gem(v,h)
        
        # dump_island(IslandEncoder().encode(self))

    def get_info(self):
        """Returns the name and status of the island"""
        return f'{self.name} - run {self.counter} - {self.weather_name}                                                  '
        
    def get_penguin_info(self,penguin_id):
        """Search a penguin by id and return the two lines info"""
        result = ['','']
        for penguin in self.penguins.values():
            if penguin.id == penguin_id:
                result = penguin.get_info()   
        return result

    def transmit_orders(self,penguin_id,order) :
        """Search a penguin by id and return the two lines info"""
        for penguin in self.penguins.values():
            if penguin.id == penguin_id:
                penguin.receive_order(order)
                break   
    
    def show_penguin_details(self,penguin_id):
        """Search a penguin by id and return it's details"""
        for penguin in self.penguins.values():
            if penguin.id == penguin_id:
                print(penguin.get_details())
                
                
class IslandEncoder(JSONEncoder):
    def default(self,object):
        if isinstance(object,Island):
            return object.__dict__
        else:
            return json.JSONEncoder.default(self,object)

