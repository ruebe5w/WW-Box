from wwbox.game import *
from wwbox.web import WebThread, instance_dict

import os

web_thread = WebThread()
web_thread.start()
old_instance_dict = {}

game = Game()
while gamestatus_dict['status'] == 0:
    if old_instance_dict != instance_dict:
        for player_key in instance_dict.keys():
            if player_key not in game.players:
                game.new_player(instance_dict[player_key]['name'], player_key)
while True:
    if gamestatus_dict['status'] == 5:  # Tutorial

        for player in game.players.keys():
            print(player)
            send_tutorial(player, 'Hier ein kleines Tutorial zu Flos Künstler-WG:',
                          ['Bodyguard', 'Doenermann', 'Drogendealerin', 'Künstler', 'Nachbar', 'Nazi', 'OW-Suchtie',
                           'Stalker', 'WG-Flittchen', 'WG-Sprecher', 'Wingwoman'])
        gamestatus_dict['status'] = 0
    if gamestatus_dict['status'] == 4:  # Tutorial selection
        for player in game.players.keys():
            img_path = '../img/' + gamestatus_dict['tutorial'] + '.png'
            send_info(player, '_', img_path)
            # os.system('eog ' + img_path)
            print('IMG:' + '../img/' + gamestatus_dict['tutorial'] + '.png')
        audio_path = '../audios/' + gamestatus_dict['tutorial'] + '.wav'
        os.system('aplay ' + audio_path)
        # playsound(audio_path)
        gamestatus_dict['status'] = 5
    if gamestatus_dict['status'] == 1:  # Start
        game.start(gamestatus_dict['scenario'])
