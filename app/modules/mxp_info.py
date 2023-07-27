#!/usr/bin/env python3

# Copyright (C) 2021, 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os
import subprocess
from subprocess import *

beta="yes"

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp/settings/lang/en.txt"

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

bg=""
fg=""
button_bg=""
button_fg=""
a_button_bg=""
a_button_fg=""
if os.path.isfile("/usr/local/bin/metterxp/settings/theme/0.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#03035B"
    a_button_fg="#FFFFFF"
if os.path.isfile("/usr/local/bin/metterxp/settings/theme/0_1.txt"):
    bg="darkgrey"
    fg="#376296"
    button_bg="#FFFFFF"
    button_fg="#376296"
    a_button_bg="#376296"
    a_button_fg="#FFA500"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/1.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/2.txt"):
    bg="#FFFFFF"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFFFF"
    a_button_bg="#FFFFFF"
    a_button_fg="#000000"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/3.txt"):
    bg="#808080"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#808080"
    a_button_bg="#808080"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/4.txt"):
    bg="#FF0000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#FF0000"
    a_button_bg="#FF0000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/5.txt"):
    bg="#FFA500"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#FFA500"
    a_button_bg="#FFA500"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/6.txt"):
    bg="#008000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#008000"
    a_button_bg="#008000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/7.txt"):
    bg="#0000FF"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#0000FF"
    a_button_bg="#0000FF"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/8.txt"):
    bg="#000080"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000080"
    a_button_bg="#000080"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/9.txt"):
    bg="#800080"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#800080"
    a_button_bg="#800080"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp/settings/theme/10.txt"):
    bg="#FFC0CB"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFC0CB"
    a_button_bg="#FFC0CB"
    a_button_fg="#000000"
else:
    def theme_open():
        if os.path.isfile("/usr/local/bin/metterxp/settings/lang/en.txt"):
            messagebox.showwarning("Warning","Can't found theme config. When you click 'OK' MetterXP settings will open.")
        elif os.path.isfile("/usr/local/bin/metterxp/settings/lang/tr.txt"):
            messagebox.showwarning("Uyarı","Tema yapılandırması bulunamadı, MetterXP ayarları 'OK' tuşuna bastığınızda açılacaktır.")
        os.system("pkexec /usr/bin/metterxp mxp_options")
        exit()
    if os.path.isfile(debian):
        theme_open()
    elif os.path.isfile(fedora):
        theme_open()
    elif os.path.isfile(solus):
        theme_open()

def metterxp():
    if os.path.isfile(lang_en):
        if os.getuid() == 0:
            messagebox.showerror("Error","Links cannot be opened while rooted.")
        if not os.getuid() == 0:
            os.system("xdg-open https://mukonqi.github.io/metterxp/en/index.html")
    elif os.path.isfile(lang_tr):
        if os.getuid() == 0:
            messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
        if not os.getuid() == 0:
            os.system("xdg-open https://mukonqi.github.io/metterxp/tr/index.html")
def foss():
    if os.path.isfile(lang_en):
        if os.getuid() == 0:
            messagebox.showerror("Error","Links cannot be opened while rooted.")
    elif os.path.isfile(lang_tr):
        if os.getuid() == 0:
            messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
    if not os.getuid() == 0:
        os.system("xdg-open https://www.gnu.org/philosophy/free-sw.tr.html")
def developer():
    if os.path.isfile(lang_en):
        if os.getuid() == 0:
            messagebox.showerror("Error","Links cannot be opened while rooted.")
        if not os.getuid() == 0:
            os.system("xdg-open https://github.com/MuKonqi")
    elif os.path.isfile(lang_tr):
        if os.getuid() == 0:
            messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
        if not os.getuid() == 0:
            os.system("xdg-open https://mukonqi.github.io")
def license():
    if os.path.isfile(lang_en):
        if os.getuid() == 0:
            messagebox.showerror("Error","Links cannot be opened while rooted.")
    elif os.path.isfile(lang_tr):
        if os.getuid() == 0:
            messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
    if not os.getuid() == 0:
        os.system("xdg-open https://www.gnu.org/licenses/gpl-3.0-standalone.html")
