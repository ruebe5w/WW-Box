import logging
import os
import sys
from configparser import ConfigParser
from wwbox.role import Role
from wwbox.action import Action

logger = logging.getLogger(__name__)


# name: str, id: int, kind: str, conditions, target: Player
def import_roles():
    role_file_array = import_role_files()
    role_array = {}
    for role_file in role_file_array:
        night_acts = role_file['NIGHT_ACTIONS']
        day_acts = role_file['DAY_ACTIONS']
        death_acts = role_file['DEATH_ACTIONS']
        name = role_file['GENERAL']['name']
        gender = role_file['GENERAL']['gender']
        toa = role_file['GENERAL']['toa']
        img = role_file['GENERAL']['img']
        scenario = role_file['GENARAL']['scenario']
        night_actions = {}
        day_actions = {}
        death_actions = {}
        actions = import_actions()
        for key in night_acts.keys():
            if key not in actions:
                raise Exception('There is no Action named {}.'.format(key))
            night_actions.update({key: actions[key]})
        for key in day_acts.keys():
            if key not in actions:
                raise Exception('There is no Action named {}.'.format(key))
            day_actions.update({key: actions[key]})
        for key in death_acts.keys():
            if key not in actions:
                raise Exception('There is no Action named {}.'.format(key))
            death_actions.update({key: actions[key]})
        role_array[name] = Role(name, gender, toa, night_actions, day_actions, death_actions, img, scenario)
    return role_array


def import_actions():
    action_file_array = import_action_files()
    action_array = {}
    for action_file in action_file_array:
        name = action_file['GENERAL']['name']
        id = action_file['GENERAL']['id']
        conditions = action_file['CONDITIONS']
        method = action_file['METHOD']
        # condins=action_file['CONDITIONS']
        # conditions={}
        # for key in condins.keys():
        #    conditions.update(condins[key])
        action_array[name] = Action(name, id, conditions, method)
    return action_array


def import_role_files():
    """Imports Role-Files"""
    ending = '.txt'
    path = '../roles'
    role_array = __import_files(path, ending)
    return role_array


def import_action_files():
    """Imports Action-Files"""
    ending = '.txt'
    path = '../actions'
    action_array = __import_files(path, ending)
    return action_array


def __import_files(path, ending):
    """Imports txt Files from a path and parse them into Arrays"""
    files = []
    values = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if ending in file:
                files.append(os.path.join(r, file))
    i = 0
    for file in files:
        values[i] = ConfigParser()
        try:
            with open(file) as f:
                values[i].read_file(f)
        except FileNotFoundError:
            logger.critical(
                "File not found: {} - ensure it is in your current directory or update envvar WWBOT_CONFIGFILE".format(
                    file))
            sys.exit(1)
        i += 1

    return values
