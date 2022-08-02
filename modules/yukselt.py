#!/usr/bin/env python3

# Copyright (C) 2021, 2022 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

import os

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if not os.path.isdir("/usr/local/bin/metterxp/apiutaller"):
    os.system("cd /usr/local/bin/metterxp/ ; mkdir apiutaller")
os.system("cd /usr/bin/ ;  rm metterxp")
os.system("cd /usr/share/applications ;  rm metterxp.desktop")
os.system("cd /usr/local/bin/metterxp/ ;  rm -rf modules ; rm -rf unsupported.app ; rm icon.png ; rm LICENSE")
os.system(" chmod +x /usr/local/bin/metterxp/metterxp/app/metterxp.py ; mv /usr/local/bin/metterxp/metterxp/app/metterxp.py /usr/bin/metterxp")
os.system(" chmod +x /usr/local/bin/metterxp/metterxp/apiutaller.py ; mv /usr/local/bin/metterxp/metterxp/apiutaller.py /usr/local/bin/metterxp/apiutaller")
os.system(" chmod +x /usr/local/bin/metterxp/metterxp/app/io.github.mukonqi.metterxp.policy ; mv /usr/local/bin/metterxp/metterxp/app/io.github.mukonqi.metterxp.policy /usr/share/polkit-1/actions/")
os.system(" chmod +x /usr/local/bin/metterxp/metterxp/app/metterxp.desktop ; mv /usr/local/bin/metterxp/metterxp/app/metterxp.desktop /usr/share/applications")
os.system(" chmod +x /usr/local/bin/metterxp/metterxp/app/unsupported.app/* ;  mv /usr/local/bin/metterxp/metterxp/app/unsupported.app /usr/local/bin/metterxp/")
os.system(" chmod +x /usr/local/bin/metterxp/metterxp/app/modules/* ; mkdir /usr/local/bin/metterxp/modules ; mv /usr/local/bin/metterxp/metterxp/app/modules/* /usr/local/bin/metterxp/modules ;  mv /usr/local/bin/metterxp/metterxp/app/icon.png /usr/local/bin/metterxp/ ;  mv /usr/local/bin/metterxp/metterxp/app/LICENSE.txt /usr/local/bin/metterxp/")
os.system("cd /usr/local/bin/metterxp/ ;  rm -rf metterxp")
exit()