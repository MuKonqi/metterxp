#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

# metterxp is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# metterxp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with metterxp.  If not, see <https://www.gnu.org/licenses/>.

from tkinter import *
from tkinter import messagebox
from subprocess import *
import subprocess
import os
import sys
from sys import platform


debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp-beta/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp-beta/settings/lang/en.txt"
args=sys.argv[1:]


if not os.path.isdir("/usr/local/bin/metterxp-beta/settings/lang/"):
    def lang_open():
        messagebox.showerror("Warning","Can't found language setting. When you click 'OK' and enter your true password, language settings will open. ")
        os.system("pkexec python3 /usr/local/bin/metterxp-beta/modules/mxp_settings.py")
        exit()
    if os.path.isfile(debian):
        lang_open()
    elif os.path.isfile(fedora):
        lang_open()
    elif os.path.isfile(solus):
        lang_open()


def mxp_info():
    subprocess.Popen("python3 /usr/local/bin/metterxp-beta/modules/mxp_info.py", shell=TRUE)
def mxp_settings():
    os.system("pkexec python3 /usr/local/bin/metterxp-beta/modules/mxp_settings.py")
    exit()
def mxp_update():
    os.system("pkexec python3 /usr/local/bin/metterxp-beta/modules/mxp_update.py --updateupdater")

def app_it_rm():
    subprocess.Popen("pkexec python3 /usr/local/bin/metterxp-beta/modules/app_it_rm.py", shell=TRUE)
def app_search():
    subprocess.Popen("python3 /usr/local/bin/metterxp-beta/modules/app_search.py", shell=TRUE)
def de_wm_it_rm():
    subprocess.Popen("python3 /usr/local/bin/metterxp-beta/modules/de_wm_it_rm.py", shell=TRUE)
def system_up():
    subprocess.Popen("python3 /usr/local/bin/metterxp-beta/modules/system_up.py", shell=TRUE)
def app_configre():
    subprocess.Popen("pkexec python3 /usr/local/bin/metterxp-beta/modules/app_configre.py", shell=TRUE)
def root_apps():
    subprocess.Popen("python3 /usr/local/bin/metterxp-beta/modules/root_apps.py", shell=TRUE)
def distros():
    subprocess.Popen("python3 /usr/local/bin/metterxp-beta/modules/distros.py", shell=TRUE)
def pm_it():
    subprocess.Popen("python3 /usr/local/bin/metterxp-beta/modules/pm_it.py", shell=TRUE)
def clean_cache_app():
    subprocess.Popen("python3 /usr/local/bin/metterxp-beta/modules/clean_cache_app.py", shell=TRUE)
def fixer():
    subprocess.Popen("python3 /usr/local/bin/metterxp-beta/modules/fixer.py", shell=TRUE)

bg=""
fg=""
button_bg=""
button_fg=""
a_button_bg=""
a_button_fg=""
if os.path.isfile("/usr/local/bin/metterxp-beta/settings/theme/0.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#03035B"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp-beta/settings/theme/1.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp-beta/settings/theme/2.txt"):
    bg="#FFFFFF"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFFFF"
    a_button_bg="#FFFFFF"
    a_button_fg="#000000"
elif os.path.isfile("/usr/local/bin/metterxp-beta/settings/theme/3.txt"):
    bg="#808080"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#808080"
    a_button_bg="#808080"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp-beta/settings/theme/4.txt"):
    bg="#FF0000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#FF0000"
    a_button_bg="#FF0000"
    a_button_fg="#FFFFFF"     
elif os.path.isfile("/usr/local/bin/metterxp-beta/settings/theme/5.txt"):
    bg="#FFA500"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#FFA500"
    a_button_bg="#FFA500"
    a_button_fg="#FFFFFF" 
elif os.path.isfile("/usr/local/bin/metterxp-beta/settings/theme/6.txt"):
    bg="#008000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#008000"
    a_button_bg="#008000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp-beta/settings/theme/7.txt"):
    bg="#0000FF"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#0000FF"
    a_button_bg="#0000FF"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp-beta/settings/theme/8.txt"):
    bg="#000080"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000080"
    a_button_bg="#000080"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp-beta/settings/theme/9.txt"):
    bg="#800080"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#800080"
    a_button_bg="#800080"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/metterxp-beta/settings/theme/10.txt"):
    bg="#FFC0CB"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFC0CB"
    a_button_bg="#FFC0CB"
    a_button_fg="#000000"
