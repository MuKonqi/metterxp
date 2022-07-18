#!/usr/bin/env python3

# Copyright (C) 2021, 2022 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os
import subprocess

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp/settings/lang/en.txt"


def module_exit():
    print("\nModül kapatılıyor...\nClosing this module...")
    exit()
def reopen():
    print("\nModül yeniden başlatılıyor...\nRestarting this module...")
    window.destroy()
    os.system("pkexec python3 /usr/local/bin/metterxp/modules/app_it_rm.py")

if not os.getuid() == 0:
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Only root can run this module!")
        exit("Only root can run this module!\nClosing this module...")
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


window=Tk()
if os.path.isfile(lang_en):
    window.title("Open applications with root user | MetterXP")
elif os.path.isfile(lang_tr):
    window.title("Uygulamaları kök haklarıyla aç | MetterXP")
window.config(background=bg)
window.resizable(0, 0)

def nautilus():
    subprocess.Popen("nautilus", shell=True)
def nemo():
    subprocess.Popen("nemo", shell=True)
def caja():
    subprocess.Popen("caja", shell=True)
def thunar():
    subprocess.Popen("thunar", shell=True)
def pcmanfmqt():
    subprocess.Popen("pcmanfm-qt", shell=True)
def custom():
    subprocess.Popen(appname.get(), shell=True)

if os.path.isfile(lang_en):
    text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Which app would you like to open with root rights?")
    space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    button1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Nautilus file manager\n(Comess with GNOME, Budgie desktop environments)", command=nautilus)
    button2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Nemo file manager\n(Comes with Cinnamon desktop environment)", command=nemo)
    button3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Caja file manager\n(Comes with Mate desktop environment)", command=caja)
    button4=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Thunar file manager\n(Comes with Xfce desktop environment)", command=thunar)
    button5=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="PCmanFM-Qt file manager\n(Comes with LXQt desktop environment)", command=pcmanfmqt)
    space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    text2=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="When you enter a program with a graphical interface below, it will open with root rights.\nFor example: konsole, gedit")
    space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    appname=Entry(window)
    button6=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Start the application I named", command=custom)
    space4=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    button_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu ", command=module_exit)
elif os.path.isfile(lang_tr):
    text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Hangi uygulamayı kök haklarıyla açmak istersiniz?")
    space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    button1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Nautilus dosya yöneticisi\n(GNOME, Budgie masaüstü ortamlarıyla gelir)", command=nautilus)
    button2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Nemo dosya yöneticisi\n(Cinnamon masaüstü ortamıyla gelir)", command=nemo)
    button3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Caja dosya yöneticisi\n(Mate masaüstü ortamıyla gelir)", command=caja)
    button4=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Thunar dosya yöneticisi\n(Xfce masaüstü ortamıyla gelir)", command=thunar)
    button5=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="PCmanFM-Qt dosya yöneticisi\n(LXQt masaüstü ortamıyla gelir)", command=pcmanfmqt)
    space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")    
    text2=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Aşağıya grafik arayüze sahip bir program girdiğinizde, o kök haklarıyla açılacaktır.\nÖrneğin: konsole, gedit")
    space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")    
    appname=Entry(window)
    button6=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Adını yazdığım uygulamayı başlat", command=custom)
    space4=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    button_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
text1.pack()
space1.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
space2.pack()
text2.pack()
space3.pack()
appname.pack()
button6.pack()
space4.pack()
button_1.pack()
button_1.pack()

mainloop()