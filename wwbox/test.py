from wwbox.game import *
from wwbox.web import WebThread, instance_dict

web_thread = WebThread()
web_thread.start()
old_instance_dict = {}

game = Game()
while gamestatus_dict['status'] == 0:
    if old_instance_dict != instance_dict:
        for player_key in instance_dict.keys():
            if player_key not in game.players:
                game.new_player(instance_dict[player_key]['name'], player_key)
if gamestatus_dict['status'] == 1:
    game.start(gamestatus_dict['scenario'])
