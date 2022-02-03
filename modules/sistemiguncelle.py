#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

# This file part of MetterXP.

import os

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if os.path.isfile(debian):
    print("\nSistem güncellemesi işlemi başlatılıyor...\n")
    os.system("sudo apt upgrade -y")
    print("\nSistem güncellemesi varsa başarıyla tamamlandı.")
    exit()
elif os.path.isfile(fedora):
    print("\nSistem güncellemesi işlemi başlatılıyor...\n")
    os.system("sudo dnf update -y")
    print("\nSistem güncellemesi varsa başarıyla tamamlandı.")
    exit()
elif os.path.isfile(solus):
    print("\nSistem güncellemesi işlemi başlatılıyor...\n")
    os.system("sudo eopkg update -y")
    print("\nSistem güncellemesi varsa başarıyla tamamlandı.")
    exit()