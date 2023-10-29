from flask import Flask, redirect, url_for, request, jsonify

from island import *
from util import *

Flaskapp = Flask(__name__)
islands = {}
initiate_names()

@Flaskapp.route('/refresh/<islandId>')
def refresh(islandId):
    if islands.get(int(islandId)) :
        island = islands[int(islandId)]
        island.become_older()
        response = jsonify(island.get_data())
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        return "{unknown island}"

@Flaskapp.route('/command/<islandId>',methods = ['POST', 'GET'])
def command(islandId):
    if islands.get(int(islandId)) :
        island = islands[int(islandId)]
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
    response = jsonify(island.get_data())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
  
if __name__ == '__main__':
    Flaskapp.run(use_reloader=False, debug=True)

