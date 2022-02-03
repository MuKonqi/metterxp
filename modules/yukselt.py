#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if os.path.isfile(debian):
    os.system("sudo apt install git -y")
elif os.path.isfile(fedora):
    os.system("sudo dnf install git -y")
elif os.path.isfile(solus):
    os.system("sudo eopkg install git -y")
os.system("cd /usr/bin/ ; sudo rm metterxp")
os.system("cd /usr/share/polkit-1/actions ; sudo rm python3.policy")
os.system("cd /usr/share/applications ; sudo rm metterxp.desktop")
os.system("cd /usr/local/bin/metterxp ; sudo rm -rf modules ; sudo rm icon.png ; sudo rm LICENSE")
os.system("cd /usr/local/bin/metterxp ; sudo git clone https://github.com/MuKonqi/metterxp ; cd metterxp ; sudo chmod +x *")
os.system("sudo mv /usr/local/bin/metterxp/metterxp/metterxp.py /usr/bin/metterxp")
os.system("sudo mv /usr/local/bin/metterxp/metterxp/python3.policy /usr/share/polkit-1/actions")
os.system("sudo mv /usr/local/bin/metterxp/metterxp/metterxp.desktop /usr/share/applications")
os.system("sudo mkdir /usr/local/bin/metterxp/modules ; sudo mv /usr/local/bin/metterxp/metterxp/modules/* /usr/local/bin/metterxp/modules ; sudo mv /usr/local/bin/metterxp/metterxp/icon.png /usr/local/bin/metterxp ; sudo mv /usr/local/bin/metterxp/metterxp/LICENSE /usr/local/bin/metterxp")
os.system("cd /usr/local/bin/metterxp ; sudo rm -rf metterxp")
exit()
