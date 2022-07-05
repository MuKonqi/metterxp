#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

# This file part of MetterXP.

import os
import sys
from tkinter import messagebox

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp-beta/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp-beta/settings/lang/en.txt"
args=sys.argv[1:]

if not os.getuid() == 0:
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Only root can run this module!")
        exit("Only root can run this module!\nClosing this module...")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit("\nSadece kök kullanıcı bu modülü çalıştırabilir!\nModül kapatılıyor...")

if "--updateupdater" in args:
    if os.path.isfile(debian):
        os.system(" apt install git -y")
    elif os.path.isfile(fedora):
        os.system(" dnf install git -y")
    elif os.path.isfile(solus):
        os.system(" eopkg install git -y")    
    os.system("cd /usr/local/bin/metterxp-beta/ ;  git clone -b beta https://github.com/MuKonqi/metterxp metterxp ; cd metterxp ;  chmod +x *")
    os.system("cd /usr/local/bin/metterxp-beta/modules ;  rm mxp_update.py")
    os.system(" cp /usr/local/bin/metterxp-beta/metterxp/app/modules/mxp_update.py /usr/local/bin/metterxp-beta/modules")
    os.system(" python3 /usr/local/bin/metterxp-beta/modules/mxp_update.py")
    exit()

os.system("cd /usr/bin/ ;  rm metterxp-beta")
os.system("cd /usr/share/polkit-1/actions ;  rm python3.policy")
os.system("cd /usr/share/applications ;  rm metterxp-beta.desktop")
os.system("cd /usr/local/bin/metterxp-beta/ ;  rm -rf modules ; rm -rf unsupported.app ; rm icon.png ;  rm LICENSE.txt")
os.system(" chmod +x /usr/local/bin/metterxp-beta/metterxp/app/metterxp-beta.py ; mv /usr/local/bin/metterxp-beta/metterxp/app/metterxp-beta.py /usr/bin/metterxp-beta")
os.system(" chmod +x /usr/local/bin/metterxp-beta/metterxp/app/python3.policy ; mv /usr/local/bin/metterxp-beta/metterxp/app/python3.policy /usr/share/polkit-1/actions/")
os.system(" chmod +x /usr/local/bin/metterxp-beta/metterxp/app/metterxp-beta.desktop ; mv /usr/local/bin/metterxp-beta/metterxp/app/metterxp-beta.desktop /usr/share/applications")
os.system(" chmod +x /usr/local/bin/metterxp-beta/metterxp/app/unsupported.app/* ;  mv /usr/local/bin/metterxp-beta/metterxp/app/unsupported.app /usr/local/bin/metterxp-beta/")
os.system(" chmod +x /usr/local/bin/metterxp-beta/metterxp/app/modules/* ; mkdir /usr/local/bin/metterxp-beta/modules ; mv /usr/local/bin/metterxp-beta/metterxp/app/modules/* /usr/local/bin/metterxp-beta/modules ;  mv /usr/local/bin/metterxp-beta/metterxp/app/icon.png /usr/local/bin/metterxp-beta/ ;  mv /usr/local/bin/metterxp-beta/metterxp/app/LICENSE.txt /usr/local/bin/metterxp-beta/")
os.system("cd /usr/local/bin/metterxp-beta/ ;  rm -rf metterxp")
if os.path.isfile(lang_en):
    messagebox.showinfo("Good New","Succesful! Updated MetterXP to a newer version. MetterXP is shutting down for updates to apply...")
elif os.path.isfile(lang_tr):
    messagebox.showinfo("İyi Haber","Başarılı! MetterXP daha yeni bir sürüme güncellendi. MetterXP, güncellemelerin uygulanması için kapatılıyor...")
os.system("python3 /usr/bin/metterxp-beta")
exit()