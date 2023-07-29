#!/usr/bin/env python3

# Copyright (C) 2021, 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

beta="yes"

from tkinter import *
from tkinter import messagebox
import os
import subprocess
from subprocess import *
import getpass

username=getpass.getuser()
t="/home/"+username+"/.by-mukonqi/metterxp/theme/"
en="/home/"+username+"/.by-mukonqi/metterxp/language/en.txt"
tr="/home/"+username+"/.by-mukonqi/metterxp/language/tr.txt"
debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if not os.path.isdir("/home/"+username+"/.by-mukonqi/metterxp/"):
    messagebox.showerror("User Error - Fatal | MetterXP","Please start only MetterXP (just select MetterXP in the applications section or type metterxp) to set up language and theme preferences.")
    exit()

if os.getuid() == 0:
    if os.path.isfile(en):
        messagebox.showerror("Error","Root can't run this module!")
    elif os.path.isfile(tr):
        messagebox.showerror("Hata","Kök kullanıcı bu modülü çalıştıramaz!")
    exit()

bg=""
fg=""
button_bg=""
button_fg=""
a_button_bg=""
a_button_fg=""
if os.path.isfile(t+"2021.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#03035B"
    a_button_fg="#FFFFFF"
elif os.path.isfile(t+"2022.txt"):
    bg="#a9a9a9"
    fg="#376296"
    button_bg="#FFFFFF"
    button_fg="#376296"
    a_button_bg="#376296"
    a_button_fg="#FFFFFF"
elif os.path.isfile(t+"modern.txt"):
    bg="#2f2f2f"
    fg="#376296"
    button_bg="#a9a9a9"
    button_fg="#000000"
    a_button_bg="#376296"
    a_button_fg="#FFFFFF"
elif os.path.isfile(t+"machine.txt"):
    bg="#2f2f2f"
    fg="#FFFFFF"
    button_bg="#bf2422"
    button_fg="#2f2f2f"
    a_button_bg="#5dc305"
    a_button_fg="#376296"
elif os.path.isfile(t+"black.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
elif os.path.isfile(t+"white.txt"):
    bg="#FFFFFF"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFFFF"
    a_button_bg="#FFFFFF"
    a_button_fg="#000000"
elif os.path.isfile(t+"gray.txt"):
    bg="#a9a9a9"
    fg="#000000"
    button_bg="#000000"
    button_fg="#a9a9a9"
    a_button_bg="#a9a9a9"
    a_button_fg="#000000"  
elif os.path.isfile(t+"red.txt"):
    bg="#FF0000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#FF0000"
    a_button_bg="#FF0000"
    a_button_fg="#FFFFFF"
elif os.path.isfile(t+"yellow.txt"):
    bg="#FFFF00"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFF00"
    a_button_bg="#FFFF00"
    a_button_fg="#000000"    
elif os.path.isfile(t+"green.txt"):
    bg="#008000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#008000"
    a_button_bg="#008000"
    a_button_fg="#FFFFFF"
elif os.path.isfile(t+"blue.txt"):
    bg="#0000FF"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#0000FF"
    a_button_bg="#0000FF"
    a_button_fg="#FFFFFF"    
elif os.path.isfile(t+"navy-blue.txt"):
    bg="#000080"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000080"
    a_button_bg="#000080"
    a_button_fg="#FFFFFF"      
elif os.path.isfile(t+"purple.txt"):
    bg="#800080"
    fg="#000000"
    button_bg="#000000"
    button_fg="#800080"
    a_button_bg="#800080"
    a_button_fg="#000000"
elif os.path.isfile(t+"lilac.txt"):
    bg="#C8A2C8"
    fg="#000000"
    button_bg="#000000"
    button_fg="#C8A2C8"
    a_button_bg="#C8A2C8"
    a_button_fg="#000000"
elif os.path.isfile(t+"pink.txt"):
    bg="#FFC0CB"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFC0CB"
    a_button_bg="#FFC0CB"
    a_button_fg="#000000"  
elif os.path.isfile(t+"complex_atno.txt"):
    bg="#474747"
    fg="#00252e"
    button_bg="#012547"
    button_fg="#8c0606"
    a_button_bg="#034d96"
    a_button_fg="#a4d46a"  
else:
    os.system("python3 /usr/local/bin/metterxp/modules/mxp_options.py")
    exit()

def metterxp():
    if os.path.isfile(en):
        os.system("xdg-open https://mukonqi.github.io/metterxp/tr/index.html")
    elif os.path.isfile(tr):
        os.system("xdg-open https://mukonqi.github.io/metterxp/tr/index.html")
def foss():
    os.system("xdg-open https://www.gnu.org/philosophy/free-sw.tr.html")
def developer():
    if os.path.isfile(en):
        os.system("xdg-open https://github.com/MuKonqi")
    elif os.path.isfile(tr):
        os.system("xdg-open https://mukonqi.github.io")
def license():
    os.system("xdg-open https://www.gnu.org/licenses/gpl-3.0-standalone.html")
def base():
    os.system("xdg-open https://github.com/MuKonqi/metterxp/tree/betterxp")
def version():
    if os.path.isfile(en):
        os.system("xdg-open https://mukonqi.github.io/metterxp/en/change-log.html")
    elif os.path.isfile(tr):
        os.system("xdg-open https://mukonqi.github.io/metterxp/tr/change-log.html")

v=open("/usr/local/bin/metterxp/version.txt", "r")
vr=v.read()
v.close()
window=Tk()
window.config(background=bg)
window.resizable(0, 0)
window.geometry("600x365")
parent = Frame(window)
parent.pack(expand=1)
space1=Label(parent, background=bg, foreground=fg, text="\n", font="arial 4")
if os.path.isfile(en):
    window.title("About | MetterXP")
    button1=Button(parent, font="arial 20 bold italic", cursor="hand2", activeforeground=button_fg, activebackground=button_bg, background=bg, foreground=fg, borderwidth="0",  highlightthickness="0", text="MetterXP\nAdvanced tool box.", command=metterxp)
    space2=Label(parent, background=bg, foreground=fg, text="\n", font="arial 4")
    button2=Button(parent, font="arial 16 bold", cursor="hand2", activeforeground=button_fg, activebackground=button_bg, background=bg, foreground=fg, borderwidth="0",  highlightthickness="0", text="Version: "+vr, command=version)
    if beta == "no":
        vl = subprocess.Popen("curl https://raw.githubusercontent.com/MuKonqi/metterxp/main/app/version.txt", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = vl.communicate()
        if out != vr:
            button2.config(text="Version: "+vr+"\nLatest Version: "+out)
    elif beta == "yes":
        vlb = subprocess.Popen("curl https://raw.githubusercontent.com/MuKonqi/metterxp/beta/app/version.txt", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = vlb.communicate()
        if out != vr:
            button2.config(text="Version: "+vr+"\nLatest Pre-Version: "+out)
    button3=Button(parent, font="arial 16 bold", cursor="hand2", activeforeground=button_fg, activebackground=button_bg, background=bg, foreground=fg, borderwidth="0",  highlightthickness="0", text="Base: BetterXP 2.0.3-2, Terminalden kurtulun 2.0", command=base)
    button4=Button(parent, font="arial 16 bold", cursor="hand2", activeforeground=button_fg, activebackground=button_bg, background=bg, foreground=fg, borderwidth="0",  highlightthickness="0", text="License: GNU General Public License, Version 3.0", command=license)
    button5=Button(parent, font="arial 16 bold", cursor="hand2", activeforeground=button_fg, activebackground=button_bg, background=bg, foreground=fg, borderwidth="0",  highlightthickness="0", text="Type: Free and Open Source Software", command=foss)
    button6=Button(parent, font="arial 16 bold", cursor="hand2", activeforeground=button_fg, activebackground=button_bg, background=bg, foreground=fg, borderwidth="0",  highlightthickness="0", text="Developer: MuKonqi (Muhammed Abdurrahman)", command=developer)
elif os.path.isfile(tr):
    window.title("Hakkında | MetterXP")
    button1=Button(parent, font="arial 20 bold italic", cursor="hand2", activeforeground=button_fg, activebackground=button_bg, background=bg, foreground=fg, borderwidth="0",  highlightthickness="0", text="MetterXP\nGelişmiş araç kutusu.", command=metterxp)
    space2=Label(parent, background=bg, foreground=fg, text="\n", font="arial 4")
    button2=Button(parent, font="arial 16 bold", cursor="hand2", activeforeground=button_fg, activebackground=button_bg, background=bg, foreground=fg, borderwidth="0",  highlightthickness="0", text="Sürüm: "+vr, command=version)
    if beta == "no":
        vl = subprocess.Popen("curl https://raw.githubusercontent.com/MuKonqi/metterxp/main/app/version.txt", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = vl.communicate()
        if out != vr:
            button2.config(text="Sürüm: "+vr+"\nSon Sürüm: "+out)
    elif beta == "yes":
        vlb = subprocess.Popen("curl https://raw.githubusercontent.com/MuKonqi/metterxp/beta/app/version.txt", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = vlb.communicate()
        if out != vr:
            button2.config(text="Sürüm: "+vr+"\nSon Ön Sürüm: "+out)
    button3=Button(parent, font="arial 16 bold", cursor="hand2", activeforeground=button_fg, activebackground=button_bg, background=bg, foreground=fg, borderwidth="0",  highlightthickness="0", text="Temel: BetterXP 2.0.3-2, Terminalden kurtulun 2.0", command=base)
    button4=Button(parent, font="arial 16 bold", cursor="hand2", activeforeground=button_fg, activebackground=button_bg, background=bg, foreground=fg, borderwidth="0",  highlightthickness="0", text="Lisans: GNU General Public License, Version 3.0", command=license)
    button5=Button(parent, font="arial 16 bold", cursor="hand2", activeforeground=button_fg, activebackground=button_bg, background=bg, foreground=fg, borderwidth="0",  highlightthickness="0", text="Tür: Özgür ve Açık Kaynaklı Yazılım", command=foss)
    button6=Button(parent, font="arial 16 bold", cursor="hand2", activeforeground=button_fg, activebackground=button_bg, background=bg, foreground=fg, borderwidth="0",  highlightthickness="0", text="Geliştirici: MuKonqi (Muhammed Abdurrahman)", command=developer)
space1.pack(fill="x")
button1.pack(fill="x")
space2.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
button5.pack(fill="x")
button6.pack(fill="x")
space3=Label(parent, background=bg, foreground=fg, text="\n", font="arial 4")
space3.pack(fill="x")
mainloop()
