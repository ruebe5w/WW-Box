# from wwbox.game import Game
from wwbox.tools import *
from wwbox.web import WebThread
from wwbox.web import instance_dict

t = WebThread()
t.start()
for player_key in instance_dict:
    set_gui(player_key, 'info', txt1={'text': 'Hallo ich bin eine autonome Abstimmung.'}, imgPicture='Rückseite.png')
