from datetime import datetime

class Context:

    def __init__(self):
        """Initiate an island instance"""
        self.islands = {}

    def get_islands(self) :
        return self.islands

    def create_island(self,island) :
        self.islands[island.id] = island
        return island

    def create_island_list(self) :
        """Creates a list of islands with name, id and running attributes"""
        islandList = []

        for island in self.islands.values() :
            if island.game_ongoing or (datetime.now() - island.game_end_datetime).total_seconds() <60:
                islandList.append({'name':island.name, 'id':island.id, 'running': island.game_ongoing, 'size' : island.size})

        return islandList

    def maintain_island_list(self) :
        """Maintains the of islands, notably supressing the ended games"""
        
        tmpIslands = {}
        for island in self.islands.values() :
            if island.game_ongoing or (datetime.now() - island.game_end_datetime).total_seconds() <60:
                tmpIslands[island.id] = island
            else:
                print(f'#### Supressing {island.id} from the list (age : {(datetime.now() - island.game_end_datetime).total_seconds()} seconds')
        self.islands = tmpIslands
