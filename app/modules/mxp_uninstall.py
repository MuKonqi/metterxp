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

if not os.path.isdir("/home/"+sys.argv[1]+"/.by-mukonqi/metterxp/"):
    def open_s():
        os.system("python3 /usr/local/bin/metterxp/modules/mxp_options.py")
        exit()
    if os.path.isfile(debian) or os.path.isfile(fedora) or os.path.isfile(solus):
        open_s()

if not os.getuid() == 0:
    if os.path.isfile(en):
        messagebox.showerror("Error","Only root can run this module!")
        exit("Only root can run this module!\nThis module is shutting down...")
    elif os.path.isfile(tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit("\nSadece kök kullanıcı bu modülü çalıştırabilir!\nModül kapatılıyor...")

os.system("cd /usr/local/bin/metterxp/apiutaller/ ; python3 apiutaller.py --uninstall")
if os.path.isfile(en):
    messagebox.showinfo("Information","Successful! MetterXP is uninstalled on your system. You can share your feedback with MuKonqi.")
elif os.path.isfile(tr):
    messagebox.showinfo("Bilgilendirme","MetterXP başarıyla kaldırıldı. Geri bildiriminizi MuKonqi ile paylaşabilirsiniz.")
exit()