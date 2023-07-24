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


debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp/settings/lang/en.txt"
args=sys.argv[1:]


def mxp_info():
    subprocess.Popen("python3 /usr/local/bin/metterxp/modules/mxp_info.py", shell=TRUE)
def mxp_update():
    os.system("pkexec /usr/bin/metterxp mxp_update")
    exit()
def mxp_uninstall():
    os.system("pkexec /usr/bin/metterxp mxp_uninstall")
    exit()
def mxp_options():
    os.system("pkexec /usr/bin/metterxp mxp_options")
    exit()

def app_store():
    subprocess.Popen("pkexec /usr/bin/metterxp app_store", shell=TRUE)
def dewm_store():
    subprocess.Popen("pkexec /usr/bin/metterxp dewm_store", shell=TRUE)
def pm_store():
    subprocess.Popen("pkexec /usr/bin/metterxp pm_store", shell=TRUE)
def app_configure():
    subprocess.Popen("pkexec /usr/bin/metterxp app_configure", shell=TRUE)
def bashrc_config():
    subprocess.Popen("python3 /usr/local/bin/metterxp/modules/bashrc_config.py", shell=TRUE)
def fm_open():
    subprocess.Popen("pkexec /usr/bin/metterxp fm_open", shell=TRUE)
def distros():
    subprocess.Popen("python3 /usr/local/bin/metterxp/modules/distros.py", shell=TRUE)
def system_up():
    subprocess.Popen("pkexec /usr/bin/metterxp system_up", shell=TRUE)
def clear_cache_app():
    subprocess.Popen("pkexec /usr/bin/metterxp clear_cache_app", shell=TRUE)
def fixer():
    subprocess.Popen("pkexec /usr/bin/metterxp fixer", shell=TRUE)

if not "mxp_options" in args:
    if not os.path.isdir("/usr/local/bin/metterxp/settings/lang/"):
        def lang_open():
            messagebox.showerror("Warning","Can't found language setting. When you click 'OK' and enter your true password, language settings will open. ")
            mxp_options()
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
    if not "mxp_options" in args:
        def theme_open():
            if os.path.isfile("/usr/local/bin/metterxp/settings/lang/en.txt"):
                messagebox.showwarning("Warning","Can't found theme config. When you click 'OK' MetterXP settings will open.")
            elif os.path.isfile("/usr/local/bin/metterxp/settings/lang/tr.txt"):
                messagebox.showwarning("Uyarı","Tema yapılandırması bulunamadı, MetterXP ayarları 'OK' tuşuna bastığınızda açılacaktır.")
            mxp_options()
            exit()
        if os.path.isfile(debian):
            theme_open()
        elif os.path.isfile(fedora):
            theme_open()
        elif os.path.isfile(solus):
            theme_open()


def main_gui():   
    if os.getuid() == 0:
        if os.path.isfile(lang_en):
                messagebox.showwarning("Fatal Request","You started MetterXP as root but MetterXP main page don't support it. Also MetterXP already requests root rights when it needs root rights.")
        elif os.path.isfile(lang_tr):
                messagebox.showinfo("Ölümcül İstek","MetterXP'ı kök olarak başlattınız ama MetterXP ana sayfası bunu desteklemez. Ayrıca MetterXP, kök haklarına ihtiyaç duyduğunda zaten kök haklarını ister.")
        exit()

    window=Tk()
    window.config(background=bg)
    window.resizable(0, 0)
    window.geometry("483x483")
    parent = Frame(window)
    
    def options():
        window.destroy()
        mxp_options()
    def update():
        window.destroy()
        mxp_update()
    def uninstall():
        window.destroy()
        mxp_uninstall()

    if os.path.isfile(lang_en):
        window.title("Hello "+username+"! • MetterXP")
        menu1=Menu(window)
        window.config(menu=menu1)
        m_options=Menu(menu1, tearoff=0)
        menu1.add_cascade(label="File",menu=m_options)
        m_options.add_command(label="About",command=mxp_info)
        m_options.add_command(label="Options",command=options)
        m_options.add_command(label="Update",command=update)
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
    elif os.path.isfile(lang_tr):
        window.title("Merhabalar "+username+"! • MetterXP")
        menu1=Menu(window)
        window.config(menu=menu1)
        m_options=Menu(menu1, tearoff=0)
        menu1.add_cascade(label="Dosya",menu=m_options)
        m_options.add_command(label="MetterXP hakkında",command=mxp_info)
        m_options.add_command(label="MetterXP seçenekleri",command=options)
        m_options.add_command(label="MetterXP'ı güncelle",command=update)
        m_options.add_command(label="MetterXP'ı kaldır",command=uninstall)
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
        if os.path.isfile(lang_en):
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
            print("settings                      MetterXP")
            print("update                        Update")
            print("uninstall                     Uninstall")
        elif os.path.isfile(lang_tr):
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
            print("ayarlar                        Ayarları")
            print("güncelle                       Güncelle")
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
        mxp_info()
        exit()
    elif "settings" in args or "ayarlar" in args:
        mxp_options()
        exit()
    elif "update" in args or "güncelle" in args:
        mxp_update()
        exit()
    elif "uninstall" in args or "kaldır" in args:
        mxp_uninstall()
        exit()
    elif "app_configure" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/app_configure.py")
        exit()
    elif "bashrc_config" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/bashrc_config.py")
        exit()
    elif "app_store" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/app_store.py")
        exit()
    elif "clear_cache_app" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/clear_cache_app.py")
        exit()
    elif "dewm_store" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/dewm_store.py")
        exit()
    elif "fixer" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/fixer.py")
        exit()
    elif "mxp_options" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/mxp_options.py")
        exit()
    elif "mxp_uninstall" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/mxp_uninstall.py")
        exit()
    elif "mxp_update" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/mxp_update.py --updateupdater")
        exit()
    elif "pm_store" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/pm_store.py")
        exit()
    elif "fm_open" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/fm_open.py")
        exit()
    elif "system_up" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/system_up.py")
        exit()
    elif "install_yasfetch" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/yasfetchtaller.py --install")
        exit()
    elif "reinstall_yasfetch" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/yasfetchtaller.py --reinstall")
        exit()
    elif "uninstall_yasfetch" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/yasfetchtaller.py --uninstall")
        exit()
    else:
        main_gui()


if os.name == "nt":
    print("Welcome to MetterXP!\nMetterXP will not work on operating systems using the NT kernel.\nPlease try to open the program with a GNU/Linux distribution based on one of these three GNU/Linux distributions:\nDebian GNU/Linux, Fedora Linux, Solus")
    exit()
elif platform == "darwin":
    os.system("./unsupported.app/Contents/MacOS/applet")
elif os.path.isfile(debian):
    main_cli()
elif os.path.isfile(fedora):
    main_cli()
elif os.path.isfile(solus):
    main_cli()
else:
    print("Welcome to MetterXP!\nThe distribution you are using dosn't support MetterXP.\nPlease try to open the program with a GNU/Linux distribution based on one of these three GNU/Linux distributions:\nDebian GNU/Linux, Fedora Linux, Solus")
    exit()