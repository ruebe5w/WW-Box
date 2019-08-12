from playsound import playsound

gamestatus_dict = {'status': 0, 'scenario': 'default'}
instance_dict = {}


def play_audio(audio_file):  # TODO Does not work on the Raspberry
    """Plays an audio file"""
    playsound(audio_file)


def evaluate_voting():
    """Evaluates the Voting-Results in the instance_dict. Returns Array with the Player-ID(s)"""
    poll_dict = {}
    for ip in instance_dict.keys():
        if 'poll' in instance_dict[ip]:
            if instance_dict[ip]['poll'] in poll_dict:
                old = poll_dict[instance_dict[ip]['poll']]
                poll_dict.update({instance_dict[ip]['poll']: old + 1})
            else:
                poll_dict.update({instance_dict[ip]['poll']: 1})
    # Count votes:
    return max(poll_dict.keys(), key=lambda k: poll_dict[k])  # TODO max vote


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


def send_info(player, txt, img=''):
    """Sends an info GUI to passed player-id"""
    set_gui(player, 'info', {'text': txt}, imgPicture={'img': img})


def send_poll(player, txt, array):
    """Sends an Poll GUI to passed player-id"""
    set_gui(player, base='poll', txt1={'text': txt}, lvPoll={'list': array})


def send_tutorial(player, txt, array):
    """Sends an Tutorial GUI to passed player-id"""
    set_gui(player, base='tutorial', txt1={'text': txt}, lvTutorial={'list': array})
