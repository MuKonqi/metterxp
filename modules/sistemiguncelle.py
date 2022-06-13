#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

# This file part of MetterXP.

import os
from tkinter import messagebox

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if not os.getuid() == 0:
    messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
    exit("\nSadece kök kullanıcı bu modülü çalıştırabilir!\nModül kapatılıyor...")

if os.path.isfile(debian):
    print("\nSistem güncellemesi işlemi başlatılıyor...\n")
    os.system(" apt upgrade -y")
    print("\nSistem güncellemesi varsa başarıyla tamamlandı.")
    exit()
elif os.path.isfile(fedora):
    print("\nSistem güncellemesi işlemi başlatılıyor...\n")
    os.system(" dnf update -y")
    print("\nSistem güncellemesi varsa başarıyla tamamlandı.")
    exit()
elif os.path.isfile(solus):
    print("\nSistem güncellemesi işlemi başlatılıyor...\n")
    os.system(" eopkg up -y")
    print("\nSistem güncellemesi varsa başarıyla tamamlandı.")
    exit()
