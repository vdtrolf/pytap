from flask import Flask, redirect, url_for, request

from island import *
from util import *

Flaskapp = Flask(__name__)
islands = {}
initiate_names()

@Flaskapp.route('/refresh/<islandid>')
def refresh(islandid):
    if islands.get(int(islandid)) :
        island = islands[int(islandid)]
        island.become_older()
        return island.get_data()
    else:
        return "{unknown island}"

@Flaskapp.route('/command/<islandid>',methods = ['POST', 'GET'])
def command(islandid):
    if islands.get(int(islandid)) :
        island = islands[int(islandid)]
        if request.method == 'POST':
            penguin_id = request.form['penguinid']
            command1 = request.form['command1']
            command2 = request.form['command2']
            island.transmit_commands(int(penguin_id), [command1,command2])      
            return redirect(url_for('refresh',islandid = islandid))
        else:
            penguin_id = request.args.get('penguinid')
            command1 = request.args.get('command1')
            command2 = request.args.get('command2')      
            island.transmit_commands(int(penguin_id), [command1,command2])                  
            return redirect(url_for('refresh',islandid = islandid))
    else:
        return "{unknown island}"
        
@Flaskapp.route('/create')
def create():
    island = Island(BOARDSIZE)
    islands[island.id] = island
    return island.get_data()
  
if __name__ == '__main__':
    Flaskapp.run(use_reloader=False, debug=True)

