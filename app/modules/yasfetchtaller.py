#!/usr/bin/env python3

# Copyright (C) 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os
import sys

en="/home/"+sys.argv[1]+"/.by-mukonqi/metterxp/language/en.txt"
tr="/home/"+sys.argv[1]+"/.by-mukonqi/metterxp/language/tr.txt"
debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if not os.path.isdir("/home/"+str(sys.argv[1])+"/.by-mukonqi/metterxp/"):
    messagebox.showerror("User Error - Fatal | MetterXP","Please start only MetterXP (just select MetterXP in the applications section or type metterxp) to set up language and theme preferences.")
    exit()

if not os.getuid() == 0:
    if os.path.isfile(en):
        messagebox.showerror("Error","Only root can run this module!")
        exit()
    elif os.path.isfile(tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit()

if str(sys.argv[2]) == "--install":
    if os.path.isfile(debian):
        os.system("apt install git python3 -y")
    if os.path.isfile(fedora):
        os.system("dnf install git python3 -y")
    if os.path.isfile(solus):
        os.system("eopkg install git python3 -y")
    os.system("cd /usr/local/bin/ ; git clone https://github.com/MuKonqi/yasfetch tmxpyasfetch")
    os.system("cd /usr/local/bin/tmxpyasfetch ; python3 apiutlaler.py --install ; cd .. ; rm -rf tmxpyasfetch")
    exit()
if str(sys.argv[2]) == "--reinstall":
    if os.path.isfile(debian):
        os.system("sudo apt install git python3 -y")
    if os.path.isfile(fedora):
        os.system("sudo dnf install git python3 -y")
    if os.path.isfile(solus):
        os.system("sudo eopkg install git python3 -y")
    os.system("cd /usr/local/bin/ ; git clone https://github.com/MuKonqi/yasfetch tmxpyasfetch")
    os.system("cd /usr/local/bin/tmxpyasfetch ; python3 apiutlaler.py --reinstall ; cd .. ; rm -rf tmxpyasfetch")
if str(sys.argv[2]) == "--uninstall":
    os.system("cd /usr/local/bin/yasfetch/apiutaller ; python3 apiutaller.py --uninstall")
exit()