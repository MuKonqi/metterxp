#!/usr/bin/env python3

# Copyright (C) 2021, 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

beta="no"

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

if not os.path.isdir("/home/"+username+"/.by-mukonqi/metterxp/"):
    os.system("python3 /usr/local/bin/metterxp/modules/mxp_options.py")
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
if os.path.isfile(t+"2011.txt"):
    bg="#9e9c9d"
    fg="#e3af79"
    button_bg="#d2d1d2"
    button_fg="#3a1212"
    a_button_bg="#0b75aa"
    a_button_fg="#FFFFFF"    
elif os.path.isfile(t+"2021.txt"):
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
elif os.path.isfile(t+"23Q2.txt"):
    bg="#2f2f2f"
    fg="#FFFFFF"
    button_bg="#bf2422"
    button_fg="#2f2f2f"
    a_button_bg="#5dc305"
    a_button_fg="#376296"
elif os.path.isfile(t+"23H2.txt"):
    bg="#2f2f2f"
    fg="#376296"
    button_bg="#a9a9a9"
    button_fg="#000000"
    a_button_bg="#376296"
    a_button_fg="#FFFFFF"
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
elif os.path.isfile(t+"theme.txt"):
    bgo=open(t+"bg.txt", "r")
    bgr="#"+bgo.read()
    bgo.close()
    bg=bgr.replace("\n","") 
    fgo=open(t+"fg.txt", "r")
    fgr="#"+fgo.read()
    fgo.close()
    fg=fgr.replace("\n","")
    bbgo=open(t+"button_bg.txt", "r")
    button_bgr="#"+bbgo.read()
    bbgo.close()
    button_bg=button_bgr.replace("\n","")
    bfgo=open(t+"button_fg.txt", "r")
    button_fgr="#"+bfgo.read()
    bfgo.close()
    button_fg=button_fgr.replace("\n","")
    abbgo=open(t+"a_button_bg.txt", "r")
    a_button_bgr="#"+abbgo.read()
    abbgo.close()
    a_button_bg=a_button_bgr.replace("\n","")
    abfgo=open(t+"a_button_fg.txt", "r")
    a_button_fgr="#"+abfgo.read()
    abfgo.close()
    a_button_fg=a_button_fgr.replace("\n","")
else:
    os.system("python3 /usr/local/bin/metterxp/modules/mxp_options.py")
    exit()

def metterxp():
    os.system("xdg-open https://github.com/MuKonqi/metterxp/wiki/")
def foss():
    os.system("xdg-open https://www.gnu.org/philosophy/free-sw.html")
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
    vwindow=Tk(className="MetterXP")
    vwindow.config(background=bg)
    vwindow.resizable(0, 0)
    if os.path.isfile(en):
        vwindow.title(vr+" - About | MetterXP")
        vlabel1=Label(vwindow, background=bg, foreground=fg, text="\nListed below are the things that have changed in the "+vr+" version compared to the old version:\n", font="arial 12 bold italic")
        ch=open("/usr/local/bin/metterxp/changelog-en.txt", "r")
        chr=ch.read()
        ch.close()
    elif os.path.isfile(tr):
        vwindow.title(vr+" - Hakkında | MetterXP")
        vlabel1=Label(vwindow, background=bg, foreground=fg, text="\nAşağıda "+vr+" sürümünde eski sürüme göre değişen şeyler listelenmiştir:\n", font="arial 12 bold italic")
        ch=open("/usr/local/bin/metterxp/changelog-tr.txt", "r")
        chr=ch.read()
        ch.close()
    vscroll=Scrollbar(vwindow)
    vtext1=Text(vwindow, font="arial 11 bold italic", yscrollcommand=vscroll.set)
    vtext1.insert(END, chr)
    vtext1.config(state=DISABLED)
    vscroll.config(command=vtext1.yview)
    vlabel1.pack(fill="x")
    vscroll.pack(side=RIGHT,fill=Y)
    vtext1.pack(fill="x")

v=open("/usr/local/bin/metterxp/version.txt", "r")
vr=v.read()
v.close()
window=Tk(className="MetterXP")
window.config(background=bg)
window.resizable(0, 0)
window.geometry("600x365")
parent = Frame(window)
parent.pack(expand=1)
icon = PhotoImage(file="/usr/local/bin/metterxp/icon.png")
window.iconphoto(True, icon)
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