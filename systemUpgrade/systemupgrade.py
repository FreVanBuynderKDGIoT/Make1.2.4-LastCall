#!/usr/bin/env python
"""
info about our project
"""

# import


__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"


import os


def call_system_update_upgrade():
    command = "sudo apt-get update -y"
    os.system(command)
    command = "sudo apt-get upgrade -y"
    os.system(command)

