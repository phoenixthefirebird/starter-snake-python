import os
import random

import cherrypy
import json
from algorithm import *

"""
This is a simple Battlesnake server written in Python.
For instructions see https://github.com/BattlesnakeOfficial/starter-snake-python/README.md
"""
#these are the global variables
width = 0
height = 0
headx = 0
heady = 0

class Battlesnake(object):



    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        # This function is called when you register your Battlesnake on play.battlesnake.com
        # It controls your Battlesnake appearance and author permissions.
        # TIP: If you open your Battlesnake URL in browser you should see this data
        return {
            "apiversion": "1",
            "author": "",  # TODO: Your Battlesnake Username
            "color": "#e60000",
            "head": "shac-tiger-king",
            "tail": "shac-weight",
        }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        # This function is called everytime your snake is entered into a game.
        # cherrypy.request.json contains information about the game that's about to be played.
        set(cherrypy.request.json)

        print("START")
        return "ok"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):

        # This function is called on every turn of a game. It's how your snake decides where to move.
        # Valid moves are "up", "down", "left", or "right".
        # TODO: Use the information in cherrypy.request.json to decide your next move, this gives us a dictionary
        data = cherrypy.request.json
        save(data)
        move = ["up", "down", "left", "right"]
        move = reverse(data)
        move = border(data,move)
        move = myself(data,move)
        move = food(data,move)
        next = random.choice(move)



        # Choose a random direction to move in
        shouts = ["Impossible Enermy", "That looks delicious", "Hmmm I am hungry", "Grrrrr", "Do I need to know recursion?", "Getting big!"]
        shout = random.choice(shouts)

        print("MOVE:" + next)
        return {"move": next,"shout" : shout}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        # This function is called when a game your snake was in ends.
        # It's purely for informational purposes, you don't have to make any decisions here.
        data = cherrypy.request.json

        print("END")
        return "ok"





if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)
