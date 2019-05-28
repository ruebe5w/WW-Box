from wwbox.game import Game
from wwbox.web import WebThread
from wwbox.web import instance_dict

web_thread = WebThread()
web_thread.start()
old_instance_dict = {}
gamestatus_dict = {'status': 0, 'scenario': 'Flohs Kuenstler-WG'}
game = Game()
while gamestatus_dict['status'] == 0:
    if old_instance_dict != instance_dict:
        for player_key in instance_dict.keys():
            if player_key not in game.players:
                game.new_player(instance_dict[player_key]['name'], player_key)
if gamestatus_dict['status'] == 1:
    game.start(gamestatus_dict['scenario'])
