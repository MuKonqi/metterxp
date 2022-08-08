#!/usr/bin/env python3

# Copyright (C) 2022 MuKonqi (Muhammed Abdurrahman)

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


def module_exit():
    exit("\nThis module is shutting down...\nModül kapatılıyor...")

if not os.getuid() == 0:
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Only root can run this module!")
        exit("Only root can run this module!\nThis module is shutting down...")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit("\nSadece kök kullanıcı bu modülü çalıştırabilir!\nModül kapatılıyor...")

def installer():
    if os.path.isfile(debian):
        os.system("sudo apt install git -y")
    if os.path.isfile(fedora):
        os.system("sudo dnf install git -y")
    if os.path.isfile(solus):
        os.system("sudo eopkg install git -y")
    os.system("git clone https://github.com/MuKonqi/yasfetch")
    if not os.path.isdir("/usr/local/"):
        os.system("cd /usr/ ; mkdir local")
    if not os.path.isdir("/usr/local/bin/"):
        os.system("cd /usr/local/ ; mkdir bin")
    if not os.path.isdir("/usr/local/bin/yasfetch/"):
        os.system("cd /usr/local/bin/ ; mkdir yasfetch")
    os.system("cd yasfetch ; cd app ; chmod +x * ; cp LICENSE.txt /usr/local/bin/yasfetch/")
    os.system("cd yasfetch ; cd app ; chmod +x * ; cp yasfetch.py /usr/bin/yasfetch")
    os.system("rm -rf yasfetch")
    module_exit()
def reinstaller():
    os.system("cd /usr/bin/ ; rm yasfetch")
    os.system("cd /usr/local/bin/ ; rm -rf yasfetch")
    installer()
def uninstaller():
    os.system("cd /usr/bin/ ; rm yasfetch")
    os.system("cd /usr/local/bin/ ; rm -rf yasfetch")
    module_exit()

if "--install" in args:
    installer()
elif "--reinstaller" in args:
    reinstaller()
elif "--uninstaller" in args:
    uninstaller()