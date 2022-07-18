#!/usr/bin/env python3

# Copyright (C) 2021, 2022 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
from subprocess import *
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
    window.title("Install/reinstall/uninstall application | MetterXP")
elif os.path.isfile(lang_tr):
    window.title("Program kur/yeniden kur/kaldır | MetterXP")
window.config(background=bg)
window.resizable(0, 0)


def main():
    def to_other():
        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button_1.destroy()
        button_2.destroy()
        text1.destroy()
        space1.destroy()
        space2.destroy()
        space3.destroy()
        exit_button_1.destroy()
        other()
    def to_flatpak():
        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button_1.destroy()
        button_2.destroy()
        text1.destroy()
        space1.destroy()
        space2.destroy()
        space3.destroy()
        exit_button_1.destroy()
        flatpak()
        
    def firefox():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install firefox -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install firefox -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install firefox -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! Mozilla Firefox was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Mozilla Firefox başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall firefox -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall firefox -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install firefox -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! Mozilla Firefox was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Mozilla Firefox başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge firefox* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove firefox* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove firefox -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! Mozilla Firefox was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Mozilla Firefox başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Mozilla Firefox browser?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="Mozilla Firefox internet tarayıcısı için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_3.pack()
    def brave():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install apt-transport-https curl")
                os.system(" curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
                os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"| tee /etc/apt/sources.list.d/brave-browser-release.list')
                os.system(" apt update")
                os.system(" apt install brave-browser")
            elif os.path.isfile(fedora):
                os.system(" dnf install dnf-plugins-core")
                os.system(" dnf config-manager --add-repo https://brave-browser-rpm-release.s3.brave.com/x86_64")
                os.system(' rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc')
                os.system(" dnf install brave-browser")                
            elif os.path.isfile(solus):
                os.system(" eopkg install brave -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succesful! Brave was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Brave başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall brave-browser -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall brave-browser -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install brave -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succesful! Brave was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Brave başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge brave-browser* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove brave-browser* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove brave -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succesful! Brave rwas uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Brave başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button_1.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Brave browser?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="Brave internet tarayıcısı için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_3.pack()
    def vlc():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install vlc -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install vlc -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install vlc -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! VLC was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","VLC başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall vlc -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall vlc -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install vlc -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! VLC was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","VLC başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge vlc* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove vlc* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove vlc -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! VLC was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","VLC başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for VLC media player?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="VLC medya oynatıcıs için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_3.pack()
    def libreoffice():
        def it():
            if os.path.isfile(debian):
                os.system(" add-apt-repository ppa:libreoffice/ppa")
                os.system(" apt update")
                os.system(" apt install libreoffice libreoffice-l10n-tr libreoffice-help-tr -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install libreoffice -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install libreoffice -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! LibreOffice was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","LibreOffice başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall libreoffice libreoffice-l10n-tr libreoffice-help-tr -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall libreoffice -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install libtreoffice -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! LibreOffice was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","LibreOffice başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge libreoffice* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove libreoffice* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove libreoffice -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! LibreOffice was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","LibreOffice başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for LibreOffice office suite?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="LibreOffice ofis programı için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_3.pack()
    def cups():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install cups -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install cups -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install cups -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! Cups was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Cups başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall cups -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall cups -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install cups -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! Cups was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Cups başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge cups* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove cups* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove cups -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! Cups was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Cups başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Cups printer manager?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="Cups yazıcı yöneticisi için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_3.pack()
    def gparted():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install gparted -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install gparted -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install gparted -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! GParted was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GParted başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall gparted -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall gparted -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install gparted -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! GParted was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GParted başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge gparted* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove gparted* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove gparted -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! GParted was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GParted başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for GParted disk part editor?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="GParted disk bölümü düzenleyicisi için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_3.pack()
    def gimp():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install gimp -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install gimp -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install gimp -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! GIMP was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GIMP başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall gimp -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall gimp -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install gimp -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! GIMP was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GIMP başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge gimp* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove gimp* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove gimp -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! GIMP was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GIMP başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for GIMP image manipulation?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="GIMP görüntü işleme programı için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_3.pack()
    def wine():
        def it():
            if os.path.isfile(debian):
                os.system(" dpkg --add-architecture i386")
                os.system(" apt install wine-stable -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install wine -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install wine -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! Wine was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Wine başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall wine -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall wine -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install wine -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! Wine was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Wine başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge wine-stable* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove wine* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove wine -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! Wine was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Wine başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Wine?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="Wine için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_3.pack()
    def plank():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install plank -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install plank -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install plank -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! Plank was installed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Plank başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall plank -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall plank -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install plank -y --rei")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! Plank was reinstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Plank başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge plank* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove plank* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove plank -y --purge")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succcesful! Plank was uninstalled.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Plank başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Plank dock?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            text1.config(text="Plank rıhtımı için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_3.pack()
    if os.path.isfile(lang_en):
        text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Which program do you want to install or reinstall or remove?")
        space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
        button1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Mozilla Firefox browser",command=firefox)
        button2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Brave browser",command=brave)
        button3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="VLC media player",command=vlc)
        button4=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="LibreOffice office suite",command=libreoffice)
        button5=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Cups printer manager",command=cups)
        button6=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="GParted disk part editor",command=gparted)
        button7=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="GIMP image manipulation",command=gimp)
        button8=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Wine",command=wine)
        button9=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Plank dock",command=plank)
        space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
        button_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Other", command=to_other)
        button_2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Flatpak applications", command=to_flatpak)
        space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
        exit_button_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
    elif os.path.isfile(lang_tr):    
        text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Hangi programı kurmak veya yeniden kurmak veya kaldırmak istiyorsunuz?")
        space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
        button1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Mozilla Firefox internet tarayıcısı",command=firefox)
        button2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Brave internet tarayıcısı",command=brave)
        button3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="VLC medya oynatıcısı",command=vlc)
        button4=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="LibreOffice ofis programı",command=libreoffice)
        button5=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Cups yazıcı yöneticisi",command=cups)
        button6=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="GParted disk bölümü düzenleyicisi",command=gparted)
        button7=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="GIMP görüntü işleme programı",command=gimp)
        button8=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Wine",command=wine)
        button9=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Plank rıhtımı",command=plank)
        space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
        button_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Diğer", command=to_other)
        button_2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Flatpak uygulamaları", command=to_flatpak)
        space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
        exit_button_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
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
    button_1.pack()
    button_2.pack()
    space3.pack()
    exit_button_1.pack()

