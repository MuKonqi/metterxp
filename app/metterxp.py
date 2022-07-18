#!/usr/bin/env python3

# Copyright (C) 2021, 2022 MuKonqi (Muhammed Abdurrahman)

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

def app_it_rm():
    subprocess.Popen("pkexec /usr/bin/metterxp app_it_rm", shell=TRUE)
def app_search():
    subprocess.Popen("python3 /usr/local/bin/metterxp/modules/app_search.py", shell=TRUE)
def de_wm_it_rm():
    subprocess.Popen("pkexec /usr/bin/metterxp de_wm_it_rm", shell=TRUE)
def system_up():
    subprocess.Popen("pkexec /usr/bin/metterxp system_up", shell=TRUE)
def app_configre():
    subprocess.Popen("pkexec /usr/bin/metterxp app_configre", shell=TRUE)
def root_apps():
    subprocess.Popen("pkexec /usr/bin/metterxp root_apps", shell=TRUE)
def distros():
    subprocess.Popen("python3 /usr/local/bin/metterxp/modules/distros.py", shell=TRUE)
def pm_it():
    subprocess.Popen("pkexec /usr/bin/metterxp pm_it", shell=TRUE)
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
    window=Tk()
    window.config(background=bg)
    window.resizable(0, 0)
    window.geometry("418x418")

    def mxp_exit():
        print("\nMetterXP kapatılıyor...\nClosing MetterXP...")
        exit()
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
        file=Menu(menu1, tearoff=0)
        menu1.add_cascade(label="File",menu=file)
        file.add_command(label="Quit", command=mxp_exit)
        m_options=Menu(menu1, tearoff=0)
        menu1.add_cascade(label="MetterXP",menu=m_options)
        m_options.add_command(label="About MetterXP",command=mxp_info)
        m_options.add_command(label="MetterXP options",command=options)
        m_options.add_command(label="Update MetterXP",command=update)
        m_options.add_command(label="Uninstall MetterXP",command=uninstall)

        text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Please select the action you want to take.")
        space1=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        button1=Button(window, text="Install/reinstal/uninstall application", command=app_it_rm, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button2=Button(window, text="Search application/package", command=app_search, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        button3=Button(window, text="Install/reinstall/uninstall\ndesktop manager/window manager", command=de_wm_it_rm, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button4=Button(window, text="Update system", command=system_up, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button5=Button(window, text="Configre softwares", command=app_configre, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button6=Button(window, text="Open applications with root user", command=root_apps, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button7=Button(window, text="About some GNU/Linux ditros", command=distros, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button8=Button(window, text="Install/reinstall package manager", command=pm_it, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button9=Button(window, text="Clean cache and/or unnecessary packages", command=clear_cache_app, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3")
        if os.path.isfile(debian):
            button10=Button(window, text="Fix package errors", command=fixer, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3")
            button10.pack()
        space2=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        mxp_info_button=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3", text="About MetterXP",command=mxp_info)
        mxp_options_button=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3", text="MetterXP options",command=options)
        space3=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        mxp_exit_button=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3", text="Close MetterXP",command=mxp_exit)
    elif os.path.isfile(lang_tr):
        window.title("Merhabalar "+username+"! • MetterXP")
        menu1=Menu(window)
        window.config(menu=menu1)
        file=Menu(menu1, tearoff=0)
        menu1.add_cascade(label="Dosya",menu=file)
        file.add_command(label="Çıkış", command=mxp_exit)
        m_options=Menu(menu1, tearoff=0)
        menu1.add_cascade(label="MetterXP",menu=m_options)
        m_options.add_command(label="MetterXP hakkında",command=mxp_info)
        m_options.add_command(label="MetterXP seçenekleri",command=options)
        m_options.add_command(label="MetterXP'ı güncelle",command=update)
        m_options.add_command(label="MetterXP'ı kaldır",command=uninstall)

        text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Lütfen yapmak istediğiniz işlemi seçiniz.")
        space1=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        button1=Button(window, text="Program kurma/yeniden kurma/kaldırma", command=app_it_rm, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button2=Button(window, text="Program/paket arama", command=app_search, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        button3=Button(window, text="Masaüstü ortamı/pencere yöneticisi\nkurma/yeniden kurma/kaldırma", command=de_wm_it_rm, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button4=Button(window, text="Sistemi güncelleme", command=system_up, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button5=Button(window, text="Programları yapılandırma", command=app_configre, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button6=Button(window, text="Programları kök kullanıcı haklarıyla açma", command=root_apps, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button7=Button(window, text="Bazı GNU/Linux dağıtımları hakkında", command=distros, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button8=Button(window, text="Paket yöneticisi kurma/yeniden kurma", command=pm_it, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button9=Button(window, text="Önbelleği ve/veya gereksiz paketleri temizle", command=clear_cache_app, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3")
        if os.path.isfile(debian):
            button10=Button(window, text="Paket hatalarını çöz", command=fixer, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3")
            button10.pack()
        space2=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        mxp_info_button=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3", text="MetterXP hakkında",command=mxp_info)
        mxp_options_button=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3", text="MetterXP seçenekleri",command=options)
        space3=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        mxp_exit_button=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3", text="MetterXP'ı kapat",command=mxp_exit)
    text1.pack()
    space1.pack()
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    button7.pack()
    button8.pack()
    button9.pack()
    space2.pack()
    mxp_info_button.pack()
    mxp_options_button.pack()
    space3.pack()
    mxp_exit_button.pack()
    mainloop()


def main_cli():
    if "yardım" in args or "-y" in args or "help" in args or "-h" in args:
        if os.path.isfile(lang_tr):
            print("\nMetterXP; program kurma/yeniden kurma/kaldırma, masaüstü ortamı/pencere yöneticisi kurma/yeniden kurma/kaldırma, sistem güncelleme, çeşitli yapılandırma özelliklerine (GRUB, Terminal, Plank, WINE...), paket yöneticisi kurma/yeniden kurma vs. özelliklere sahip olan bir araç kutusudur.")
            print("İşte bütün kullanımlar:")
            print("yardım/-y                      Yardım ekranını (burayı) göster")
            print("prkurkaldır                    Program kur/yeniden kur/kaldır")
            print("prara                          Program/paket ara")
            print("dewmkurkaldır                  Masaüstü ortamı/window yöneticisi kur/yeniden kur/kaldır")
            print("sistemigüncelle                Sistemi güncelle")
            print("yapılandır                     Yazılımları yapılandır")
            print("kök                            Programları kök kullanıcı haklarıyla açma")
            print("dağıtımlar                     Bazı GNU/Linux dağıtımları hakkında")
            print("pmkur                          Paket yöneticisi kur/yeniden kur")
            print("hakkında                       MetterXP hakkında")
            print("ayarlar                        MetterXP ayarlar")
            print("güncelle                       MetterXP'ı güncelle")
            print("kaldır                         MetterXP'ı kaldır")
            if os.path.isfile(solus):
                print("önbellektemizle                Önbelleği temizle")
            else:
                print("önbellekpakettemizle           Önbelleği ve gereksiz paketleri temizle")
            if os.path.isfile(debian):
                print("hataçözücü                     Paket hatalarını çöz")
        elif os.path.isfile(lang_en):
            print("\nMetterXP; program install/reinstall/uninstall, desktop environment/window manager install/reinstall/uninstall, system update, various configuration features (GRUB, Terminal, Plank, WINE...), package manager install/reinstall etc. It is a toolbox with features.")
            print("Here are al the uses:")
            print("help/-h                        Show help screen (this screen)")
            print("appitrm                        Install/reinstall/uninstall application")
            print("appsearch                      Search application/package")
            print("dewmitrm                       Install/reinstall/uninstall desktop environment/window manager")
            print("systemup                       Update system")
            print("configre                       Configre softwares")
            print("root                           Open applications with root user")
            print("distros                        About some GNU/Linux distros")
            print("pmit                           Install/reinstall package manager")
            print("info                           About MetterXP")
            print("settings                       MetterXP settings")
            print("update                         Update MetterXP")
            print("uninstall                      Uninstall MetterXP")
            if os.path.isfile(solus):
                print("clearcache                     Clean cache")
            else:
                print("clearcache                     Clear cache and unnecessary packages")
            if os.path.isfile(debian):
                print("fixerr                         Fix package errors")
        exit()
    elif "prkurkaldır" in args or "appitrm" in args:
        app_it_rm()
        exit()
    elif "prara" in args or "appsearch" in args:
        app_search()
        exit()
    elif "dewmkurkaldır" in args or "dewmitrm" in args:
        de_wm_it_rm()
        exit()
    elif "sistemigüncelle" in args or "systemup" in args:
        system_up()
        exit()
    elif "yapılandır" in args or "configre" in args:
        app_configre()
        exit()
    elif "kök" in args or "root" in args:
        root_apps()
    elif "dağıtımlar" in args or "distros" in args:
        distros()
        exit()
    elif "pmkur" in args or "pmit" in args:
        pm_it()
        exit()
    elif "hakkında" in args or "info" in args:
        mxp_info()
        exit()
    elif "ayarlar" in args or "settings" in args:
        mxp_options()
        exit()
    elif "güncelle" in args or "update" in args:
        mxp_update()
        exit()
    elif "kaldır" in args or "uninstall" in args:
        mxp_uninstall()
        exit()
    elif "app_configre" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/app_configre.py")
        exit()
    elif "app_it_rm" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/app_it_rm.py")
        exit()
    elif "clear_cache_app" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/clear_cache_app.py")
        exit()
    elif "de_wm_it_rm" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/de_wm_it_rm.py")
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
    elif "pm_it" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/pm_it.py")
        exit()
    elif "root_apps" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/root_apps.py")
        exit()
    elif "system_up" in args:
        os.system("python3 /usr/local/bin/metterxp/modules/system_up.py")
        exit()
    if os.path.isfile(solus):
        if "önbellektemizle" in args or "clearcache" in args:
            clear_cache_app()
            exit()
    else:
        if "önbellekpakettemizle" in args or "clearpackagecache" in args:
            fixer()
            exit()
    if os.path.isfile(debian):
        if "hataçözücü" in args in "fixerrs" in args:
            fixer()
            exit()
    else:
        main_gui()


if os.name == "nt":
    print("Welcome to MetterXP!\nMetterXP will not work on operating systems using the NT kernel.\nPlease try to open the program with a GNU/Linux distribution based on one of these three GNU/Linux distributions:\nDebian GNU/Linux, Fedora Linux, Solus\n\nClosing MetterXP ...")
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
    print("Welcome to MetterXP!\nThe distribution you are using does not fully support MetterXP.\nPlease try to open the program with a GNU/Linux distribution based on one of these three GNU/Linux distributions:\nDebian GNU/Linux, Fedora Linux, Solus\nClosing MetterXP...")
    exit()
