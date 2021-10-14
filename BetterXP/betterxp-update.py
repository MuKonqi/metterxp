#!/usr/bin/env python3

# Copyright (C) 2021, Muhammed Abdurrahman

# This file is part of BetterXP and BetterXP Installer.

import os
if os.path.isfile('/etc/debian_version'):
    os.system("cd /usr/local/bin/BetterXP")
    os.system("sudo rm /usr/local/bin/BetterXP/betterxp-debian.py")
    os.system("sudo rm /usr/local/bin/BetterXP/betterxp-fedora.py")
    os.system("sudo rm /usr/local/bin/BetterXP/betterxp-solus.py")
    os.system("sudo rm /usr/local/bin/BetterXP/desktop.png")
    os.system("sudo rm -rf /usr/local/bin/BetterXP/ArchTerminal")
    os.system("sudo rm -rf /usr/local/bin/BetterXP/DebianTerminal")
    os.system("sudo rm -rf /usr/local/bin/BetterXP/KaliTerminal")
    os.system("sudo cp /usr/local/bin/BetterXP/BetterXP/BetterXP/betterxp-debian.py /usr/local/bin/BetterXP")
    os.system("sudo cp /usr/local/bin/BetterXP/BetterXP/BetterXP/betterxp-fedora.py /usr/local/bin/BetterXP")
    os.system("sudo cp /usr/local/bin/BetterXP/BetterXP/BetterXP/betterxp-solus.py /usr/local/bin/BetterXP")
    os.system("sudo cp /usr/local/bin/BetterXP/BetterXP/BetterXP/desktop.png /usr/local/bin/BetterXP")
    os.system("sudo cp -r /usr/local/bin/BetterXP/BetterXP/BetterXP/ArchTerminal /usr/local/bin/BetterXP")
    os.system("sudo cp -r /usr/local/bin/BetterXP/BetterXP/BetterXP/DebianTerminal /usr/local/bin/BetterXP")
    os.system("sudo cp -r /usr/local/bin/BetterXP/BetterXP/BetterXP/KaliTerminal /usr/local/bin/BetterXP")
    os.system("sudo rm -rf /usr/local/bin/BetterXP/BetterXP")
    exit()
elif os.path.isfile('/etc/fedora-release'):
    os.system("cd /usr/local/bin/BetterXP")
    os.system("sudo rm /usr/local/bin/BetterXP/betterxp-debian.py")
    os.system("sudo rm /usr/local/bin/BetterXP/betterxp-fedora.py")
    os.system("sudo rm /usr/local/bin/BetterXP/betterxp-solus.py")
    os.system("sudo rm /usr/local/bin/BetterXP/desktop.png")
    os.system("sudo rm -rf /usr/local/bin/BetterXP/ArchTerminal")
    os.system("sudo rm -rf /usr/local/bin/BetterXP/DebianTerminal")
    os.system("sudo rm -rf /usr/local/bin/BetterXP/KaliTerminal")
    os.system("sudo cp /usr/local/bin/BetterXP/BetterXP/BetterXP/betterxp-debian.py /usr/local/bin/BetterXP")
    os.system("sudo cp /usr/local/bin/BetterXP/BetterXP/BetterXP/betterxp-fedora.py /usr/local/bin/BetterXP")
    os.system("sudo cp /usr/local/bin/BetterXP/BetterXP/BetterXP/betterxp-solus.py /usr/local/bin/BetterXP")
    os.system("sudo cp /usr/local/bin/BetterXP/BetterXP/BetterXP/desktop.png /usr/local/bin/BetterXP")
    os.system("sudo cp -r /usr/local/bin/BetterXP/BetterXP/BetterXP/ArchTerminal /usr/local/bin/BetterXP")
    os.system("sudo cp -r /usr/local/bin/BetterXP/BetterXP/BetterXP/DebianTerminal /usr/local/bin/BetterXP")
    os.system("sudo cp -r /usr/local/bin/BetterXP/BetterXP/BetterXP/KaliTerminal /usr/local/bin/BetterXP")
    os.system("sudo rm -rf /usr/local/bin/BetterXP/BetterXP")
    exit()
elif os.path.isfile('/etc/solus-release'):
    os.system("cd /usr/local/bin/BetterXP")
    os.system("sudo rm /usr/local/bin/BetterXP/betterxp-debian.py")
    os.system("sudo rm /usr/local/bin/BetterXP/betterxp-fedora.py")
    os.system("sudo rm /usr/local/bin/BetterXP/betterxp-solus.py")
    os.system("sudo rm /usr/local/bin/BetterXP/desktop.png")
    os.system("sudo rm -rf /usr/local/bin/BetterXP/ArchTerminal")
    os.system("sudo rm -rf /usr/local/bin/BetterXP/DebianTerminal")
    os.system("sudo rm -rf /usr/local/bin/BetterXP/KaliTerminal")
    os.system("sudo cp /usr/local/bin/BetterXP/BetterXP/BetterXP/betterxp-debian.py /usr/local/bin/BetterXP")
    os.system("sudo cp /usr/local/bin/BetterXP/BetterXP/BetterXP/betterxp-fedora.py /usr/local/bin/BetterXP")
    os.system("sudo cp /usr/local/bin/BetterXP/BetterXP/BetterXP/betterxp-solus.py /usr/local/bin/BetterXP")
    os.system("sudo cp /usr/local/bin/BetterXP/BetterXP/BetterXP/desktop.png /usr/local/bin/BetterXP")
    os.system("sudo cp -r /usr/local/bin/BetterXP/BetterXP/BetterXP/ArchTerminal /usr/local/bin/BetterXP")
    os.system("sudo cp -r /usr/local/bin/BetterXP/BetterXP/BetterXP/DebianTerminal /usr/local/bin/BetterXP")
    os.system("sudo cp -r /usr/local/bin/BetterXP/BetterXP/BetterXP/KaliTerminal /usr/local/bin/BetterXP")
    os.system("sudo rm -rf /usr/local/bin/BetterXP/BetterXP")
    exit()