def flatpak():
    def flatpak_main():
        def f_packageit():
            c1_f_package="flatpak install "
            get_f_packagename=f_packagename.get()
            c2_f_package=" -y"
            cf_f_package=c1_f_package+get_f_packagename+c2_f_package
            run_cf_f_package = subprocess.Popen(cf_f_package, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
            (out, err) = run_cf_f_package.communicate()
            if os.path.isfile(lang_en):
                window_2=Toplevel()
                window_2.title("Output | MetterXP")
                window_2.config(background="#000000")
                window_2.resizable(0, 0)
                scroll=Scrollbar(window_2)
                text7=Label(window_2, background=bg, foreground=fg, font="arial 12", text="\nInformation: When the package name you entered is correct, the process has been completed successfully! \n\nNote: Changing the command output below does not change anything.\n")
                text8=Text(window_2, yscrollcommand=scroll.set)
                text8.insert(END, out)
                scroll.config(command=text8.yview)
                space10=Label(window_2, background=bg, foreground=fg, text="\n", font="arial 3")
                button_7=Button(window_2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close window", command=window_2.destroy)
            elif os.path.isfile(lang_tr):
                window_2=Toplevel()
                window_2.title("Çıktı | MetterXP")
                window_2.config(background="#000000")
                window_2.resizable(0, 0)
                scroll=Scrollbar(window_2)
                text7=Label(window_2, background=bg, foreground=fg, font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
                text8=Text(window_2, yscrollcommand=scroll.set)
                text8.insert(END, out)
                scroll.config(command=text8.yview)
                space10=Label(window_2, background=bg, foreground=fg, text="\n", font="arial 3")
                button_7=Button(window_2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Pencereyi kapat", command=window_2.destroy)
            scroll.pack(side=RIGHT,fill=Y)
            text7.pack()
            text8.pack()
            space10.pack()
            button_7.pack()
        def f_packagereit():
            c1_f_package="flatpak install "
            get_f_packagename=f_packagename.get()
            c2_f_package=" -y --reinstall"
            cf_f_package=c1_f_package+get_f_packagename+c2_f_package
            run_cf_f_package = subprocess.Popen(cf_f_package, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
            (out, err) = run_cf_f_package.communicate()
            if os.path.isfile(lang_en):
                window_2=Toplevel()
                window_2.title("Output | MetterXP")
                window_2.config(background="#000000")
                window_2.resizable(0, 0)
                scroll=Scrollbar(window_2)
                text7=Label(window_2, background=bg, foreground=fg, font="arial 12", text="\nInformation: When the package name you entered is correct, the process has been completed successfully! \n\nNote: Changing the command output below does not change anything.\n")
                text8=Text(window_2, yscrollcommand=scroll.set)
                text8.insert(END, out)
                scroll.config(command=text8.yview)
                space10=Label(window_2, background=bg, foreground=fg, text="\n", font="arial 3")
                button_7=Button(window_2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close window", command=window_2.destroy)
            elif os.path.isfile(lang_tr):
                window_2=Toplevel()
                window_2.title("Çıktı | MetterXP")
                window_2.config(background="#000000")
                window_2.resizable(0, 0)
                scroll=Scrollbar(window_2)
                text7=Label(window_2, background=bg, foreground=fg, font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
                text8=Text(window_2, yscrollcommand=scroll.set)
                text8.insert(END, out)
                scroll.config(command=text8.yview)
                space10=Label(window_2, background=bg, foreground=fg, text="\n", font="arial 3")
                button_7=Button(window_2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Pencereyi kapat", command=window_2.destroy)
            scroll.pack(side=RIGHT,fill=Y)
            text7.pack()
            text8.pack()
            space10.pack()
            button_7.pack()
        def f_packagerm():
            c1_f_package="flatpak uninstall "
            get_f_packagename=f_packagename.get()
            c2_f_package=" -y"
            cf_f_package=c1_f_package+get_f_packagename+c2_f_package
            run_cf_f_package = subprocess.Popen(cf_f_package, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
            (out, err) = run_cf_f_package.communicate()
            if os.path.isfile(lang_en):
                window_2=Toplevel()
                window_2.title("Output | MetterXP")
                window_2.config(background="#000000")
                window_2.resizable(0, 0)
                scroll=Scrollbar(window_2)
                text7=Label(window_2, background=bg, foreground=fg, font="arial 12", text="\nInformation: When the package name you entered is correct, the process has been completed successfully! \n\nNote: Changing the command output below does not change anything.\n")
                text8=Text(window_2, yscrollcommand=scroll.set)
                text8.insert(END, out)
                scroll.config(command=text8.yview)
                space10=Label(window_2, background=bg, foreground=fg, text="\n", font="arial 3")
                button_7=Button(window_2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close window", command=window_2.destroy)
            elif os.path.isfile(lang_tr):
                window_2=Toplevel()
                window_2.title("Çıktı | MetterXP")
                window_2.config(background="#000000")
                window_2.resizable(0, 0)
                scroll=Scrollbar(window_2)
                text7=Label(window_2, background=bg, foreground=fg, font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
                text8=Text(window_2, yscrollcommand=scroll.set)
                text8.insert(END, out)
                scroll.config(command=text8.yview)
                space10=Label(window_2, background=bg, foreground=fg, text="\n", font="arial 3")
                button_7=Button(window_2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Pencereyi kapat", command=window_2.destroy)
            scroll.pack(side=RIGHT,fill=Y)
            text7.pack()
            text8.pack()
            space10.pack()
            button_7.pack()
        if os.path.isfile(lang_en):
            window.title("Install/reinstall/uninstall Flatpak apps | MetterXP")
            text5=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Please enter the name of the program/package you want to install or reinstall or uninstall.\nNote: You must enter the package name correctly!")
            space7=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
            f_packagename=Entry(window)
            b_f_packageit=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Install",command=f_packageit)
            b_f_packagereit=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Reinstall",command=f_packagereit)
            b_f_packagerm=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Uninstall",command=f_packagerm)
            space8=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
            text6=Label(window, background=bg, foreground=fg, font="arial 9 bold", text="Information: There may be some errors (meaningless letters, numbers, etc.) in the command output to be opened.\nPlease ignore this.")
            space9=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
            exit_button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            reopen_button_2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Restart this module\nBack to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            window.title("Flatpak uygulamaları kur/yeniden/kur/kaldır | MetterXP")
            text5=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Lütfen kurmak veya yeniden kurmak veya kaldırmak istediğiniz programın/paketin adını giriniz.\nNot: Paket adını doğru girmeniz gerekmektedir!")
            space7=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
            f_packagename=Entry(window)
            b_f_packageit=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Kur",command=f_packageit)
            b_f_packagereit=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Yeniden kur",command=f_packagereit)
            b_f_packagerm=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Kaldır",command=f_packagerm)
            space8=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
            text6=Label(window, background=bg, foreground=fg, font="arial 9 bold", text="Bilgilendirme: Açılacak komut çıktısında bazı hatalar (anlamsız harfler, sayılar vb.) olabilir.\nLütfen bunu dikkate almayınız.")
            space9=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
            exit_button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            reopen_button_2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        text5.pack()
        space7.pack()
        f_packagename.pack()
        b_f_packageit.pack()
        b_f_packagereit.pack()
        b_f_packagerm.pack()
        space8.pack()
        text6.pack()
        space9.pack()
        exit_button_3.pack()
        reopen_button_2.pack()
    if os.path.isfile("/usr/bin/flatpak") or os.path.isfile("/bin/flatpak:"):
        flatpak_main()
    else:
        if os.path.isfile(lang_en):
            messagebox.showwarning("Warning","Flatpak can't found. When you click 'OK', package manager installer will be open.")
        elif os.path.isfile(lang_tr):
            messagebox.showwarning("Uyarı","Flatpak bulunamadı. 'OK' tuşuna bastığınızda paket yöneticisi yükleyicisi açılacaktır.")
        window.destroy()
        os.system("pkexec python3 /usr/local/bin/metterxp/modules/pm_it.py")
        flatpak_main()
def other():
    def packageit():
        if os.path.isfile(debian):
            c1_package=" apt install "
            get_packagename=packagename.get()
            c2_package=" -y"
            cf_package=c1_package+get_packagename+c2_package
            run_cf_package = subprocess.Popen(cf_package, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
            (out, err) = run_cf_package.communicate()
        elif os.path.isfile(fedora):
            c1_package=" dnf install "
            get_packagename=packagename.get()
            c2_package=" -y"
            cf_package=c1_package+get_packagename+c2_package
            run_cf_package = subprocess.Popen(cf_package, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
            (out, err) = run_cf_package.communicate()
        elif os.path.isfile(solus):
            c1_package=" eopkg install "
            get_packagename=packagename.get()
            c2_package=" -y"
            cf_package=c1_package+get_packagename+c2_package
            run_cf_package = subprocess.Popen(cf_package, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
            (out, err) = run_cf_package.communicate()
        if os.path.isfile(lang_en):
            window_2=Toplevel()
            window_2.title("Output | MetterXP")
            window_2.config(background=bg)
            window_2.resizable(0, 0)
            scroll=Scrollbar(window_2)
            text3=Label(window_2, background=bg, foreground=fg, font="arial 12", text="\nInformation: When the package name you entered is correct, the process has been completed successfully!\n\nNote: Changing the output of the command below will not change anything.\n")
            text4=Text(window_2, yscrollcommand=scroll.set)
            text4.insert(END, out)
            scroll.config(command=text4.yview)
            space6=Label(window_2, background=bg, foreground=fg, text="\n", font="arial 3")
            button_6=Button(window_2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close window", command=window_2.destroy)
        elif os.path.isfile(lang_tr):
            window_2=Toplevel()
            window_2.title("Çıktı | MetterXP")
            window_2.config(background=bg)
            window_2.resizable(0, 0)
            scroll=Scrollbar(window_2)
            text3=Label(window_2, background=bg, foreground=fg, font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
            text4=Text(window_2, yscrollcommand=scroll.set)
            text4.insert(END, out)
            scroll.config(command=text4.yview)
            space6=Label(window_2, background=bg, foreground=fg, text="\n", font="arial 3")
            button_6=Button(window_2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Pencereyi kapat", command=window_2.destroy)
        scroll.pack(side=RIGHT,fill=Y)
        text3.pack()
        text4.pack()
        space6.pack()
        button_6.pack()
    def packagereit():
        if os.path.isfile(debian):
            c1_package=" apt reinstall "
            get_packagename=packagename.get()
            c2_package=" -y"
            cf_package=c1_package+get_packagename+c2_package
            run_cf_package = subprocess.Popen(cf_package, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
            (out, err) = run_cf_package.communicate()
        elif os.path.isfile(fedora):
            c1_package=" dnf reinstall "
            get_packagename=packagename.get()
            c2_package=" -y"
            cf_package=c1_package+get_packagename+c2_package
            run_cf_package = subprocess.Popen(cf_package, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
            (out, err) = run_cf_package.communicate()
        elif os.path.isfile(solus):
            c1_package=" eopkg install "
            get_packagename=packagename.get()
            c2_package=" -y --rei"
            cf_package=c1_package+get_packagename+c2_package
            run_cf_package = subprocess.Popen(cf_package, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
            (out, err) = run_cf_package.communicate()
        if os.path.isfile(lang_en):
            window_2=Toplevel()
            window_2.title("Output | MetterXP")
            window_2.config(background=bg)
            window_2.resizable(0, 0)
            scroll=Scrollbar(window_2)
            text3=Label(window_2, background=bg, foreground=fg, font="arial 12", text="\nInformation: When the package name you entered is correct, the process has been completed successfully!\n\nNote: Changing the output of the command below will not change anything.\n")
            text4=Text(window_2, yscrollcommand=scroll.set)
            text4.insert(END, out)
            scroll.config(command=text4.yview)
            space6=Label(window_2, background=bg, foreground=fg, text="\n", font="arial 3")
            button_6=Button(window_2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close window", command=window_2.destroy)
        elif os.path.isfile(lang_tr):
            window_2=Toplevel()
            window_2.title("Çıktı | MetterXP")
            window_2.config(background=bg)
            window_2.resizable(0, 0)
            scroll=Scrollbar(window_2)
            text3=Label(window_2, background=bg, foreground=fg, font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
            text4=Text(window_2, yscrollcommand=scroll.set)
            text4.insert(END, out)
            scroll.config(command=text4.yview)
            space6=Label(window_2, background=bg, foreground=fg, text="\n", font="arial 3")
            button_6=Button(window_2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Pencereyi kapat", command=window_2.destroy)
        scroll.pack(side=RIGHT,fill=Y)
        text3.pack()
        text4.pack()
        space6.pack()
        button_6.pack()      
    def packagerm():
        if os.path.isfile(debian):
            c1_package=" apt purge "
            get_packagename=packagename.get()
            c2_package="* -y"
            cf_package=c1_package+get_packagename+c2_package
            run_cf_package = subprocess.Popen(cf_package, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
            (out, err) = run_cf_package.communicate()
        elif os.path.isfile(fedora):
            c1_package=" dnf remove "
            get_packagename=packagename.get()
            c2_package="* -y"
            cf_package=c1_package+get_packagename+c2_package
            run_cf_package = subprocess.Popen(cf_package, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
            (out, err) = run_cf_package.communicate()
        elif os.path.isfile(solus):
            c1_package=" eopkg remove "
            get_packagename=packagename.get()
            c2_package=" -y --purge"
            cf_package=c1_package+get_packagename+c2_package
            run_cf_package = subprocess.Popen(cf_package, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
            (out, err) = run_cf_package.communicate()
        if os.path.isfile(lang_en):
            window_2=Toplevel()
            window_2.title("Output | MetterXP")
            window_2.config(background=bg)
            window_2.resizable(0, 0)
            scroll=Scrollbar(window_2)
            text3=Label(window_2, background=bg, foreground=fg, font="arial 12", text="\nInformation: When the package name you entered is correct, the process has been completed successfully!\n\nNote: Changing the output of the command below will not change anything.\n")
            text4=Text(window_2, yscrollcommand=scroll.set)
            text4.insert(END, out)
            scroll.config(command=text4.yview)
            space6=Label(window_2, background=bg, foreground=fg, text="\n", font="arial 3")
            button_6=Button(window_2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close window", command=window_2.destroy)
        elif os.path.isfile(lang_tr):
            window_2=Toplevel()
            window_2.title("Çıktı | MetterXP")
            window_2.config(background=bg)
            window_2.resizable(0, 0)
            scroll=Scrollbar(window_2)
            text3=Label(window_2, background=bg, foreground=fg, font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
            text4=Text(window_2, yscrollcommand=scroll.set)
            text4.insert(END, out)
            scroll.config(command=text4.yview)
            space6=Label(window_2, background=bg, foreground=fg, text="\n", font="arial 3")
            button_6=Button(window_2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Pencereyi kapat", command=window_2.destroy)
        scroll.pack(side=RIGHT,fill=Y)
        text3.pack()
        text4.pack()
        space6.pack()
        button_6.pack()
    if os.path.isfile(lang_en):
        text2=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Please enter the name of the program/package you want to install or reinstall or uninstall.\nNote: You must enter the package name correctly!")
        space4=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
        packagename=Entry(window)
        b_packageit=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Install",command=packageit)
        b_packagereit=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Reinstall",command=packagereit)
        b_packagerm=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Uninsall",command=packagerm)
        space5=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
        text3=Label(window, background=bg, foreground=fg, font="arial 9 bold", text="Information: There may be some errors (meaningless letters, numbers, etc.) in the command output to be opened.\nPlease ignore this.")
        space6=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
        exit_button_2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
        reopen_button_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Restart this module\nBack to menu", command=reopen)
    elif os.path.isfile(lang_tr):
        text2=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Lütfen kurmak veya yeniden kurmak veya kaldırmak istediğiniz programın/paketin adını giriniz.\nNot: Paket adını doğru girmeniz gerekmektedir!")
        space4=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
        packagename=Entry(window)
        b_packageit=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Kur",command=packageit)
        b_packagereit=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Yeniden kur",command=packagereit)
        b_packagerm=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Kaldır",command=packagerm)
        space5=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
        text3=Label(window, background=bg, foreground=fg, font="arial 9 bold", text="Bilgilendirme: Açılacak komut çıktısında bazı hatalar (anlamsız harfler, sayılar vb.) olabilir.\nLütfen bunu dikkate almayınız.")
        space6=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
        exit_button_2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
        reopen_button_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
    text2.pack()
    space4.pack()
    packagename.pack()
    b_packageit.pack()
    b_packagereit.pack()
    b_packagerm.pack()
    space5.pack()
    text3.pack()
    space6.pack()
    exit_button_2.pack()
    reopen_button_1.pack()


main()
mainloop()