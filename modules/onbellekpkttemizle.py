#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

# This file part of MetterXP.

import os

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if os.path.isfile(debian):
    print("\nÖnbelleği ve gereksiz paketları temizleme işlemi başlatılıyor...\n")
    os.system(" apt autoremove -y")
    print("\nÖnbellek ve gereksiz paketler başarıyla temizlendi.")
    exit()
elif os.path.isfile(fedora):
    print("\nÖnbelleği ve gereksiz paketları temizleme işlemi başlatılıyor...\n")
    os.system(" dnf autoremove -y &&  dnf clean all")
    print("\nÖnbellek ve gereksiz paketler başarıyla temizlendi.")
    exit()
elif os.path.isfile(solus):
    print("\nÖnbelleği temizleme işlemi başlatılıyor...\n")
    os.system(" eopkg dc -y")
    print("\nÖnbellek başarıyla temizlendi.")
    exit()