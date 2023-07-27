#!/usr/bin/env python3

# Copyright (C) 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

import os
import sys
from subprocess import *
from tkinter import messagebox

en="/home/"+sys.argv[2]+"/.by-mukonqi/metterxp/language/en.txt"
tr="/home/"+sys.argv[2]+"/.by-mukonqi/metterxp/language/tr.txt"
debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if not os.path.isdir("/home/"+sys.argv[1]+"/.by-mukonqi/metterxp/"):
    def open_s():
        os.system("python3 /usr/local/bin/metterxp/modules/mxp_options.py")
        exit()
    if os.path.isfile(debian) or os.path.isfile(fedora) or os.path.isfile(solus):
        open_s()

if not os.getuid() == 0:
    if os.path.isfile(en):
        messagebox.showerror("Error","Only root can run this module!")
        exit()
    elif os.path.isfile(tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit()

if "--update" in sys.argv[2]:
    if os.path.isfile(debian):
        os.system("apt install git -y")
    elif os.path.isfile(fedora):
        os.system("dnf install git -y")
    elif os.path.isfile(solus):
        os.system("eopkg install git -y")    
    os.system("cd /usr/local/bin/metterxp/ ; git clone https://github.com/MuKonqi/metterxp ; cd metterxp ;  chmod +x *")
    os.system("cd /usr/local/bin/metterxp/modules ; rm mxp_reset.py")
    os.system("cp /usr/local/bin/metterxp/metterxp/app/modules/mxp_reset.py /usr/local/bin/metterxp/modules")
    os.system("python3 /usr/local/bin/metterxp/modules/mxp_reset.py")
    exit()

os.system("cd /home/"+sys.argv[1]+"/.by-mukonqi/ ; rm -rf metterxp")
os.system("cd /usr/local/bin/metterxp/metterxp/ ; python3 apiutaller.py --reinstall")
if os.path.isfile(en):
    messagebox.showinfo("Successful","MetterXP is has ben reset.")
elif os.path.isfile(tr):
    messagebox.showinfo("Başarılı","MetterXP sıfırlandı.")
os.system("metterxp")
exit()