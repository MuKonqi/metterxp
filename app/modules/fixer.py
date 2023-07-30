#!/usr/bin/env python3

# Copyright (C) 2021, 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

import os
from tkinter import messagebox
import sys

en="/home/"+sys.argv[1]+"/.by-mukonqi/metterxp/language/en.txt"
tr="/home/"+sys.argv[1]+"/.by-mukonqi/metterxp/language/tr.txt"
debian="/etc/debian_version"

if not os.path.isdir("/home/"+str(sys.argv[1])+"/.by-mukonqi/metterxp/"):
    messagebox.showerror("User Error - Fatal | MetterXP","Please start only MetterXP (just select MetterXP in the applications section or type metterxp) to set up language and theme preferences.")
    exit()

if not os.path.isfile(debian):
    if os.path.isfile(en):
        messagebox.showerror("Fatal Error","This feature module does not support non-Debian based distros.")
    elif os.path.isfile(tr):
        messagebox.showerror("Fatal Error","Bu özellik modülü Debian tabanlı olmayan dağıtımları desteklemez.")        

if not os.getuid() == 0:
    if os.path.isfile(en):
        messagebox.showerror("Error","Only root can run this module!")
        exit()
    elif os.path.isfile(tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit()

os.system("apt-get install -f &&  dpkg --configure -a")
if os.path.isfile(en):
    messagebox.showinfo("Information","Successful! Applicaton/package errors are fixed.")
elif os.path.isfile(tr):
    messagebox.showinfo("Bilgilendirme","Program/paket hataları başarıyla çözüldü.")
exit()