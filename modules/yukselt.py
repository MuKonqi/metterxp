#!/usr/bin/env python3

# Copyright (C) 2021, 2022 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

import os
import sys

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
args=sys.argv[1:]

if "--yukseltiyukselt" in args:
    if os.path.isfile(debian):
        os.system(" apt install git -y")
    elif os.path.isfile(fedora):
        os.system(" dnf install git -y")
    elif os.path.isfile(solus):
        os.system(" eopkg install git -y")    
    os.system("cd /usr/local/bin/metterxp ;  git clone https://github.com/MuKonqi/metterxp ; cd metterxp ;  chmod +x *")
    os.system("cd /usr/local/bin/metterxp/modules ; rm yukselt.py")
    os.system(" cp /usr/local/bin/metterxp/metterxp/modules/mxp_update.py /usr/local/bin/metterxp/modules/")
    os.system(" python3 /usr/local/bin/metterxp/modules/mxp_update.py")
    exit()