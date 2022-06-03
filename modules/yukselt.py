#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

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
    os.system("cd /usr/local/bin/metterxp/modules ;  rm yukselt.py")
    os.system(" mv /usr/local/bin/metterxp/metterxp/modules/yukselt.py /usr/local/bin/metterxp/modules/yukselt.py")
    os.system(" python3 /usr/local/bin/metterxp/modules/yukselt.py")
    exit()

os.system("cd /usr/bin/ ;  rm metterxp")
os.system("cd /usr/share/polkit-1/actions ;  rm python3.policy")
os.system("cd /usr/share/applications ;  rm metterxp.desktop")
os.system("cd /usr/local/bin/metterxp ;  rm -rf modules ;  rm icon.png ;  rm LICENSE")
os.system(" mv /usr/local/bin/metterxp/metterxp/metterxp.py /usr/bin/metterxp")
os.system(" mv /usr/local/bin/metterxp/metterxp/python3.policy /usr/share/polkit-1/actions/")
os.system(" mv /usr/local/bin/metterxp/metterxp/metterxp.desktop /usr/share/applications")
os.system(" mkdir /usr/local/bin/metterxp/modules ;  mv /usr/local/bin/metterxp/metterxp/modules/* /usr/local/bin/metterxp/modules ;  mv /usr/local/bin/metterxp/metterxp/icon.png /usr/local/bin/metterxp ;  mv /usr/local/bin/metterxp/metterxp/LICENSE /usr/local/bin/metterxp")
os.system("cd /usr/local/bin/metterxp ;  rm -rf metterxp")
exit()