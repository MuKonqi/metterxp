#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

# This file part of MetterXP.

import os

print("\nProgram/paket hataları çözülüyor...")
os.system(" apt-get install -f &&  dpkg --configure -a")
print("\nProgram/paket hataları çözüldü.")
exit()