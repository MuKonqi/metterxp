#!/usr/bin/env python3

# Copyright (C) 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os
import sys

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp/settings/lang/en.txt"
args=sys.argv[1:]

if not os.getuid() == 0:
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Only root can run this module!")
        exit("Only root can run this module!\nThis module is shutting down...")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit("\nSadece kök kullanıcı bu modülü çalıştırabilir!\nModül kapatılıyor...")

def installer():
    if os.path.isfile(debian):
        os.system("sudo apt install git python3 -y")
    if os.path.isfile(fedora):
        os.system("sudo dnf install git python3 -y")
    if os.path.isfile(solus):
        os.system("sudo eopkg install git python3 -y")
    os.system("pip3 install psutil distro")
    os.system("git clone https://github.com/MuKonqi/yasfetch")
    os.system("cd yasfetch ; python3 apiutlaler.py --install")
    exit()
def reinstaller():
    os.system("cd /usr/bin/ ; rm yasfetch")
    os.system("cd /usr/local/bin/ ; rm -rf yasfetch")
    installer()
def uninstaller():
    os.system("cd /usr/bin/ ; rm yasfetch")
    os.system("cd /usr/local/bin/ ; rm -rf yasfetch")
    exit()

if "--install" in args:
    installer()
elif "--reinstall" in args:
    reinstaller()
elif "--uninstall" in args:
    uninstaller()