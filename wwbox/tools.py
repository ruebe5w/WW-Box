from playsound import playsound

gamestatus_dict = {'status': 0, 'scenario': 'default'}
instance_dict = {}


def play_audio(audio_file):
    """Plays an audio file"""
    playsound(audio_file)


def send_gui(player, gui_commands):
    """Updates Player's GUI"""
    print('PLEASE USE SET_GUI()')
    # TODO send information to players
    # if not death:


def set_gui(player, base, txt1, txt2=None, btStart=None, btLogin=None, btConf=None, ddScenario=None, imgPicture=None,
            listRoles=None, lvPoll=None, lvTutorial=None):
    '''Sets the GUI for a Player.
    set_gui(player=player_key, base='info', txt1={'text': 'Hallo ich bin eine autonome Info.'},
                    imgPicture='Rückseite.png')'''
    instance_dict[player]['ui'].update({'base': base})
    instance_dict[player]['ui'].update({'txt1': txt1})
    if not txt2 is None:
        instance_dict[player]['ui'].update({'txt2': txt2})
    if not btStart is None:
        instance_dict[player]['ui'].update({'btStart': btStart})
    if not btLogin is None:
        instance_dict[player]['ui'].update({'btLogin': btLogin})
    if not btConf is None:
        instance_dict[player]['ui'].update({'btConf': btConf})
    if not ddScenario is None:
        instance_dict[player]['ui'].update({'ddScenario': ddScenario})
    if not imgPicture is None:
        instance_dict[player]['ui'].update({'imgPicture': imgPicture})
    if not listRoles is None:
        instance_dict[player]['ui'].update({'listRoles': listRoles})
    if not lvPoll is None:
        instance_dict[player]['ui'].update({'lvPoll': lvPoll})
    if not lvTutorial is None:
        instance_dict[player]['ui'].update({'lvTutorial': lvTutorial})
