import logging
import os
import sys
from configparser import ConfigParser
from wwbox.role import Role
from wwbox.action import Action
from wwbox.scenario import Scenario

logger = logging.getLogger(__name__)


def import_scenario():
    """Imports Scenarios from Scenario-Config-Files."""
    scenario_file_array = __import_scenario_files()
    scenario_array = {}
    for scenario_file in scenario_file_array:
        role_names = scenario_file['ROLES']
        name = scenario_file['GENERAL']['name']
        img = scenario_file['GENERAL']['img']
        author = scenario_file['GENERAL']['author']
        description = scenario_file['GENERAL']['description']
        discussion_time = scenario_file['GENERAL']['discussion_time']
        audios = scenario_file['AUDIOS']

        roles = import_roles()
        role_array = import_dict(role_names, roles, 'Role')

        scenario_array[name] = Scenario(name, author, description, audios, img, role_array, discussion_time)
    return scenario_array


# name: str, id: int, kind: str, conditions, target: Player
def import_roles():
    """Imports roles from Role-Config-Files."""
    role_file_array = __import_role_files()
    role_array = {}
    for role_file in role_file_array:
        night_acts = role_file['NIGHT_ACTIONS']
        day_acts = role_file['DAY_ACTIONS']
        on_attack_acts = role_file['ON_ATTACK_ACTIONS']
        death_acts = role_file['DEATH_ACTIONS']
        name = role_file['GENERAL']['name']
        gender = role_file['GENERAL']['gender']
        toa = role_file['GENERAL']['toa']
        img = role_file['GENERAL']['img']
        team = role_file['GENERAL']['team']
        scenario = role_file['GENARAL']['scenario']

        actions = import_actions()
        night_actions = import_dict(night_acts, actions, 'Action')
        day_actions = import_dict(day_acts, actions, 'Action')
        on_attack_actions = import_dict(on_attack_acts, actions, 'Action')
        death_actions = import_dict(death_acts, actions, 'Action')
        role_array[name] = Role(name, gender, toa, team, night_actions, day_actions, on_attack_actions, death_actions,
                                img, scenario)
    return role_array


def import_dict(previous_dict, value_dict, key_cat: str):
    """Imports dicts from Config-Files"""
    return_dict = {}
    for key in previous_dict.keys():
        if key not in value_dict:
            raise Exception('There is no ' + key_cat + ' named {}.'.format(key))
        return_dict.update({key: value_dict[key]})
    return return_dict


def import_actions():
    """Imports Actions from Action-Config-Files"""
    action_file_array = __import_action_files()
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


def __import_scenario_files():
    """Imports Scenario-Files"""
    ending = '.ini'
    path = 'scenarios'
    scenario_array = __import_files(path, ending)
    return scenario_array


def __import_role_files():
    """Imports Role-Files"""
    ending = '.ini'
    path = '../roles'
    role_array = __import_files(path, ending)
    return role_array


def __import_action_files():
    """Imports Action-Files"""
    ending = '.ini'
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

        values.append(ConfigParser())
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
