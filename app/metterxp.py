#!/usr/bin/env python3

# Copyright (C) 2021, 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# MetterXP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# MetterXP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with MetterXP.  If not, see <https://www.gnu.org/licenses/>.

from tkinter import *
from tkinter import messagebox
from subprocess import *
import subprocess
import os
import sys
from sys import platform
import getpass
username=getpass.getuser()

t="/home/"+username+"/.by-mukonqi/metterxp/theme/"
p=0

en="/home/"+username+"/.by-mukonqi/metterxp/language/en.txt"
tr="/home/"+username+"/.by-mukonqi/metterxp/language/tr.txt"

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

args=sys.argv[1:]

def mxp_about():
    subprocess.Popen("python3 /usr/local/bin/metterxp/modules/mxp_about.py", shell=True)
def mxp_options():
    subprocess.Popen("python3 /usr/local/bin/metterxp/modules/mxp_options.py", shell=True)
def mxp_update():
    os.system("pkexec /usr/bin/metterxp mxp_update "+username)
    exit()
def mxp_reset():
    os.system("pkexec /usr/bin/metterxp mxp_reset "+username)
    exit()
def mxp_uninstall():
    os.system("pkexec /usr/bin/metterxp mxp_uninstall "+username)
    exit()
def app_store():
    subprocess.Popen("pkexec /usr/bin/metterxp app_store "+username, shell=True)
def dewm_store():
    subprocess.Popen("pkexec /usr/bin/metterxp dewm_store "+username, shell=True)
def pm_store():
    subprocess.Popen("pkexec /usr/bin/metterxp pm_store "+username, shell=True)
def app_configure():
    subprocess.Popen("pkexec /usr/bin/metterxp app_configure "+username, shell=True)
def bashrc_config():
    subprocess.Popen("python3 /usr/local/bin/metterxp/modules/bashrc_config.py", shell=True)
def fm_open():
    subprocess.Popen("pkexec /usr/bin/metterxp fm_open "+username, shell=True)
def distros():
    subprocess.Popen("python3 /usr/local/bin/metterxp/modules/distros.py", shell=True)
def system_up():
    subprocess.Popen("pkexec /usr/bin/metterxp system_up "+username, shell=True)
def clear_cache_app():
    subprocess.Popen("pkexec /usr/bin/metterxp clear_cache_app "+username, shell=True)
def fixer():
    subprocess.Popen("pkexec /usr/bin/metterxp fixer "+username, shell=True)
    
if not "mxp_options" in args:
    if username != "root" and not os.path.isdir("/home/"+username+"/.by-mukonqi/metterxp/"):
        if os.path.isfile(debian) or os.path.isfile(fedora) or os.path.isfile(solus):
            mxp_options()
            exit()

if len(sys.argv) > 2:
    if str(sys.argv[2]) == "p":
        p=1
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
elif username != "root" and not os.path.isdir(t):
    mxp_options()
    exit()

if "2011" in args:
    bg="#9e9c9d"
    fg="#e3af79"
    button_bg="#d2d1d2"
    button_fg="#3a1212"
    a_button_bg="#0b75aa"
    a_button_fg="#FFFFFF"    
elif "2021" in args:
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#03035B"
    a_button_fg="#FFFFFF"
elif "2022" in args:
    bg="#a9a9a9"
    fg="#376296"
    button_bg="#FFFFFF"
    button_fg="#376296"
    a_button_bg="#376296"
    a_button_fg="#FFFFFF"
elif "23Q2" in args:
    bg="#2f2f2f"
    fg="#FFFFFF"
    button_bg="#bf2422"
    button_fg="#2f2f2f"
    a_button_bg="#5dc305"
    a_button_fg="#376296"
elif "23H2" in args:
    bg="#2f2f2f"
    fg="#376296"
    button_bg="#a9a9a9"
    button_fg="#000000"
    a_button_bg="#376296"
    a_button_fg="#FFFFFF"
elif "black" in args:
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
elif "white" in args:
    bg="#FFFFFF"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFFFF"
    a_button_bg="#FFFFFF"
    a_button_fg="#000000"
