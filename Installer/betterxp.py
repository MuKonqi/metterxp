#!/usr/bin/env python3

# Copyright (C) 2021, Muhammed Abdurrahman

# This file is part of BetterXP and BetterXP Installer.

import os
if os.name == "nt":
    print("BetterXP başlatıcısına hoş geldiniz!\nBetterXP ile BetterXP başlatıcısı NT çekirdeğini kullanan işletim sistemlerinde (Windows, ReactOS) çalışmaz.\nLütfen şu üç GNU/Linux dağıtımından birini temel alan bir GNU/Linux dağıtımıyla programı açmayı deneyiniz:\nDebian GNU/Linux, Fedora Linux, Solus\n\nBetterXP başlatıcısı kapatılıyor...")
    exit()
elif os.path.isfile("/etc/debian_version"):
    print("Copyright (C) 2021, Muhammed Abdurrahman\nBu program GNU General Public License, Version 3 altında lisanslanmıştır.\nDetaylar için: Devam et! -> BetterXP Hakkında -> Lisans\n\nBetterXP başlatılıyor...")
    os.system("python3 /usr/local/bin/BetterXP/betterxp-debian.py")
elif os.path.isfile("/etc/fedora-release"):
    print("Copyright (C) 2021, Muhammed Abdurrahman\nBu program GNU General Public License, Version 3 altında lisanslanmıştır.\nDetaylar için: Devam et! -> BetterXP Hakkında -> Lisans\n\nBetterXP başlatılıyor...")
    os.system("python3 /usr/local/bin/BetterXP/betterxp-fedora.py")
elif os.path.isfile("/etc/solus-release"):
    print("Copyright (C) 2021, Muhammed Abdurrahman\nBu program GNU General Public License, Version 3 altında lisanslanmıştır.\nDetaylar için: Devam et! -> BetterXP Hakkında -> Lisans\n\nBetterXP başlatılıyor...")
    os.system("python3 /usr/local/bin/BetterXP/betterxp-solus.py")
else:
    print("BetterXP başlatıcısına hoş geldiniz!\nKullandığınız GNU/Linux dağıtımını BetterXP ile BetterXP başlatıcısı tam anlamıyla desteklemiyor.\n\nBetterXP başlatıcısı kapatılıyor...")
    exit()