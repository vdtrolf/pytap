from flask import Flask, redirect, url_for,  request, jsonify
from datetime import datetime

from domain.island import *
from utilities.util import *
from context import *


context = Context()
initiate_names()

Flaskapp = Flask(__name__)

    
@Flaskapp.route('/refresh/<islandId>')
def refresh(islandId):
    """ """

    context.maintain_island_list()
    islands = context.get_islands()
    
    # print (f"%%% 1 {islands}")

    islandList = context.create_island_list()
    response = '{}'
    
    if islands and islands.get(int(islandId)) :
        island = islands[int(islandId)]
        island.become_older()
        response = jsonify(island.get_data(islandList))
        response.headers.add('Access-Control-Allow-Origin', '*')
        
    return response    
 

@Flaskapp.route('/command/<islandId>',methods = ['POST', 'GET'])
def command(islandId):
    """ """

    islands = context.get_islands()
    # print (f"%%% 2 {islands}")
    islandList = context.create_island_list()

    if islands and islands.get(int(islandId)) :
        island = islands[int(islandId)]

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
    """ """
    islands = context.get_islands()
    # print (f"%%% 3 {islands}")

    size  = request.args.get('size')
    if size is None or not (int(size) in BOARDSIZES) :
        size = BOARDSIZE
    
    print(f'Size is {size}')
    island = context.create_island(Island(int(size)))
    context.maintain_island_list()
    islandList = context.create_island_list()

    response = jsonify(island.get_data(islandList))
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@Flaskapp.route('/islands')
def island():
    """ """

    # print (f"%%% 4 ")
    islandList = context.create_island_list()

    response = jsonify({'islands':islandList})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    # Quick test configuration. Please use proper Flask configuration options
    # in production settings, and use a separate file or environment variables
    # to manage the secret key!

    
    Flaskapp.debug = True
    Flaskapp.run(use_reloader=False, debug=True)

    


