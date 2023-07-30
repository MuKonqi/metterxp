#!/usr/bin/env python3

# Copyright (C) 2021, 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
from subprocess import *
import os
import subprocess
import sys

t="/home/"+str(sys.argv[1])+"/.by-mukonqi/metterxp/theme/"
en="/home/"+str(sys.argv[1])+"/.by-mukonqi/metterxp/language/en.txt"
tr="/home/"+str(sys.argv[1])+"/.by-mukonqi/metterxp/language/tr.txt"
debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if not os.path.isdir("/home/"+str(sys.argv[1])+"/.by-mukonqi/metterxp/"):
    messagebox.showerror("User Error - Fatal | MetterXP","Please start only MetterXP (just select MetterXP in the applications section or type metterxp) to set up language and theme preferences.")
    exit()

if not os.getuid() == 0:
    if os.path.isfile(en):
        messagebox.showerror("Error","Only root can run this module!")
        exit()
    elif os.path.isfile(tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
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
    if os.path.isfile(en):
        messagebox.showerror("User Error - Fatal | MetterXP","Please start only MetterXP (just select MetterXP in the applications section or type metterxp) to set up theme preferences.")
    elif os.path.isfile(tr):
        messagebox.showerror("Kullanıcı Hatası - Ölümcül | MetterXP", "Tema tercihlerini ayarlamak için lütfen yalnızca MetterXP'yi başlatın (uygulamalar bölümünde MetterXP'yi seçin veya metterxp yazın.")
    exit()

def reopen():
    window.destroy()
    os.system("pkexec /usr/bin/metterxp app_store "+str(sys.argv[1]))
    
window=Tk(className="MetterXP")
if os.path.isfile(en):
    window.title("Application store | MetterXP")
elif os.path.isfile(tr):
    window.title("Uygulama mağazası | MetterXP")
window.config(background=bg)
window.resizable(0, 0)
parent = Frame(window)
window.geometry("571x571")
icon = PhotoImage(file="/usr/local/bin/metterxp/icon.png")
window.iconphoto(True, icon)
parent.pack(expand=1)


def main():
    def others():
        buttonm.destroy()
        spacem.destroy()
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
    def to_other():
        others()
        other()
    def to_flatpak():
        others()
        flatpak()
        
    def firefox():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install firefox -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install firefox -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install firefox -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Mozilla Firefox was installed.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Mozilla Firefox başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall firefox -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall firefox -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install firefox -y --rei")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Mozilla Firefox was reinstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Mozilla Firefox başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge firefox* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove firefox* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove firefox -y --purge")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Mozilla Firefox was uninstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Mozilla Firefox başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        buttonm.destroy()
        spacem.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for Mozilla Firefox browser?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            text1.config(text="Mozilla Firefox internet tarayıcısı için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
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
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Brave was installed.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Brave başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall brave-browser -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall brave-browser -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install brave -y --rei")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Brave was reinstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Brave başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge brave-browser* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove brave-browser* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove brave -y --purge")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Brave rwas uninstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Brave başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        buttonm.destroy()
        spacem.destroy()
        button_1.destroy()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for Brave browser?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            text1.config(text="Brave internet tarayıcısı için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def vlc():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install vlc -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install vlc -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install vlc -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! VLC was installed.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","VLC başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall vlc -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall vlc -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install vlc -y --rei")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! VLC was reinstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","VLC başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge vlc* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove vlc* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove vlc -y --purge")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! VLC was uninstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","VLC başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        buttonm.destroy()
        spacem.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for VLC media player?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            text1.config(text="VLC medya oynatıcıs için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
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
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! LibreOffice was installed.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","LibreOffice başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall libreoffice libreoffice-l10n-tr libreoffice-help-tr -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall libreoffice -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install libtreoffice -y --rei")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! LibreOffice was reinstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","LibreOffice başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge libreoffice* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove libreoffice* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove libreoffice -y --purge")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! LibreOffice was uninstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","LibreOffice başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        buttonm.destroy()
        spacem.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for LibreOffice office suite?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            text1.config(text="LibreOffice ofis programı için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def cups():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install cups -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install cups -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install cups -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Cups was installed.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Cups başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall cups -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall cups -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install cups -y --rei")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Cups was reinstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Cups başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge cups* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove cups* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove cups -y --purge")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Cups was uninstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Cups başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        buttonm.destroy()
        spacem.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for Cups printer manager?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            text1.config(text="Cups yazıcı yöneticisi için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def gparted():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install gparted -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install gparted -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install gparted -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! GParted was installed.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","GParted başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall gparted -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall gparted -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install gparted -y --rei")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! GParted was reinstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","GParted başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge gparted* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove gparted* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove gparted -y --purge")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! GParted was uninstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","GParted başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        buttonm.destroy()
        spacem.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for GParted disk part editor?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            text1.config(text="GParted disk bölümü düzenleyicisi için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def gimp():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install gimp -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install gimp -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install gimp -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! GIMP was installed.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","GIMP başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall gimp -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall gimp -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install gimp -y --rei")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! GIMP was reinstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","GIMP başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge gimp* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove gimp* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove gimp -y --purge")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! GIMP was uninstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","GIMP başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        buttonm.destroy()
        spacem.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for GIMP image manipulation?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            text1.config(text="GIMP görüntü işleme programı için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def wine():
        def it():
            if os.path.isfile(debian):
                os.system(" dpkg --add-architecture i386")
                os.system(" apt install wine-stable -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install wine -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install wine -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Wine was installed.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Wine başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall wine -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall wine -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install wine -y --rei")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Wine was reinstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Wine başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge wine-stable* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove wine* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove wine -y --purge")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Wine was uninstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Wine başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        buttonm.destroy()
        spacem.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for Wine?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            text1.config(text="Wine için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def plank():
        def it():
            if os.path.isfile(debian):
                os.system(" apt install plank -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install plank -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install plank -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Plank was installed.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Plank başarıyla kuruldu.")
        def reit():
            if os.path.isfile(debian):
                os.system(" apt reinstall plank -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall plank -y")
            elif os.path.isfile(solus):
                os.system(" eopkg install plank -y --rei")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Plank was reinstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Plank başarıyla yeniden kuruldu.")
        def rm():
            if os.path.isfile(debian):
                os.system(" apt purge plank* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove plank* -y")
            elif os.path.isfile(solus):
                os.system(" eopkg remove plank -y --purge")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Plank was uninstalled.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Plank başarıyla kaldırıldı.")
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        buttonm.destroy()
        spacem.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for Plank dock?")
            button1.config(text="Install", command=it)
            button2.config(text="Reinstall", command=reit)
            button3.config(text="Uninstall", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            text1.config(text="Plank rıhtımı için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=it)
            button2.config(text="Yeniden kur", command=reit)
            button3.config(text="Kaldır", command=rm)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    def mukonqi():
        def mukander():
            def install():
                if os.path.isfile(debian):
                    os.system("sudo apt install git python3 -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install git python3 -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install git python3 -y")
                os.system("cd /usr/local/bin/ ; git clone https://github.com/MuKonqi/mukander tempmxpas ; cd tempmxpas ; python3 apiutaller.py --install ; cd .. ; rm -rf tempmxpas")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Succesfull! Mukander was installed.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Mukander başarıyla kuruldu.")
            def reinstall():
                if os.path.isfile(debian):
                    os.system("sudo apt install git python3 -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install git python3 -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install git python3 -y")
                os.system("cd /usr/local/bin/ ; git clone https://github.com/MuKonqi/mukander tempmxpas ; cd tempmxpas ; python3 apiutaller.py --reinstall ; cd .. ; rm -rf tempmxpas")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Succesfull! Mukander was reinstalled.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Mukander başarıyla yeniden kuruldu.")
            def uninstall():
                os.system("cd /usr/local/bin/mukander/apiutaller ; python3 apiutaller.py --uninstall")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Succesfull! Mukander was uninstalled.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Mukander başarıyla kaldırıldı.")
            mwindow=Tk(className="MetterXP")
            mwindow.config(background=bg)
            mwindow.resizable(0, 0)
            mwindow.geometry("483x483")
            mparent = Frame(mwindow)
            mparent.pack(expand=1)
            if os.path.isfile(en):
                mwindow.title("Mukander - Application store | MetterXP")
                mtext1=Label(mparent, background=bg, foreground=fg, font="arial 11 bold italic", text="What do you want to do for Mukander?")
                mspace1=Label(mparent, background=bg, foreground=fg, text="\n", font="arial 3")
                mbutton1=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Install",command=install)
                mbutton2=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Reinstall",command=reinstall)
                mbutton3=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Uninstall",command=uninstall)     
            elif os.path.isfile(tr):
                mwindow.title("Mukander - Uygulama mağazası | MetterXP")
                mtext1=Label(mparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Mukander için ne yapmak istersiniz?")
                mspace1=Label(mparent, background=bg, foreground=fg, text="\n", font="arial 3")
                mbutton1=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Kur",command=install)
                mbutton2=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Yeniden kur",command=reinstall)
                mbutton3=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Kaldır",command=uninstall)         
            mtext1.pack(fill="x")
            mspace1.pack(fill="x")
            mbutton1.pack(fill="x")
            mbutton2.pack(fill="x")
            mbutton3.pack(fill="x")
        def mukotes():
            def install():
                if os.path.isfile(debian):
                    os.system("sudo apt install git python3 -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install git python3 -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install git python3 -y")
                os.system("cd /usr/local/bin/ ; git clone https://github.com/MuKonqi/mukotes tempmxpas ; cd tempmxpas ; python3 apiutaller.py --install ; cd .. ; rm -rf tempmxpas")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Succesfull! Mukotes was installed.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Mukotes başarıyla kuruldu.")
            def reinstall():
                if os.path.isfile(debian):
                    os.system("sudo apt install git python3 -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install git python3 -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install git python3 -y")
                os.system("cd /usr/local/bin/ ; git clone https://github.com/MuKonqi/mukotes tempmxpas ; cd tempmxpas ; python3 apiutaller.py --reinstall ; cd .. ; rm -rf tempmxpas")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Succesfull! Mukotes was reinstalled.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Mukotes başarıyla yeniden kuruldu.")
            def uninstall():
                os.system("cd /usr/local/bin/mukotes/apiutaller ; python3 apiutaller.py --uninstall")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Succesfull! Mukotes was uninstalled.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Mukotes başarıyla kaldırıldı.")
            mwindow=Tk(className="MetterXP")
            mwindow.config(background=bg)
            mwindow.resizable(0, 0)
            mwindow.geometry("483x483")
            mparent = Frame(mwindow)
            mparent.pack(expand=1)
            if os.path.isfile(en):
                mwindow.title("Mukotes - Application store | MetterXP")
                mtext1=Label(mparent, background=bg, foreground=fg, font="arial 11 bold italic", text="What do you want to do for Mukotes?")
                mspace1=Label(mparent, background=bg, foreground=fg, text="\n", font="arial 3")
                mbutton1=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Install",command=install)
                mbutton2=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Reinstall",command=reinstall)
                mbutton3=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Uninstall",command=uninstall)     
            elif os.path.isfile(tr):
                mwindow.title("Mukotes - Uygulama mağazası | MetterXP")
                mtext1=Label(mparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Mukotes için ne yapmak istersiniz?")
                mspace1=Label(mparent, background=bg, foreground=fg, text="\n", font="arial 3")
                mbutton1=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Kur",command=install)
                mbutton2=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Yeniden kur",command=reinstall)
                mbutton3=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Kaldır",command=uninstall)     
            mtext1.pack(fill="x")
            mspace1.pack(fill="x")
            mbutton1.pack(fill="x")
            mbutton2.pack(fill="x")
            mbutton3.pack(fill="x")
        def muktart():
            def install():
                if os.path.isfile(debian):
                    os.system("sudo apt install git python3 -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install git python3 -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install git python3 -y")
                os.system("cd /usr/local/bin/ ; git clone https://github.com/MuKonqi/muktart tempmxpas ; cd tempmxpas ; python3 apiutaller.py --install ; cd .. ; rm -rf tempmxpas")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Succesfull! Muktart was installed.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Muktart başarıyla kuruldu.")
            def reinstall():
                if os.path.isfile(debian):
                    os.system("sudo apt install git python3 -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install git python3 -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install git python3 -y")
                os.system("cd /usr/local/bin/ ; git clone https://github.com/MuKonqi/muktart tempmxpas ; cd tempmxpas ; python3 apiutaller.py --reinstall ; cd .. ; rm -rf tempmxpas")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Succesfull! Muktart was reinstalled.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Muktart başarıyla yeniden kuruldu.")
            def uninstall():
                os.system("cd /usr/local/bin/muktart/apiutaller ; python3 apiutaller.py --uninstall")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Succesfull! Muktart was uninstalled.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Muktart başarıyla kaldırıldı.")
            mwindow=Tk(className="MetterXP")
            mwindow.config(background=bg)
            mwindow.resizable(0, 0)
            mwindow.geometry("483x483")
            mparent = Frame(mwindow)
            mparent.pack(expand=1)
            if os.path.isfile(en):
                mwindow.title("Muktart - Application store | MetterXP")
                mtext1=Label(mparent, background=bg, foreground=fg, font="arial 11 bold italic", text="What do you want to do for Muktart?")
                mspace1=Label(mparent, background=bg, foreground=fg, text="\n", font="arial 3")
                mbutton1=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Install",command=install)
                mbutton2=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Reinstall",command=reinstall)
                mbutton3=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Uninstall",command=uninstall)     
            elif os.path.isfile(tr):
                mwindow.title("Muktart - Uygulama mağazası | MetterXP")
                mtext1=Label(mparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Muktart için ne yapmak istersiniz?")
                mspace1=Label(mparent, background=bg, foreground=fg, text="\n", font="arial 3")
                mbutton1=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Kur",command=install)
                mbutton2=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Yeniden kur",command=reinstall)
                mbutton3=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Kaldır",command=uninstall)                
            mtext1.pack(fill="x")
            mspace1.pack(fill="x")
            mbutton1.pack(fill="x")
            mbutton2.pack(fill="x")
            mbutton3.pack(fill="x")
        def projgit():
            def install():
                if os.path.isfile(debian):
                    os.system("sudo apt install git python3 -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install git python3 -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install git python3 -y")
                os.system("cd /usr/local/bin/ ; git clone https://github.com/MuKonqi/projgit tempmxpas ; cd tempmxpas ; python3 apiutaller.py --install ; cd .. ; rm -rf tempmxpas")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Succesfull! Projgit was installed.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Projgit başarıyla kuruldu.")
            def reinstall():
                if os.path.isfile(debian):
                    os.system("sudo apt install git python3 -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install git python3 -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install git python3 -y")
                os.system("cd /usr/local/bin/ ; git clone https://github.com/MuKonqi/projgit tempmxpas ; cd tempmxpas ; python3 apiutaller.py --reinstall ; cd .. ; rm -rf tempmxpas")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Succesfull! Projgit was reinstalled.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Projgit başarıyla yeniden kuruldu.")
            def uninstall():
                os.system("cd /usr/local/bin/projgit/apiutaller ; python3 apiutaller.py --uninstall")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Succesfull! Projgit was uninstalled.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Projgit başarıyla kaldırıldı.")
            mwindow=Tk(className="MetterXP")
            mwindow.config(background=bg)
            mwindow.resizable(0, 0)
            mwindow.geometry("483x483")
            mparent = Frame(mwindow)
            mparent.pack(expand=1)
            if os.path.isfile(en):
                mwindow.title("Projgit - Application store | MetterXP")
                mtext1=Label(mparent, background=bg, foreground=fg, font="arial 11 bold italic", text="What do you want to do for Projgit?")
                mspace1=Label(mparent, background=bg, foreground=fg, text="\n", font="arial 3")
                mbutton1=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Install",command=install)
                mbutton2=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Reinstall",command=reinstall)
                mbutton3=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Uninstall",command=uninstall)     
            elif os.path.isfile(tr):
                mwindow.title("Projgit - Uygulama mağazası | MetterXP")
                mtext1=Label(mparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Projgit için ne yapmak istersiniz?")
                mspace1=Label(mparent, background=bg, foreground=fg, text="\n", font="arial 3")
                mbutton1=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Kur",command=install)
                mbutton2=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Yeniden kur",command=reinstall)
                mbutton3=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Kaldır",command=uninstall)                
            mtext1.pack(fill="x")
            mspace1.pack(fill="x")
            mbutton1.pack(fill="x")
            mbutton2.pack(fill="x")
            mbutton3.pack(fill="x")
        def yasfetch():
            def install():
                if os.path.isfile(debian):
                    os.system("sudo apt install git python3 -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install git python3 -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install git python3 -y")
                os.system("cd /usr/local/bin/ ; git clone https://github.com/MuKonqi/yasfetch tempmxpas ; cd tempmxpas ; python3 apiutaller.py --install ; cd .. ; rm -rf tempmxpas")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Succesfull! Yasfetch was installed.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Yasfetch başarıyla kuruldu.")
            def reinstall():
                if os.path.isfile(debian):
                    os.system("sudo apt install git python3 -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install git python3 -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install git python3 -y")
                os.system("cd /usr/local/bin/ ; git clone https://github.com/MuKonqi/yasfetch tempmxpas ; cd tempmxpas ; python3 apiutaller.py --reinstall ; cd .. ; rm -rf tempmxpas")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Succesfull! Yasfetch was reinstalled.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Yasfetch başarıyla yeniden kuruldu.")
            def uninstall():
                os.system("cd /usr/local/bin/yasfetch/apiutaller ; python3 apiutaller.py --uninstall")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Succesfull! Yasfetch was uninstalled.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Yasfetch başarıyla kaldırıldı.")
            mwindow=Tk(className="MetterXP")
            mwindow.config(background=bg)
            mwindow.resizable(0, 0)
            mwindow.geometry("483x483")
            mparent = Frame(mwindow)
            mparent.pack(expand=1)
            if os.path.isfile(en):
                mwindow.title("Yasfetch - Application store | MetterXP")
                mtext1=Label(mparent, background=bg, foreground=fg, font="arial 11 bold italic", text="What do you want to do for Yasfetch?")
                mspace1=Label(mparent, background=bg, foreground=fg, text="\n", font="arial 3")
                mbutton1=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Install",command=install)
                mbutton2=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Reinstall",command=reinstall)
                mbutton3=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Uninstall",command=uninstall)     
            elif os.path.isfile(tr):
                mwindow.title("Yasfetch - Uygulama mağazası | MetterXP")
                mtext1=Label(mparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Yasfetch için ne yapmak istersiniz?")
                mspace1=Label(mparent, background=bg, foreground=fg, text="\n", font="arial 3")
                mbutton1=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Kur",command=install)
                mbutton2=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Yeniden kur",command=reinstall)
                mbutton3=Button(mparent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Kaldır",command=uninstall)                
            mtext1.pack(fill="x")
            mspace1.pack(fill="x")
            mbutton1.pack(fill="x")
            mbutton2.pack(fill="x")
            mbutton3.pack(fill="x")
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        buttonm.destroy()
        spacem.destroy()
        button_1.destroy()
        button_2.destroy()
        if os.path.isfile(en):
            text1.config(text="Please select a application.")
            button1.config(text="Mukander\nsimple command starter", command=mukander)
            button2.config(text="Mukotes\nsimple note editor", command=mukotes)
            button3.config(text="Muktart\nsimple application starter", command=muktart)
            button4.config(text="Projgit\npublishing changes in Git repositories", command=projgit)
            button5.config(text="Yasfetch\ngetting system information", command=yasfetch)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            text1.config(text="Lütfen bir uygulama seçin.")
            button1.config(text="Mukander\nbasit komut başlatıcısı", command=mukander)
            button2.config(text="Mukotes\nbasit not editörü", command=mukotes)
            button3.config(text="Muktart\nbasit uygulama başlatıcısı", command=muktart)
            button4.config(text="Projgit\nGit depolarında değişiklik yayınlama", command=projgit)
            button5.config(text="Yasfetch\nsistem bilgisini alma", command=yasfetch)
            button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_3.pack(fill="x")
    if os.path.isfile(en):
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Which program do you want to install or reinstall or remove?")
        space1=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        buttonm=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Some other apps from developer\n[MuKonqi (Muhammed Abdurrahman)",command=mukonqi)
        spacem=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        button1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Mozilla Firefox browser",command=firefox)
        button2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Brave browser",command=brave)
        button3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="VLC media player",command=vlc)
        button4=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="LibreOffice office suite",command=libreoffice)
        button5=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Cups printer manager",command=cups)
        button6=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="GParted disk part editor",command=gparted)
        button7=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="GIMP image manipulation",command=gimp)
        button8=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Wine",command=wine)
        button9=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Plank dock",command=plank)
        space2=Label(parent, background=bg, foreground=fg, text="\n", font="arial 1")
        button_1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Other", command=to_other)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Flatpak", command=to_flatpak)    
    elif os.path.isfile(tr):    
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Hangi programı kurmak veya yeniden kurmak veya kaldırmak istiyorsunuz?")
        space1=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        buttonm=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Geliştiricinin [MuKonqi (Muhammed Abdurrahman)]\ndiğer bazı uygulamaları",command=mukonqi)
        spacem=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        button1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Mozilla Firefox internet tarayıcısı",command=firefox)
        button2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Brave internet tarayıcısı",command=brave)
        button3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="VLC medya oynatıcısı",command=vlc)
        button4=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="LibreOffice ofis programı",command=libreoffice)
        button5=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Cups yazıcı yöneticisi",command=cups)
        button6=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="GParted disk bölümü düzenleyicisi",command=gparted)
        button7=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="GIMP görüntü işleme programı",command=gimp)
        button8=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Wine",command=wine)
        button9=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Plank rıhtımı",command=plank)
        space2=Label(parent, background=bg, foreground=fg, text="\n", font="arial 1")
        button_1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Diğer", command=to_other)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Flatpak", command=to_flatpak)
    text1.pack(fill="x")
    space1.pack(fill="x")
    buttonm.pack(fill="x")
    spacem.pack(fill="x")
    button1.pack(fill="x")
    button2.pack(fill="x")
    button3.pack(fill="x")
    button4.pack(fill="x")
    button5.pack(fill="x")
    button6.pack(fill="x")
    button7.pack(fill="x")
    button8.pack(fill="x")
    button9.pack(fill="x")
    space2.pack(fill="x")
    button_1.pack(fill="x")
    button_2.pack(fill="x")

def flatpak():
    if not os.path.isfile("/usr/bin/flatpak") or not os.path.isfile("/bin/flatpak"):
        if os.path.isfile(en):
            messagebox.showwarning("Warning","Flatpak can't found. When you click 'OK', package manager installer will be open.")
        elif os.path.isfile(tr):
            messagebox.showwarning("Uyarı","Flatpak bulunamadı. 'OK' tuşuna bastığınızda paket yöneticisi yükleyicisi açılacaktır.")
        window.destroy()
        os.system("pkexec /usr/bin/metterxp pm_it")
    def packageit():
        if packagename.get() == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You did not write anything, if you want nstalling a package, please write the package name.")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paketi kuracaksanız lütfen paket adını yazın.")
            return
        c1_package="flatpak install "
        get_packagename=packagename.get()
        c2_package=" -y"
        cf_package=c1_package+get_packagename+c2_package
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return    
        window_2=Toplevel()
        if os.path.isfile(en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)
        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x") 
    def packagereit():
        if packagename.get() == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You did not write anything, if you want reinstalling a package, please write the package name.")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paketi yeniden kuracaksanız lütfen paket adını yazın.")
            return
        c1_package="flatpak install "
        get_packagename=packagename.get()
        c2_package=" -y --reinstall"
        cf_package=c1_package+get_packagename+c2_package
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return    
        window_2=Toplevel()
        if os.path.isfile(en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)
        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x")      
    def packagerm():
        if packagename.get() == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You did not write anything, if you want uninstalling a package please write the package name.")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paket kaldıracaksınız lütfen paket adını yazın.")
            return
        c1_package="flatpak uninstall "
        get_packagename=packagename.get()
        c2_package=" -y"
        cf_package=c1_package+get_packagename+c2_package
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return    
        window_2=Toplevel()
        if os.path.isfile(en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)
        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x") 
    def packagesearch():
        if packagename.get() == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You did not write anything, if you want searching a package, please write the package name.")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paket aratacaksınız lütfen paket adını yazın.")
            return
        c1_package="flatpak search "
        get_packagename=packagename.get()
        cf_package=c1_package+get_packagename
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return
        window_2=Toplevel()
        if os.path.isfile(en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)

        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x")        
    if os.path.isfile(en):
        text2=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Please enter the Flatpak package name.")
        space4=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        packagename=Entry(parent)
        b_packageit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Install",command=packageit)
        b_packagereit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Reinstall",command=packagereit)
        b_packagerm=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Uninstall",command=packagerm)
        b_packagesearch=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Seacrh",command=packagesearch)
        space5=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        reopen_button_1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Back to menu", command=reopen)
    elif os.path.isfile(tr):
        text2=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic italic", text="Lütfen Flatpak paketi adı giriniz.")
        space4=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        packagename=Entry(parent)
        b_packageit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Kur",command=packageit)
        b_packagereit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Yeniden kur",command=packagereit)
        b_packagerm=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Kaldır",command=packagerm)
        b_packagesearch=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Ara",command=packagesearch)
        space5=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        reopen_button_1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Menüye dön", command=reopen)
    text2.pack(fill="x")
    space4.pack(fill="x")
    packagename.pack(fill="x")
    b_packageit.pack(fill="x")
    b_packagereit.pack(fill="x")
    b_packagerm.pack(fill="x")
    b_packagesearch.pack(fill="x")
    space5.pack(fill="x")
    reopen_button_1.pack(fill="x")

