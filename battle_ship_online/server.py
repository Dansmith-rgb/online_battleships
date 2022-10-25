import datetime
import socket
from _thread import *

from numpy import square
from board import Game_data
import pickle
import json
import ast

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "192.168.1.230"
port = 5555

# trying to set up socket to listen for incoming connectins.
try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

# Starting to listen for connectins.
s.listen()
print("[START] Waiting for a connection")

connections = 0

games = {0: Game_data()}

spectartor_ids = []
specs = 0


def read_specs():
    """
    Checks to see if specs.txt exists and creates a new one
    if there isn't one
    """
    global spectartor_ids

    spectartor_ids = []
    try:
        with open("specs.txt", "r") as f:
            for line in f:
                spectartor_ids.append(line.strip())
    except:
        print("[ERROR] No specs.txt file found, creating one...")
        open("specs.txt", "w")


def threaded_client(conn, game, spec=False):
    """
    This is where the server recieves information about the game
    and relays to everyone in that game

    :param conn: allows the server to send and recieve data 
    on that connection
    :type conn: socket object
    :param game: Tells server what game somebody is in
    :type game: int
    :param spec: if true you are a spectator, defaults to False
    :type spec: bool, optional
    """
    global pos, games, currentId, specs, connections

    if not spec:
        name = None
        gd = games[game]

        if connections % 2 == 0:
            currentId = "1"
        else:
            currentId = "2"

        gd.start_user = currentId

        # Pickle the object and send it to the server
        data_string = pickle.dumps(gd)
        # If r(second player of the game) has joined then make the
        # game ready
        if currentId == "2":
            gd.ready = True
        conn.send(data_string)
        connections += 1

        # Start while loop
        while True:
            if game not in games:
                break

            try:
                # If server doesn't recieve any data break from loop
                d = conn.recv(8192 * 3)
                data = d.decode("utf-8")
                if not d:
                    break
                else:
                    #print(data)
                    if data.count("update") > 0:
                        all = data.split(" ")
                        name = all[1]
                        sqaure_number = all[2]
                        
                        player = all[3]
                        if player == "1":
                            
                            gd.board[sqaure_number][1] = name
                        else:
                            
                            gd.board_2[sqaure_number][1] = name

                        #square_info = all[1]
                    # If the data has select and space and all the
                    # other variables then it will go inside the if statement
                    if data.count("guess") > 0:
                        # It splits up the data it has been sent
                        all = data.split(" ")
                        sqaure_number = all[1]
                        player = all[2]
                        if player == "1": 
                            gd.check_guesses(gd.board_2, sqaure_number)

                        else:
                            gd.check_guesses(gd.board, sqaure_number)
                        # It then changes who's turn it is
                        if gd.turn == "1":
                            gd.turn = "2"
                            gd.reset1 = True
                            gd.reset2 = True
                        else:
                            gd.turn = "1"
                            gd.reset1 = True
                            gd.reset2 = True

                    if data == "reset1":
                        gd.reset1 = False
                    
                    if data =="reset2":
                        gd.reset2 = False

                    if data == "player 1 ready":
                        gd.p1_ready = True

                    if data == "player 2 ready":
                        gd.p2_ready = True
                    # If the data has winner y in it then set the board winner to y
                    if data == "winner 1":
                        gd.winner = "1"
                        print(f"[GAME] Player {gd.p1Name} won in game {game}")
                    # If the data has winner r in it then set the board winner to r
                    if data == "winner r":
                        gd.winner = "2"
                        print(f"[GAME] Player {gd.p2Name} won in game {game}")

                    # If data has name and something after then check
                    # currentId and set players name
                    if data.count("name") == 1:

                        name = data.split(" ")[1]

                        if currentId == "2":
                            gd.p2Name = name
                        elif currentId == "1":
                            gd.p1Name = name

                    # Package all data up to send to players
                    sendData = pickle.dumps(gd)

                # Send all data to player
                conn.sendall(sendData)

            except Exception as e:
                print(e)

        connections -= 1
        try:
            del games[game]
            print("[GAME] Game", game, "ended")
        except:
            pass
        print("[DISCONNECT] Player", name, "left game", game)
        # Close connection
        conn.close()


# Start loop to get game or create new game and call main function
while True:
    if connections < 6:
        conn, addr = s.accept()
        spec = False
        g = -1
        print("[CONNECT] New connection")

        for game in games.keys():
            if games[game].ready == False:
                g = game

        if g == -1:
            try:
                g = list(games.keys())[-1] + 1
                games[g] = Game_data()
            except:
                g = 0
                games[g] = Game_data()

        print("[DATA] Number of Connections:", connections + 1)
        print("[DATA] Number of Games:", len(games))

        start_new_thread(threaded_client, (conn, g, spec))

