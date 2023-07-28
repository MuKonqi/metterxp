#!/usr/bin/env python3

# Copyright (C) 2021, 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

import os
import sys
import subprocess
from subprocess import *
from tkinter import messagebox

en="/home/"+str(sys.argv[1])+"/.by-mukonqi/metterxp/language/en.txt"
tr="/home/"+str(sys.argv[1])+"/.by-mukonqi/metterxp/language/tr.txt"
debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if not os.path.isdir("/home/"+str(sys.argv[1])+"/.by-mukonqi/metterxp/"):
    messagebox.showerror("User Error - Fatal | MetterXP","Please start only MetterXP (just select MetterXP in the applications section or type metterxp) to set up language and theme preferences.")
    exit()

beta="yes"

if not "--reset" in sys.argv[2:]:
    v=open("/usr/local/bin/metterxp/version.txt", "r")
    vr=v.read()
    v.close()
    if beta == "no":
        vl = subprocess.Popen("curl https://raw.githubusercontent.com/MuKonqi/metterxp/main/app/version.txt", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = vl.communicate()
    elif beta == "yes":
        vlb = subprocess.Popen("curl https://raw.githubusercontent.com/MuKonqi/metterxp/beta/app/version.txt", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = vlb.communicate()
    if out == vr:
        if os.path.isfile(en):
            messagebox.showerror("","MetterXP is already up-to-date.")
        elif os.path.isfile(tr):
            messagebox.showerror("","MetterXP zaten güncel.")
        os.system("metterxp")
        exit()

if not os.getuid() == 0:
    if os.path.isfile(en):
        messagebox.showerror("Error","Only root can run this module!")
        exit()
    elif os.path.isfile(tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit()

if beta == "no":
    os.system("cd /usr/local/bin/ ; git clone https://github.com/MuKonqi/metterxp tmxp ; cd metterxp ;  chmod +x *")
elif beta == "yes":
    os.system("cd /usr/local/bin/ ; git clone -b beta https://github.com/MuKonqi/metterxp tmxp ; cd metterxp ;  chmod +x *")

if len(sys.argv) == 3:
    if "--reset" in sys.argv[2]:
        os.system("cd /home/"+sys.argv[1]+"/.by-mukonqi/ ; rm -rf metterxp") 
 
os.system("cd /usr/local/bin/tmxp/ ; python3 apiutaller.py --reinstall")
os.system("cd /usr/local/bin/ ; rm -rf tmxp")
os.system("metterxp")
exit()