def other():
    def packageit():
        if packagename.get() == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You did not write anything, if you want nstalling a package, please write the package name.")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paketi kuracaksanız lütfen paket adını yazın.")
            return
        if os.path.isfile(debian):
            c1_package=" apt install "
            get_packagename=packagename.get()
            c2_package=" -y"
        elif os.path.isfile(fedora):
            c1_package=" dnf install "
            get_packagename=packagename.get()
            c2_package=" -y"
        elif os.path.isfile(solus):
            c1_package=" eopkg install "
            get_packagename=packagename.get()
            c2_package=" -y"
        cf_package=c1_package+get_packagename+c2_package
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return    
        window_2=Toplevel()
        if os.path.isfile(en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)
        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x") 
    def packagereit():
        if packagename.get() == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You did not write anything, if you want reinstalling a package, please write the package name.")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paketi yeniden kuracaksanız lütfen paket adını yazın.")
            return
        if os.path.isfile(debian):
            c1_package=" apt reinstall "
            get_packagename=packagename.get()
            c2_package=" -y"
        elif os.path.isfile(fedora):
            c1_package=" dnf reinstall "
            get_packagename=packagename.get()
            c2_package=" -y"
        elif os.path.isfile(solus):
            c1_package=" eopkg install "
            get_packagename=packagename.get()
            c2_package=" -y --rei"
        cf_package=c1_package+get_packagename+c2_package
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return    
        window_2=Toplevel()
        if os.path.isfile(en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)
        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x")      
    def packagerm():
        if packagename.get() == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You did not write anything, if you want uninstalling a package please write the package name.")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paket kaldıracaksınız lütfen paket adını yazın.")
            return
        if os.path.isfile(debian):
            c1_package=" apt purge "
            get_packagename=packagename.get()
            c2_package="* -y"
        elif os.path.isfile(fedora):
            c1_package=" dnf remove "
            get_packagename=packagename.get()
            c2_package="* -y"
        elif os.path.isfile(solus):
            c1_package=" eopkg remove "
            get_packagename=packagename.get()
            c2_package=" -y --purge"
        cf_package=c1_package+get_packagename+c2_package
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return    
        window_2=Toplevel()
        if os.path.isfile(en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)
        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x") 
    def packagesearch():
        if packagename.get() == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You did not write anything, if you want searching a package, please write the package name.")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Bir şey yazmadınız, eğer paket aratacaksınız lütfen paket adını yazın.")
            return
        if os.path.isfile(debian):
            c1_package="apt search "
        elif os.path.isfile(fedora):
            c1_package="dnf search "
        elif os.path.isfile(solus):
            c1_package="eopkg search "
        get_packagename=packagename.get()
        cf_package=c1_package+get_packagename
        run_cf_package = subprocess.Popen(cf_package, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
        if out == "":
            if os.path.isfile(en):
                messagebox.showerror("User Error","You entered the wrong package name, try again!")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Paket adını yanlış girdiniz, tekrar deneyin!")
            return
        window_2=Toplevel()
        if os.path.isfile(en):
            window_2.title("Output - Application installation wizard | MetterXP")
        elif os.path.isfile(tr):
            window_2.title("Çıktı - Uygulama mağazası | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Text(window_2, yscrollcommand=scroll.set)
        text3.insert(END, out)
        scroll.config(command=text3.yview)
        scroll.pack(side=RIGHT,fill=Y)
        text3.config(state=DISABLED)
        text3.pack(fill="x")        
    if os.path.isfile(en):
        text2=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Please enter the name package name.")
        space4=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        packagename=Entry(parent)
        b_packageit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Install",command=packageit)
        b_packagereit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Reinstall",command=packagereit)
        b_packagerm=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Uninstall",command=packagerm)
        b_packagesearch=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Seacrh",command=packagesearch)
        space5=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        reopen_button_1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Back to menu", command=reopen)
    elif os.path.isfile(tr):
        text2=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic italic", text="Lütfen paket adı giriniz.")
        space4=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        packagename=Entry(parent)
        b_packageit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Kur",command=packageit)
        b_packagereit=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Yeniden kur",command=packagereit)
        b_packagerm=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Kaldır",command=packagerm)
        b_packagesearch=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="4", background=button_bg, text="Ara",command=packagesearch)
        space5=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        reopen_button_1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Menüye dön", command=reopen)
    text2.pack(fill="x")
    space4.pack(fill="x")
    packagename.pack(fill="x")
    b_packageit.pack(fill="x")
    b_packagereit.pack(fill="x")
    b_packagerm.pack(fill="x")
    b_packagesearch.pack(fill="x")
    space5.pack(fill="x")
    reopen_button_1.pack(fill="x")


main()
mainloop()