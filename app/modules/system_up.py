#!/usr/bin/env python3

# Copyright (C) 2021, 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

import os
from tkinter import messagebox
import sys

en="/home/"+sys.argv[1]+"/.by-mukonqi/metterxp/language/en.txt"
tr="/home/"+sys.argv[1]+"/.by-mukonqi/metterxp/language/tr.txt"
debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if os.path.isdir("/home/"+str(sys.argv[1])+"/.by-mukonqi/metterxp/"):
    messagebox.showerror("User Error - Fatal | MetterXP","Please start only MetterXP (just select MetterXP in the applications section or type metterxp) to set up language and theme preferences.")
    exit()

if not os.getuid() == 0:
    if os.path.isfile(en):
        messagebox.showerror("Error","Only root can run this module!")
        exit()
    elif os.path.isfile(tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit()
    
if os.path.isfile(debian):
    os.system("apt upgrade -y")
elif os.path.isfile(fedora):
    os.system("dnf update -y")
elif os.path.isfile(solus):
    os.system("eopkg up -y")
if os.path.isfile(en):
    messagebox.showinfo("Information","If a system update is available, it has been completed.")
elif os.path.isfile(tr):
    messagebox.showinfo("Bilgilendirme","Eğer bir sistem güncellemesi mevcutsa tamamlandı.")
exit()