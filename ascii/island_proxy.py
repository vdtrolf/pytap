from .penguin_renderer import *
from .cell_renderer import *
from .fish_renderer import *
from .garbage_renderer import *
from .gem_renderer import *
from utilities.util import *

class Island_proxy :

    def __init__(self,island):
        """Initiate an island proxy with it's island instance"""
        self.island = island

    def get_cell_bg(self,vpos,hpos):
        """get the cell color scheme"""
        return get_cell_bg(self.island.cells[vpos][hpos])

    def get_cell_ascii(self,vpos,hpos):
        """get the ascii value at a given position"""
        cell_bg = get_cell_bg(self.island.cells[vpos][hpos]) 
        if self.island.penguins.get(vpos*100+hpos) :
            return get_penguin_ascii(self.island.penguins[vpos*100+hpos],cell_bg)
        elif self.island.fishes.get(vpos*100+hpos) :
            return get_fish_ascii(self.island.fishes[vpos*100+hpos])
        elif self.island.garbages.get(vpos*100+hpos) :
            return get_garbage_ascii(self.island.garbages[vpos*100+hpos])
        elif self.island.gems.get(vpos*100+hpos) :
            return get_gem_ascii(self.island.gems[vpos*100+hpos],cell_bg)
        else:   
            return get_cell_ascii(self.island.cells[vpos][hpos])

    def get_info(self):
        """Returns the name and status of the island"""
        return f'{self.island.name} - run {int(self.island.year)} - {self.island.weather_name} - speed: {self.island.evolution_speed}                                               '
        
    def get_penguin_info(self,penguin_id):
        """Search a penguin by id and return the two lines info"""
        result = ['','']
        for penguin in self.island.penguins.values():
            if penguin.id == penguin_id:
                result = get_penguin_info(penguin)   
        return result
   
    def show_penguin_details(self,penguin_id):
        """Search a penguin by id and return it's details"""
        for penguin in self.island.penguins.values():
            if penguin.id == penguin_id:
                print(get_penguin_details(penguin))
                

