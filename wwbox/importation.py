from configparser import ConfigParser
import logging
import sys
import os

logger = logging.getLogger(__name__)


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
