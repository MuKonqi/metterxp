#!/usr/bin/env python3

# Copyright (C) 2021, 2022 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

import os
import sys
from tkinter import *
from tkinter import messagebox

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp/settings/lang/en.txt"
args=sys.argv[1:]

if not os.getuid() == 0:
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Only root can run this module!")
        exit("Only root can run this module!\nThis module is shutting down...")
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

if "--updateupdater" in args:
    if os.path.isfile(lang_en):
        messagebox.showinfo("Information","When you press the 'OK' button then the process will start. Please don't close MetterXP during the process.")
    elif os.path.isfile(lang_tr):
        messagebox.showinfo("Bilgilendirme","'OK' düğmesine bastığınızda işlem başlayacaktır. Lütfen işlem sırasında MetterXP'ı kapatmayın.")
    if os.path.isfile(debian):
        os.system(" apt install git -y")
    elif os.path.isfile(fedora):
        os.system(" dnf install git -y")
    elif os.path.isfile(solus):
        os.system(" eopkg install git -y")    
    os.system("cd /usr/local/bin/metterxp/ ;  git clone https://github.com/MuKonqi/metterxp ; cd metterxp ;  chmod +x *")
    os.system("cd /usr/local/bin/metterxp/modules ;  rm mxp_update.py")
    os.system(" cp /usr/local/bin/metterxp/metterxp/app/modules/mxp_update.py /usr/local/bin/metterxp/modules")
    os.system(" python3 /usr/local/bin/metterxp/modules/mxp_update.py")
    exit()

if os.path.isfile("/usr/local/bin/metterxp/python3.policy"):
    os.system("cd /usr/local/bin/metterxp ; rm python3.policy")
if not os.path.isdir("/usr/local/bin/metterxp/apiutaller"):
    os.system("cd /usr/local/bin/metterxp/ ; mkdir apiutaller")
os.system("cd /usr/bin/ ;  rm metterxp")
os.system("cd /usr/share/polkit-1/actions ;  rm io.github.mukonqi.metterxp.policy")
os.system("cd /usr/share/applications ;  rm metterxp.desktop")
os.system("cd /usr/local/bin/metterxp/ ;  rm -rf modules ; rm -rf unsupported.app ; rm icon.png ;  rm LICENSE.txt")
os.system(" chmod +x /usr/local/bin/metterxp/metterxp/app/metterxp.py ; mv /usr/local/bin/metterxp/metterxp/app/metterxp.py /usr/bin/metterxp")
os.system(" chmod +x /usr/local/bin/metterxp/metterxp/apiutaller.py ; mv /usr/local/bin/metterxp/metterxp/apiutaller.py /usr/local/bin/metterxp/apiutaller")
os.system(" chmod +x /usr/local/bin/metterxp/metterxp/app/io.github.mukonqi.metterxp.policy ; mv /usr/local/bin/metterxp/metterxp/app/io.github.mukonqi.metterxp.policy /usr/share/polkit-1/actions/")
os.system(" chmod +x /usr/local/bin/metterxp/metterxp/app/metterxp.desktop ; mv /usr/local/bin/metterxp/metterxp/app/metterxp.desktop /usr/share/applications")
os.system(" chmod +x /usr/local/bin/metterxp/metterxp/app/unsupported.app/* ;  mv /usr/local/bin/metterxp/metterxp/app/unsupported.app /usr/local/bin/metterxp/")
os.system(" chmod +x /usr/local/bin/metterxp/metterxp/app/modules/* ; mkdir /usr/local/bin/metterxp/modules ; mv /usr/local/bin/metterxp/metterxp/app/modules/* /usr/local/bin/metterxp/modules ;  mv /usr/local/bin/metterxp/metterxp/app/icon.png /usr/local/bin/metterxp/ ;  mv /usr/local/bin/metterxp/metterxp/app/LICENSE.txt /usr/local/bin/metterxp/")
os.system("cd /usr/local/bin/metterxp/ ;  rm -rf metterxp")
if os.path.isfile(lang_en):
    messagebox.showinfo("Good New","Successful! Updated MetterXP to a newer version. If you click 'OK', MetterXP will be close.")
elif os.path.isfile(lang_tr):
    messagebox.showinfo("İyi Haber","Başarılı! MetterXP daha yeni bir sürüme güncellendi. 'OK' tuşuna bastığınızda MetterXP kapatılacak.")
exit()