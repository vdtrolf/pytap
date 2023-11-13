from flask import Flask, redirect, url_for, request, jsonify

from island import *
from util import *

Flaskapp = Flask(__name__)
islands = {}
initiate_names()

    
@Flaskapp.route('/refresh/<islandId>')
def refresh(islandId):

    islandList = []
    for island in islands.values() :
        islandList.append({'name':island.name, 'id':island.id, 'running': island.game_ongoing, 'size' : island.size})

    if islands.get(int(islandId)) :
        island = islands[int(islandId)]
        island.become_older()
        response = jsonify(island.get_data(islandList))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        return "{unknown island}"


@Flaskapp.route('/command/<islandId>',methods = ['POST', 'GET'])
def command(islandId):
    if islands.get(int(islandId)) :
        island = islands[int(islandId)]

        islandList = []
        for island in islands.values() :
            islandList.append({'name':island.name, 'id':island.id, 'running': island.game_ongoing, 'poimts' : island.size})

        if request.method == 'POST':
            penguin_id = request.form['penguinId']
            command1 = request.form['command1']
            command2 = request.form['command2']
            island.transmit_commands(int(penguin_id), [command1,command2])      

            response = jsonify({"done":"ok"})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

            # return redirect(url_for('refresh',islandid = islandid))
        else:
            penguin_id = request.args.get('penguinId')
            command1 = request.args.get('command1')
            command2 = request.args.get('command2')      
            island.transmit_commands(int(penguin_id), [command1,command2])                  
            island.execute_commands()
            response = jsonify(island.get_data(islandList))
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

            # return redirect(url_for('refresh',islandid = islandid))
    else:
        return "{unknown island}"
        
@Flaskapp.route('/create')
def create():

    islandList = []
    for island in islands.values() :
        islandList.append({'name':island.name, 'id':island.id, 'running': island.game_ongoing, 'size' : island.size})

    size  = request.args.get('size')
    if not (size is None) and int(size) in BOARDSIZES :
        print(f'Size is {size}')
        island = Island(int(size))
    else :
        print('no size or unknown size')
        island = Island(BOARDSIZE)

    islands[island.id] = island
    response = jsonify(island.get_data(islandList))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@Flaskapp.route('/islands')
def island():
    islandList = []
    for island in islands.values() :
        islandList.append({'name':island.name, 'id':island.id, 'running': island.game_ongoing, 'size' : island.size})
    response = jsonify({'islands':islandList})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

  
if __name__ == '__main__':
    Flaskapp.run(use_reloader=False, debug=True)

