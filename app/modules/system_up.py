#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

# This file part of MetterXP.

import os
from tkinter import messagebox

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp-beta/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp-beta/settings/lang/en.txt"

if not os.getuid() == 0 :
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Only root can run this module!")
        exit("Only root can run this module!\nClosing this module...")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit("\nSadece kök kullanıcı bu modülü çalıştırabilir!\nModül kapatılıyor...")

if os.path.isfile(lang_en):
    messagebox.showinfo("Information","When you press the 'OK' button then the process will start. Please do NOT close MetterXP during the process.")
elif os.path.isfile(lang_tr):
    messagebox.showinfo("Bilgilendirme","'OK' düğmesine bastığınızda işlem başlayacaktır. Lütfen işlem sırasında MetterXP'i kapatMAyın.")
if os.path.isfile(debian):
    os.system(" apt upgrade -y")
elif os.path.isfile(fedora):
    os.system(" dnf update -y")
elif os.path.isfile(solus):
    os.system(" eopkg up -y")
if os.path.isfile(lang_en):
    messagebox.showinfo("Information","Succesful! If a system update is available, it is complete.")
elif os.path.isfile(lang_tr):
    messagebox.showinfo("Bilgilendirme","Bir sistem güncellemesi varsa, tamamlandı.")
exit()