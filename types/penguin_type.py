from dataclasses import dataclass

@dataclass
class Penguin:
    """Class for keeping track of a penguin """
    key: int
    id: int
    age: int
    dead_age : int
    hunger: int = 0
    temp: int = 0
    figure: int
    vpos: int 
    hpos: int        
    gender: int
    name: str
    activity: int
    activity_time: int
    activity_direction: int
    activity_text: str
    activity_done: bool
    goal: int
    commands: list[str]
    hasFish: bool = False 
    hasGem: bool = False
    inLove: bool = False


    # self.key = get_next_key()
    #     self.id = id
    #     self.alive = True
    #     self.age = random.randint(1,3)
    #     self.deadAge = 0
    #     self.hunger = 0
    #     self.temp = 0
    #     self.figure = random.randint(0,2)
    #     self.vpos=vpos
    #     self.hpos=hpos
    #     self.gender = genders[random.randint(0,1)]
    #     self.name = generate_penguin_name(self.gender)
    #     self.activity = ACTIVITY_NONE
    #     self.activity_time = 0
    #     self.activity_direction = 0
    #     self.activity_target = 0
    #     self.activity_text = ""
    #     self.goal = 0
    #     self.commands = []
    #     self.hasFish = False
    #     self.hasGem = False
    #     self.inLove = False
    #     self.activity_done = False