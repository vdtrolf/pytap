from flask import Flask

from island import *
from util import *

Flaskapp = Flask(__name__)
boardSize = 12
initiate_names()

@Flaskapp.route('/')
def helloWorld():
    island = Island(boardSize)
    return island.get_data()
  
if __name__ == '__main__':
    Flaskapp.run(use_reloader=False, debug=True)

