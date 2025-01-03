from dataclasses import dataclass
from cell_type import Cell
from penguin_type import Penguin
from fish_type import Fish
from gem_type import Gem
from garbage_type import Garbage
from log_type import Log


@dataclass
class Island:
    """Class for keeping track of an island"""
    key: int
    id: int 
    name: str        
    counter: int = 0
    weather: int
    weather_age: int
    weather_name: str
    year: int = 2000
    evolution_speed: int = 1
    wether: bool = False
    game_ongoing: bool = True
    game_end_datetime: int = None 
    cells: list[Cell]
    penguins: dict[int,Penguin]
    fishes: dict[int,Fish]
    gems: dict[int,Gem]
    garbages: dict[int,Garbage]
    log : Log




    # self.key = get_next_key()
    #     self.id = random.randint(0,99999)
    #     self.size = size
    #     self.name = generate_island_name()
    #     self.cells = []
    #     self.penguins = {}
    #     self.fishes = {}
    #     self.gems = {}
    #     self.garbages = {}
    #     self.counter = 0
    #     self.build_island(size)   
    #     weather = random_weather(0,0,True)    
    #     self.weather = weather[0]
    #     self.weather_age = weather[1]
    #     self.weather_name = weather[2]
    #     self.year = 2000
    #     self.evolution_speed = 1
    #     self.game_ongoing = True
    #     self.game_end_datetime = None