def base():
    if os.path.isfile(lang_en):
        if os.getuid() == 0:
            messagebox.showerror("Error","Links cannot be opened while rooted.")
    elif os.path.isfile(lang_tr):
        if os.getuid() == 0:
            messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
    if not os.getuid() == 0:
        os.system("xdg-open https://github.com/MuKonqi/metterxp/tree/betterxp")
def version():
    if os.path.isfile(lang_en):
        if os.getuid() == 0:
            messagebox.showerror("Error","Links cannot be opened while rooted.")
        if not os.getuid() == 0:
            os.system("xdg-open https://mukonqi.github.io/metterxp/en/change-log.html")
    elif os.path.isfile(lang_tr):
        if os.getuid() == 0:
            messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
        if not os.getuid() == 0:
            os.system("xdg-open https://mukonqi.github.io/metterxp/tr/change-log.html")

out=0
v=open("/usr/local/bin/metterxp/version.txt", "r")
vr=v.read()
v.close()
window=Tk()
window.config(background=bg)
window.resizable(0, 0)
window.geometry("600x600")
parent = Frame(window)
parent.pack(expand=1)
space1=Label(parent, background=bg, foreground=fg, text="\n", font="arial 7") 
if os.path.isfile(lang_en):
    window.title("About | MetterXP")
    button1=Button(parent, font="arial 15 bold italic", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="MetterXP\nDesigned for maximum and better experience.", command=metterxp)
    space2=Label(parent, background=bg, foreground=fg, text="\n", font="arial 1")
    button2=Button(parent, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Version: "+vr, command=version)
    if beta == "no":
        vl = subprocess.Popen("curl https://raw.githubusercontent.com/MuKonqi/metterxp/main/app/version.txt", shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = vl.communicate()
        if out != vr:
            buttonl=Button(parent, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Latest Version: "+out, command=version)
        elif out == vr:
            out=0   
    elif beta == "yes":
        vlb = subprocess.Popen("curl https://raw.githubusercontent.com/MuKonqi/metterxp/beta/app/version.txt", shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = vlb.communicate()
        if out != vr:
            buttonl=Button(parent, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Latest Pre-Release: "+out, command=version)
        elif out == vr:
            out=0
    button3=Button(parent, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Base: BetterXP 2.0.3-2, Terminalden kurtulun 2.0", command=base)
    button4=Button(parent, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="License: GNU General Public License, Version 3.0 (GPLv3)", command=license)
    button5=Button(parent, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Coding type: Free and Open Source Software (FOSS)", command=foss)
    button6=Button(parent, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Developer: MuKonqi (Muhammed Abdurrahman)", command=developer)
elif os.path.isfile(lang_tr):
    window.title("Hakkında | MetterXP")
    button1=Button(parent, font="arial 15 bold italic", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="MetterXP\nMaksimum ve daha iyi deneyim için tasarlandı.", command=metterxp)
    space2=Label(parent, background=bg, foreground=fg, text="\n", font="arial 1")
    button2=Button(parent, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Sürüm: "+vr, command=version)
    if beta == "no":
        vl = subprocess.Popen("curl https://raw.githubusercontent.com/MuKonqi/metterxp/main/app/version.txt", shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = vl.communicate()
        if out != vr:
            buttonl=Button(parent, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Son Sürüm: "+out, command=version)
        elif out == vr:
            out=0   
    elif beta == "yes":
        vlb = subprocess.Popen("curl https://raw.githubusercontent.com/MuKonqi/metterxp/beta/app/version.txt", shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = vlb.communicate()
        if out != vr:
            buttonl=Button(parent, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Son Ön Sürüm: "+out, command=version)
        elif out == vr:
            out=0
    button3=Button(parent, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Temel: BetterXP 2.0.3-2, Terminalden kurtulun 2.0", command=base)
    button4=Button(parent, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Lisans: GNU General Public License, Version 3.0 (GPLv3)", command=license)
    button5=Button(parent, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Kodlanma türü: Özgür ve Açık Kaynaklı Yazılım (FOSS)", command=foss)
    button6=Button(parent, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Geliştirici: MuKonqi (Muhammed Abdurrahman)", command=developer)
space1.pack(fill="x")
button1.pack(fill="x")
space2.pack(fill="x")
button2.pack(fill="x")
if out != 0:
    buttonl.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
button5.pack(fill="x")
button6.pack(fill="x")
mainloop()