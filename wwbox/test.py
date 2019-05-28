from wwbox.game import Game
from wwbox.tools import *
from wwbox.web import WebThread
from wwbox.web import instance_dict
import time

web_thread = WebThread()
web_thread.start()
old_instance_dict = {}
gamestatus_dict = {'status': 0}
game = Game()
while gamestatus_dict['status'] == 0:
    if old_instance_dict != instance_dict:
        for player in instance_dict.keys():
            if player not in game.players:
                game.new_player()
for i in range(1, 30):
    try:
        for player_key in instance_dict:
            set_gui(player=player_key, base='info', txt1={'text': 'Hallo ich bin eine autonome Abstimmung.'},
                    imgPicture='Rückseite.png')
    except:
        print('_____________________________________________________________________')
    time.sleep(2)
