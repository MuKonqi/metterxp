#!/usr/bin/env python3

# Copyright (C) 2021, 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

import os
import sys
import subprocess
from subprocess import *
from tkinter import messagebox

en="/home/"+sys.argv[1]+"/.by-mukonqi/metterxp/language/en.txt"
tr="/home/"+sys.argv[1]+"/.by-mukonqi/metterxp/language/tr.txt"
debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if not os.path.isdir("/home/"+sys.argv[1]+"/.by-mukonqi/metterxp/"):
    def open_s():
        os.system("python3 /usr/local/bin/metterxp/modules/mxp_options.py")
        exit()
    if os.path.isfile(debian) or os.path.isfile(fedora) or os.path.isfile(solus):
        open_s()

beta="yes"
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
    exit()

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
    os.system("cd /usr/local/bin/metterxp/modules ; rm mxp_update.py")
    os.system("cp /usr/local/bin/metterxp/metterxp/app/modules/mxp_update.py /usr/local/bin/metterxp/modules")
    os.system("python3 /usr/local/bin/metterxp/modules/mxp_update.py")
    exit()

os.system("cd /usr/local/bin/metterxp/metterxp/ ; python3 apiutaller.py --reinstall")
if os.path.isfile(en):
    messagebox.showinfo("Successful","MetterXP is updated to newer version.")
elif os.path.isfile(tr):
    messagebox.showinfo("Başarılı","MetterXP daha yeni bir sürüme güncellendi.")
os.system("metterxp")
exit()