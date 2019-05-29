from configparser import ConfigParser
from errno import ENOENT

import sys

conf = ConfigParser()

conffile = "config.ini"

try:
    with open(conffile) as f:
        conf.read_file(f)
except ENOENT:
    print("File not found: {} - ensure it is in your current directory.".format(conffile))
    sys.exit(1)
