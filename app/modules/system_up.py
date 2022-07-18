#!/usr/bin/env python3

# Copyright (C) 2021, 2022 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

import os
from tkinter import messagebox

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp/settings/lang/en.txt"

if not os.getuid() == 0 :
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Only root can run this module!")
        exit("Only root can run this module!\nClosing this module...")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit("\nSadece kök kullanıcı bu modülü çalıştırabilir!\nModül kapatılıyor...")

if not os.path.isdir("/usr/local/bin/metterxp/settings/lang/"):
    def lang_open():
        messagebox.showerror("Warning","Can't found language setting. When you click 'OK' and enter your true password, language settings will open. ")
        os.system("pkexec /usr/bin/metterxp mxp_options")
        exit()
    if os.path.isfile(debian):
        lang_open()
    elif os.path.isfile(fedora):
        lang_open()
    elif os.path.isfile(solus):
        lang_open()

if os.path.isfile(lang_en):
    messagebox.showinfo("Information","When you press the 'OK' button then the process will start. Please don't close MetterXP during the process.")
elif os.path.isfile(lang_tr):
    messagebox.showinfo("Bilgilendirme","'OK' düğmesine bastığınızda işlem başlayacaktır. Lütfen işlem sırasında MetterXP'ı kapatmayın.")
    
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