elif "gray" in args:
    bg="#a9a9a9"
    fg="#000000"
    button_bg="#000000"
    button_fg="#a9a9a9"
    a_button_bg="#a9a9a9"
    a_button_fg="#000000"  
elif "red" in args:
    bg="#FF0000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#FF0000"
    a_button_bg="#FF0000"
    a_button_fg="#FFFFFF"
elif "yellow" in args:
    bg="#FFFF00"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFF00"
    a_button_bg="#FFFF00"
    a_button_fg="#000000"    
elif "green" in args:
    bg="#008000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#008000"
    a_button_bg="#008000"
    a_button_fg="#FFFFFF"
elif "blue" in args:
    bg="#0000FF"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#0000FF"
    a_button_bg="#0000FF"
    a_button_fg="#FFFFFF"    
elif "navy-blue" in args:
    bg="#000080"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000080"
    a_button_bg="#000080"
    a_button_fg="#FFFFFF"      
elif "purple" in args:
    bg="#800080"
    fg="#000000"
    button_bg="#000000"
    button_fg="#800080"
    a_button_bg="#800080"
    a_button_fg="#000000"
elif "lilac" in args:
    bg="#C8A2C8"
    fg="#000000"
    button_bg="#000000"
    button_fg="#C8A2C8"
    a_button_bg="#C8A2C8"
    a_button_fg="#000000"
elif "pink" in args:
    bg="#FFC0CB"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFC0CB"
    a_button_bg="#FFC0CB"
    a_button_fg="#000000"
elif "complex_atno" in args:
    bg="#474747"
    fg="#00252e"
    button_bg="#012547"
    button_fg="#8c0606"
    a_button_bg="#034d96"
    a_button_fg="#a4d46a"
elif "ct" in args:
    bg="#"+str(sys.argv[3])
    fg="#"+str(sys.argv[4])
    button_bg="#"+str(sys.argv[5])
    button_fg="#"+str(sys.argv[6])
    a_button_bg="#"+str(sys.argv[7])
    a_button_fg="#"+str(sys.argv[8])

