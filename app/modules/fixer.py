#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

# This file part of MetterXP.

import os
from tkinter import messagebox

if not os.getuid() == 0:
    messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
    exit("\nSadece kök kullanıcı bu modülü çalıştırabilir!\nModül kapatılıyor...")

print("\nProgram/paket hataları çözülüyor...")
os.system(" apt-get install -f &&  dpkg --configure -a")
print("\nProgram/paket hataları çözüldü.")
exit()