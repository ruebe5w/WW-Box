import logging
import os
import sys
from configparser import ConfigParser
from wwbox.baserole import BaseRole

logger = logging.getLogger(__name__)


def import_roles():
    role_file_array = import_role_files()
    role_array = {}
    for role_file in role_file_array:
        night_actions = role_file['NIGHT_ACTIONS']
        day_actions = role_file['DAY_ACTIONS']
        death_actions = role_file['DEATH_ACTIONS']
        night_acts = {}
        for action in night_actions.keys():
            night_acts.update(name: str, id: int, kind: str, conditions, target: Player
        role_array[role_file['GENERAL']['name']] = BaseRole(role_file['GENERAL']['name'],
                                                            role_file['GENERAL']['gender'], night_actions, day_actions,
                                                            death_actions, role_file['GENERAL']['img'])
    return role_array

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