def main_gui():   
    def apply():
        def applied():
            if os.path.isfile(en):
                messagebox.showinfo("Information","Theme applied.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Tema uygulandı.")
            spacep1.destroy()
            buttonp.destroy()
            spacep2.destroy()
        if str(sys.argv[1]) != "ct":
            os.system("cd "+t+" ; rm * ; touch "+str(sys.argv[1])+".txt")
            if os.path.isfile(t+str(sys.argv[1])+".txt"):
                applied()
        elif str(sys.argv[1]) == "ct":
            os.system("cd "+t+" ; rm * ; touch theme.txt")
            os.system("cd "+t+" ; echo "+str(sys.argv[3])+" >> bg.txt")
            os.system("cd "+t+" ; echo "+str(sys.argv[4])+" >> fg.txt")
            os.system("cd "+t+" ; echo "+str(sys.argv[5])+" >> button_bg.txt")
            os.system("cd "+t+" ; echo "+str(sys.argv[6])+" >> button_fg.txt")
            os.system("cd "+t+" ; echo "+str(sys.argv[7])+" >> a_button_bg.txt")
            os.system("cd "+t+" ; echo "+str(sys.argv[8])+" >> a_button_fg.txt")
            applied()
    
    if os.getuid() == 0:
        if os.path.isfile(en):
                messagebox.showwarning("Fatal Request","You started MetterXP as root but MetterXP main page don't support it. Also MetterXP already requests root rights when it needs root rights.")
        elif os.path.isfile(tr):
                messagebox.showinfo("Ölümcül İstek","MetterXP'ı kök olarak başlattınız ama MetterXP ana sayfası bunu desteklemez. Ayrıca MetterXP, kök haklarına ihtiyaç duyduğunda zaten kök haklarını ister.")
        exit()

    window=Tk(className="MetterXP")
    window.config(background=bg)
    window.resizable(0, 0)
    window.geometry("483x571")
    icon = PhotoImage(file="/usr/local/bin/metterxp/icon.png")
    window.iconphoto(True, icon)
    parent = Frame(window)
    
    def update():
        window.destroy()
        mxp_update()
    def reset():
        window.destroy()
        mxp_reset()
    def uninstall():
        window.destroy()
        mxp_uninstall()

    if os.path.isfile(en):
        window.title("Hello "+username+"! • MetterXP")
        menu1=Menu(window)
        window.config(menu=menu1)
        m_options=Menu(menu1, tearoff=0)
        menu1.add_cascade(label="File",menu=m_options)
        m_options.add_command(label="About",command=mxp_about)
        m_options.add_command(label="Options",command=mxp_options)
        m_options.add_command(label="Update",command=update)
        m_options.add_command(label="Reset",command=reset)
        m_options.add_command(label="Uninstall",command=uninstall)
        open_m=Menu(menu1, tearoff=0)
        menu1.add_cascade(label="Open",menu=open_m)
        open_m.add_command(label="Application store", command=app_store)
        open_m.add_command(label="Desktop Environment and Window Manager store", command=dewm_store)
        open_m.add_command(label="Package manager store", command=pm_store)
        open_m.add_command(label="Configuring softwares", command=app_configure)
        open_m.add_command(label="Configuring .bashrc file", command=bashrc_config)
        open_m.add_command(label="Opening file managers", command=fm_open)
        open_m.add_command(label="Inform about some GNU/Linux distributions", command=distros)
        open_m.add_command(label="Update system", command=system_up)
        open_m.add_command(label="Clear cache and/or unnecessary packages", command=clear_cache_app)
        if os.path.isfile(debian):
            open_m.add_command(label="Solve package errors", command=fixer)
        
        if p == 1:
            spacep1=Label(window, background=bg, foreground=fg, font="arial 4", text="\n")
            buttonp=Button(window, text="APPLY THIS THEME", command=apply, font="arial 12 bold", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="4")
            spacep2=Label(window, background=bg, foreground=fg, font="arial 4", text="\n")

        text1=Label(window, background=bg, foreground=fg, font="arial 11 bold italic", text="Please select the action you want to take.")
        space1=Label(parent, background=bg, foreground=fg, font="arial 3", text="\n")
        button1=Button(parent, text="Application store", command=app_store, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")
        button2=Button(parent, text="Desktop Environment and Window Manager store", command=dewm_store, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")
        button3=Button(parent, text="Package manager store", command=pm_store, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")               
        button4=Button(parent, text="Configuring softwares", command=app_configure, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")       
        button5=Button(parent, text="Configuring .bashrc file", command=bashrc_config, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")        
        button6=Button(parent, text="Opening file managers", command=fm_open, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")        
        button7=Button(parent, text="Inform about some GNU/Linux distributions", command=distros, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")        
        button8=Button(parent, text="Update system", command=system_up, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")        
        button9=Button(parent, text="Clear cache and/or unnecessary packages", command=clear_cache_app, font="arial 11 bold", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg , borderwidth="5")
        if os.path.isfile(debian):
            button10=Button(parent, text="Solve package errors", command=fixer, font="arial 11 bold", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="5")
    elif os.path.isfile(tr):
        window.title("Merhabalar "+username+"! • MetterXP")
        menu1=Menu(window)
        window.config(menu=menu1)
        m_options=Menu(menu1, tearoff=0)
        menu1.add_cascade(label="Dosya",menu=m_options)
        m_options.add_command(label="Hakkında",command=mxp_about)
        m_options.add_command(label="Seçenekler",command=mxp_options)
        m_options.add_command(label="Güncelle",command=update)
        m_options.add_command(label="Sıfırla",command=reset)
        m_options.add_command(label="Kaldır",command=uninstall)
        open_m=Menu(menu1, tearoff=0)
        menu1.add_cascade(label="Aç",menu=open_m)
        open_m.add_command(label="Uygulama mağazası", command=app_store)
        open_m.add_command(label="Masaüstü Ortamı ve Pencere Yöneticisi mağazası", command=dewm_store)
        open_m.add_command(label="Paket yöneticisi mağazası", command=pm_store)
        open_m.add_command(label="Programları yapılandırma", command=app_configure)
        open_m.add_command(label=".bashrc dosyası yapılandırma", command=bashrc_config)
        open_m.add_command(label="Dosya yöneticilerini kök kullanıcı haklarıyla açma", command=fm_open)
        open_m.add_command(label="Bazı GNU/Linux dağıtımları hakkında bilgi verme", command=distros)
        open_m.add_command(label="Sistemi güncelle", command=system_up)
        open_m.add_command(label="Önbelleği ve/veya gereksiz paketleri temizle", command=clear_cache_app)
        if os.path.isfile(debian):
            open_m.add_command(label="Paket hatalarını çöz", command=fixer)
        
        if p == 1:
            spacep1=Label(window, background=bg, foreground=fg, font="arial 4", text="\n")
            buttonp=Button(window, text="BU TEMAYI UYGULA", command=apply, font="arial 12 bold", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="4")
            spacep2=Label(window, background=bg, foreground=fg, font="arial 4", text="\n")

        text1=Label(window, background=bg, foreground=fg, font="arial 11 bold italic", text="Lütfen yapmak istediğiniz işlemi seçiniz.")
        space1=Label(parent, background=bg, foreground=fg, font="arial 3", text="\n")
        button1=Button(parent, text="Uygulama mağazası", command=app_store, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")
        button2=Button(parent, text="Masaüstü Ortamı ve Pencere Yöneticisi mağazası", command=dewm_store, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")
        button3=Button(parent, text="Paket yöneticisi mağazası", command=pm_store, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")                
        button4=Button(parent, text="Programları yapılandırma", command=app_configure, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")        
        button5=Button(parent, text=".bashrc dosyasını yapılandırma", command=bashrc_config, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")
        button6=Button(parent, text="Dosya yöneticilerini kök kullanıcı haklarıyla açma", command=fm_open, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")
        button7=Button(parent, text="Bazı GNU/Linux dağıtımları hakkında bilgi verme", command=distros, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")
        button8=Button(parent, text="Sistemi güncelle", command=system_up, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="5")
        button9=Button(parent, text="Önbelleği ve/veya gereksiz paketleri temizle", command=clear_cache_app, font="arial 11 bold", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="5")
        if os.path.isfile(debian):
            button10=Button(parent, text="Paket hatalarını çöz", command=fixer, font="arial 11 bold", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="5")
    if p == 1:
        spacep1.pack()
        buttonp.pack()
        spacep2.pack()
    text1.pack()
    parent.pack(expand=1)
    space1.pack(fill="x")
    button1.pack(fill="x")
    button2.pack(fill="x")
    button3.pack(fill="x")
    button4.pack(fill="x")
    button5.pack(fill="x")
    button6.pack(fill="x")
    button7.pack(fill="x")
    button8.pack(fill="x")
    button9.pack(fill="x")
    if os.path.isfile(debian):
        button10.pack(fill="x")
    mainloop()


def main_cli():
    if "yardım" in args or "y" in args or "help" in args or "h" in args:
        if os.path.isfile(en):
            print("Here's how to call all feature modules:")
            print("l                              Show list of all modules (this) screen")
            print("list                           Show list of all modules (this) screen")
            print("app                            Application store")
            print("dewm                           Desktop Environment and Windows Manager store")
            print("packagemanager                 Package manager store")
            print("configure                      Configuring softwares")
            print("bashrc                         Configuring .bashrc file")           
            print("filemanager                    Opening file managers")
            print("distros                        Inform about some GNU/Linux distributions")
            print("updatesystem                   Update system")
            print("clear                          Clear cache and/or unnecessary packages")
            if os.path.isfile(debian):
                print("fix                             Fix package errors")
            print("Here's how to call all MetterXP modules:")
            print("about                         About")
            print("settings                      Settings")
            print("update                        Update")
            print("reset                         Reset")
            print("uninstall                     Uninstall")
        elif os.path.isfile(tr):
            print("İşte bütün özellik modüllerinin çağrılması:")
            print("l                              Tüm modüllerin listesini (burayı) göster")
            print("liste                          Tüm modüllerin listesini (burayı) göster")
            print("uygulama                       Uygulama mağazası")
            print("mopy                           Masaüstü Ortamı ve Pencere Yöneticisi mağazası")
            print("paketyöneticisi                Paket yöneticisi mağazası")
            print("yapılandır                     Yazılımları yapılandırma")
            print("bashrc                         .bashrc dosyasını yapılandırm")           
            print("dosyayönetici                  Dosya yöneticilerini kök kullanıcı haklarıyla açma")
            print("dağıtımlar                     Bazı GNU/Linux dağıtımları hakkında bilgi verme")
            print("sistemigüncelle                Sistemi güncelle")
            print("temizle                        Önbelleği ve/veya gereksiz paketleri temizle")
            if os.path.isfile(debian):
                print("çöz                             Paket hatalarını çöz")
            print("İşte bütün MetterXP modüllerinin çağrılması:")
            print("hakkında                       Hakkında")
            print("ayarlar                        Ayarlar")
            print("güncelle                       Güncelle")
            print("sıfırla                        Sıfırla")
            print("kaldır                         Kaldır")
        exit()
    elif "app" in args or "uygulama" in args:
        app_store()
        exit()
    elif "mopy" in args or "dewm" in args:
        dewm_store()
        exit()
    elif "packagemanager" in args or "paketyöneticisi" in args:
        pm_store()
        exit()
    elif "configure" in args or "yapılandır" in args:
        app_configure()
        exit()
    elif "bashrc" in args:
        bashrc_config()
        exit()
    elif "filemanager" in args or "dosyayönetici" in args:
        fm_open()
        exit()
    elif "distros" in args or "dağıtımlar" in args:
        distros()
        exit()
    elif "updatesystem" in args or "sistemigüncelle" in args:
        system_up()
        exit()
    elif "clear" in args or "temizle" in args:
        clear_cache_app()
        exit()
    elif "fix" in args or "çöz" in args:
        fixer()
        exit()
    elif "about" in args or "hakkında" in args:
        mxp_about()
        exit()
    elif "settings" in args or "ayarlar" in args:
        mxp_options()
        exit()
    elif "update" in args or "güncelle" in args:
        mxp_update()
        exit()
    elif "reset" in args or "sıfırla" in args:
        mxp_reset()
        exit()
    elif "uninstall" in args or "kaldır" in args:
        mxp_uninstall()
        exit()
    elif "app_configure" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/app_configure.py "+str(sys.argv[2]))
        exit()
    elif "app_store" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/app_store.py "+str(sys.argv[2]))
        exit()
    elif "clear_cache_app" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/clear_cache_app.py "+str(sys.argv[2]))
        exit()
    elif "dewm_store" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/dewm_store.py "+str(sys.argv[2]))
        exit()
    elif "fixer" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/fixer.py "+str(sys.argv[2]))
        exit()
    elif "mxp_uninstall" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/mxp_uninstall.py "+str(sys.argv[2]))
        exit()
    elif "mxp_update" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/mxp_reinstall.py "+str(sys.argv[2]))
        exit()
    elif "mxp_reset" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/mxp_reinstall.py "+str(sys.argv[2])+" --reset")
        exit()
    elif "pm_store" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/pm_store.py "+str(sys.argv[2]))
        exit()
    elif "fm_open" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/fm_open.py "+str(sys.argv[2]))
        exit()
    elif "system_up" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/system_up.py "+str(sys.argv[2]))
        exit()
    elif "install_yasfetch" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/yasfetchtaller.py "+str(sys.argv[2])+" --install")
        exit()
    elif "reinstall_yasfetch" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/yasfetchtaller.py "+str(sys.argv[2])+" --reinstall")
        exit()
    elif "uninstall_yasfetch" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/yasfetchtaller.py "+str(sys.argv[2])+" --uninstall")
        exit()
    else:
        main_gui()
        
if os.name == "nt":
    print("Welcome to MetterXP!\nMetterXP will not work on operating systems using the NT kernel.\nPlease try to open the program with a GNU/Linux distribution based on one of these three GNU/Linux distributions:\nDebian GNU/Linux, Fedora Linux, Solus")
    exit()
elif platform == "darwin":
    os.system("./unsupported.app/Contents/MacOS/applet")
elif os.path.isfile(debian) or os.path.isfile(fedora) or os.path.isfile(solus):
    main_cli()
else:
    print("Welcome to MetterXP!\nThe distribution you are using dosn't support MetterXP.\nPlease try to open the program with a GNU/Linux distribution based on one of these three GNU/Linux distributions:\nDebian GNU/Linux, Fedora Linux, Solus")
    exit()