else:
    if os.path.isfile("/usr/local/bin/metterxp-beta/settings/lang/en.txt"):
        messagebox.showwarning("Warning","Can't found theme config. When you click 'OK' MetterXP settings will open.")
    elif os.path.isfile("/usr/local/bin/metterxp-beta/settings/lang/tr.txt"):
        messagebox.showwarning("Uyarı","Tema yapılandırması bulunamadı, MetterXP ayarları 'OK' tuşuna bastığınızda açılacaktır.")
    os.system("pkexec python3 /usr/local/bin/metterxp-beta/modules/mxp_settings.py")
    exit()


def main_gui():
    window=Tk()
    window.title("MetterXP 2.0-0 Beta")
    window.config(background=bg)
    window.resizable(0, 0)
    def mxp_exit():
        print("\nMetterXP kapatılıyor...\nClosing MetterXP...")
        exit()
    def update():
        window.destroy()
        mxp_update()
    def settings():
        window.destroy()
        mxp_settings()

    if os.path.isfile(lang_en):
        menu1=Menu(window)
        window.config(menu=menu1)
        file=Menu(menu1, tearoff=0)
        menu1.add_cascade(label="File",menu=file)
        file.add_command(label="Quit", command=mxp_exit)
        text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Please select the action you want to take.")
        space1=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        button1=Button(window, text="Install/reinstal/uninstall application", command=app_it_rm, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button2=Button(window, text="Search application/package", command=app_search, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        button3=Button(window, text="Install/reinstall/uninstall\ndesktop manager/window manager", command=de_wm_it_rm, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button4=Button(window, text="Update system", command=system_up, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button5=Button(window, text="Configre softwares", command=app_configre, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button6=Button(window, text="Open applications and run special command\nwith root user", command=root_apps, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button7=Button(window, text="About some GNU/Linux ditros", command=distros, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button8=Button(window, text="Install/reinstall package manager", command=pm_it, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button9=Button(window, text="Clean cache and/or unnecessary packages", command=clean_cache_app, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3")
        if os.path.isfile(debian):
            button10=Button(window, text="Fix package errors", command=fixer, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3")
            button10.pack()           
        space2=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        mxp_info_button=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3", text="About MetterXP",command=mxp_info)
        mxp_settings_button=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3", text="MetterXP settings",command=settings)
        mxp_update_button=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3", text="Update MetterXP",command=update)
        space3=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        mxp_exit_button=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3", text="Close MetterXP",command=mxp_exit)
    elif os.path.isfile(lang_tr):
        menu1=Menu(window)
        window.config(menu=menu1)
        file=Menu(menu1, tearoff=0)
        menu1.add_cascade(label="Dosya",menu=file)
        file.add_command(label="Çıkış", command=mxp_exit)
        text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Lütfen yapmak istediğiniz işlemi seçiniz.")
        space1=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        button1=Button(window, text="Program kurma/yeniden kurma/kaldırma", command=app_it_rm, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button2=Button(window, text="Program/paket arama", command=app_search, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        button3=Button(window, text="Masaüstü ortamı/pencere yöneticisi\nkurma/yeniden kurma/kaldırma", command=de_wm_it_rm, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button4=Button(window, text="Sistemi güncelleme", command=system_up, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button5=Button(window, text="Programları yapılandırma", command=app_configre, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button6=Button(window, text="Programları ve özel komutları\nkök kullanıcı haklarıyla açma", command=root_apps, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button7=Button(window, text="Bazı GNU/Linux dağıtımları hakkında", command=distros, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button8=Button(window, text="Paket yöneticisi kurma/yeniden kurma", command=pm_it, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        button9=Button(window, text="Önbelleği ve/veya gereksiz paketleri temizle", command=clean_cache_app, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3")
        if os.path.isfile(debian):
            button10=Button(window, text="Paket hatalarını çöz", command=fixer, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3")
            button10.pack()           
        space2=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
        mxp_info_button=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3", text="MetterXP hakkında",command=mxp_info)
        mxp_settings_button=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3", text="MetterXP ayarları",command=settings)
        mxp_update_button=Button(window, font="arial 10", cursor="hand2", background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, borderwidth="3", text="MetterXP'ı güncelle",command=update)
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
    mxp_settings_button.pack()
    mxp_update_button.pack()
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
            print("kök                            Programları ve özel komutları kök kullanıcı haklarıyla açma")
            print("dağıtımlar                     Bazı GNU/Linux dağıtımları hakkında")
            print("pmkur                          Paket yöneticisi kur/yeniden kur")
            print("hakkında                       MetterXP hakkında")
            print("ayarlar                        MetterXP ayarlar")
            print("güncelle                       MetterXP'ı güncelle")
            if os.path.isfile(solus):
                print("önbellektemizle                Önbelleği temizle")
            else:
                print("önbellekpakettemizle           Önbelleği ve gereksiz paketleri temizle")
            if os.path.isfile(debian):
                print("hataçözücü                     Hata çözücü")
        elif os.path.isfile(lang_en):
            print("\nMetterXP; program install/reinstall/uninstall, desktop environment/window manager install/reinstall/uninstall, system update, various configuration features (GRUB, Terminal, Plank, WINE...), package manager install/reinstall etc. It is a toolbox with features.")
            print("Here are al the uses:")
            print("help/-h                        Show help screen (this screen)")
            print("appitrm                        Install/reinstall/uninstall application")
            print("appsearch                      Search application/package")
            print("dewmitrm                       Install/reinstall/uninstall desktop environment/window manager")
            print("systemup                       Update system")
            print("configre                       Configre softwares")
            print("root                           Open applications and run special commands with root user")
            print("distros                        About some GNU/Linux distros")
            print("pmit                           Install/reinstall package manager")
            print("info                           About MetterXP")
            print("settings                       MetterXP settings")
            print("update                         Update MetterXP")
            if os.path.isfile(solus):
                print("cleancache                     Clean cache")
            else:
                print("cleancache                     Clear cache and unnecessary packages")
            if os.path.isfile(debian):
                print("fixerrs                     Error fixer")
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
        mxp_settings()
        exit()
    elif "güncelle" in args or "update" in args:
        mxp_update()
        exit()
    if os.path.isfile(solus):    
        if "önbellektemizle" in args or "cleancache" in args:
            clean_cache_app()
            exit()
    else:
        if "önbellekpakettemizle" in args or "cleanpackagecache" in args:
            fixer()
            exit()
    if os.path.isfile(debian):
        if "hataçözücü" in args in "fixerrs" in args:
            fixer()
            exit()
    else:
        main_gui()
    

if os.name == "nt":
    print("MetterXP'a hoş geldiniz!\nMetterXP NT çekirdeğini kullanan işletim sistemlerinde çalışmaz.\nLütfen şu üç GNU/Linux dağıtımından birini temel alan bir GNU/Linux dağıtımıyla programı açmayı deneyiniz:\nDebian GNU/Linux, Fedora Linux, Solus\n\nMetterXP kapatılıyor...")
    mxp_exit()
elif platform == "darwin":
    os.system("./unsupported.app/Contents/MacOS/applet")
elif os.path.isfile(debian):
    main_cli()
elif os.path.isfile(fedora):
    main_cli()
elif os.path.isfile(solus):
    main_cli()
else:
    print("MetterXP'a hoş geldiniz!\nKullandığınız dağıtımı MetterXP tam anlamıyla desteklemiyor.\nLütfen şu üç GNU/Linux dağıtımından birini temel alan bir GNU/Linux dağıtımıyla programı açmayı deneyiniz:\nDebian GNU/Linux, Fedora Linux, Solus\n\nMetterXP kapatılıyor...")
    exit()
