#!/usr/bin/env python3

# Copyright (C) 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

import os
from tkinter import messagebox
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

os.system("cd /usr/local/bin/metterxp/apiutaller/ ; python3 apiutaller.py --uninstall")
if os.path.isfile(en):
    messagebox.showinfo("Information","Successful! MetterXP is uninstalled on your system. You can share your feedback with MuKonqi.")
elif os.path.isfile(tr):
    messagebox.showinfo("Bilgilendirme","MetterXP başarıyla kaldırıldı. Geri bildiriminizi MuKonqi ile paylaşabilirsiniz.")
exit()