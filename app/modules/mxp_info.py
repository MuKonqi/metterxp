#!/usr/bin/env python3

# Copyright (C) 2021, 2022 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp/settings/lang/en.txt"

def module_exit():
    print("\nModül kapatılıyor...\nClosing this module...")
    exit()

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
        os.system("xdg-open https://mukonqi.github.io/metterxp/en/index.html")
    elif os.path.isfile(lang_tr):
        os.system("xdg-open https://mukonqi.github.io/metterxp/tr/index.html")
def foss():
    os.system("xdg-open https://www.gnu.org/philosophy/free-sw.tr.html")
def developer():
    os.system("xdg-open https://mukonqi.github.io")
def license():
    os.system("xdg-open https://www.gnu.org/licenses/gpl-3.0-standalone.html")
def base():
    os.system("xdg-open https://github.com/MuKonqi/metterxp/tree/betterxp")
def version():
    if os.path.isfile(lang_en):
        os.system("xdg-open https://mukonqi.github.io/metterxp/en/whats-new.html")
    elif os.path.isfile(lang_tr):
        os.system("xdg-open https://mukonqi.github.io/metterxp/tr/whats-new.html")

if os.path.isfile(lang_en):
    window=Tk()
    window.title("About MetterXP | MetterXP")
    window.config(background=bg)
    window.resizable(0, 0)
    space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 7") 
    button1=Button(window, font="arial 15 bold italic", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="MetterXP\nDesigned for maximum and better experience.", command=metterxp)
    space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
    button2=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Version: 2.0.0", command=version)
    button3=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Base: BetterXP 2.0.3-2, Terminalden kurtulun 2.0", command=base)
    button4=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="License: GNU General Public License, Version 3.0 (GPLv3)", command=license)
    button5=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="License type: Free and Open Source Software (FOSS)", command=foss)
    button6=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Developer: Muhammed Abdurrahman", command=developer)
    space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    button_1=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, text="Close this module\nBack to main menu", command=module_exit)
elif os.path.isfile(lang_tr):
    window=Tk()
    window.title("MetterXP hakkında | MetterXP")
    window.config(background=bg)
    window.resizable(0, 0)
    space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 7") 
    button1=Button(window, font="arial 15 bold italic", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="MetterXP\nMaksimum ve daha iyi deneyim için tasarlandı.", command=metterxp)
    space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
    button2=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Sürüm: 2.0.0", command=version)
    button3=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Temel: BetterXP 2.0.3-2, Terminalden kurtulun 2.0", command=base)
    button4=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Lisans: GNU General Public License, Version 3.0 (GPLv3)", command=license)
    button5=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Lisans türü: Özgür ve Açık Kaynaklı Yazılım (FOSS)", command=foss)
    button6=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Geliştirici: Muhammed Abdurrahman", command=developer)
    space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    button_1=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, text="Modülü kapat\nAna menüye dön", command=module_exit)
space1.pack()
button1.pack()
space2.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
space3.pack()
button_1.pack()
mainloop()