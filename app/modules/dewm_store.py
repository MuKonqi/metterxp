#!/usr/bin/env python3

# Copyright (C) 2021, 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os
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
    os.system("pkexec /usr/bin/metterxp dewm_store")

def reboot():
    os.system("reboot now")


window=Tk(className="MetterXP")
if os.path.isfile(en):
    window.title("Desktop Environment and Window Manager store | MetterXP")
elif os.path.isfile(tr):
    window.title("Masaüstü Ortamı ve Pencere Yöneticisi mağazası | MetterXP")
window.config(background=bg)
window.resizable(0, 0)
parent = Frame(window)
window.geometry("483x483")
icon = PhotoImage(file="/usr/local/bin/metterxp/icon.png")
window.iconphoto(True, icon)
parent.pack(expand=1)

if os.path.isfile(debian) or os.path.isfile(fedora):
    def kde():
        def install():
            if os.path.isfile(debian):
                os.system(" apt install kde-plasma-desktop -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @kde-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","KDE Plasma installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall kde-plasma-desktop -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @kde-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","KDE Plasma reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge kde-plasma-desktop* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove @kde-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","KDE Plasma uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for KDE Plasma?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="KDE Plasma için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    def gnome():
        def install():
            if os.path.isfile(debian):
                os.system(" apt install gnome gnome-shell -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @gnome-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","GNOME installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","GNOME kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall gnome gnome-shell -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @gnome-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","GNOME reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","GNOME yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge gnome* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove @gnome-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","GNOME uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","GNOME kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for GNOME?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="GNOME için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    def cinnamon():
        def install():
            if os.path.isfile(debian):
                os.system(" apt install cinnamon -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @cinnamon-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Cinnamon installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Cinnamon kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall cinnamon -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @cinnamon-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Cinnamon reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Cinnamon yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge cinnamon* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove @cinnamon-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Cinnamon uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Cinnamon kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for Cinnamon?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="Cinnamon için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    def mate():
        def install():
            if os.path.isfile(debian):
                os.system(" apt install mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @mate-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Mate installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Mate kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @mate-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Mate reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Mate yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge mate-plasma-desktop* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove @mate-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Mate uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Mate kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for Mate?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="Mate için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    def xfce():
        def install():
            if os.path.isfile(debian):
                os.system(" apt install xfce4 -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @xfce-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Xfce installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Xfce kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall xfce4 -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @xfce4-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Xfce reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Xfce yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge xfce4* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove @xfce-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Xfce uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Xfce kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for Xfce?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="Xfce için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    def deepin():
        def install():
            if os.path.isfile(debian):
                os.system(" apt install software-properties-common -y")
                os.system(" add-apt-repository ppa:ubuntudde-dev/stable -y")
                os.system(" apt update -y")
                os.system(" apt install dde -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @deepin-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Deepin installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Deepin  kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall dde -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @deepin-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Deepin reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Deepin yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge dde* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove @deepin-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Deepin uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Deepin kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for Deepin?\nNote: The process of installing Deepin is not completely stable.")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="Deepin için ne yapmak istiyorsunuz?\nNot: Deepin 'i kurma işlemi tamamen stabil değildir.")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    def lxde():
        def install():
            if os.path.isfile(debian):
                os.system(" apt install lxde -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @lxde-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","LXDE installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","LXDE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall lxde -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @lxde-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","LXDE reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","LXDE yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge lxde* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove @lxde-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","LXDE uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","LXDE kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for LXDE?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="LXDE için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    def lxqt():
        def install():
            if os.path.isfile(debian):
                os.system(" apt install openbox pcmanfm-qt lxqt-admin lxqt-common lxqt-config lxqt-globalkeys lxqt-notificationd lxqt-panel lxqt-policykit lxqt-powermanagement lxqt-qtplugin lxqt-runner lxqt-session -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @kde-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","KDE Plasma installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall openbox pcmanfm-qt lxqt-admin lxqt-common lxqt-config lxqt-globalkeys lxqt-notificationd lxqt-panel lxqt-policykit lxqt-powermanagement lxqt-qtplugin lxqt-runner lxqt-session -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @kde-desktop -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","KDE Plasma reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(fedora):
                def openboxuninstall():
                    os.system(" apt purge openbox* -y")
                    if os.path.isfile(en):
                        messagebox.showinfo("Information","The OpenBox used by LXQthas been uninstalled.\nYour computer will reboot as soon as you click the 'OK' button to apply the changes.")
                    elif os.path.isfile(tr):
                        messagebox.showinfo("Bilgilendirme","LXQt 'in kullandığı OpenBox kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                    reboot()
                os.system(" apt purge pcmanfm-qt lxqt-admin lxqt-common lxqt-config lxqt-globalkeys lxqt-notificationd lxqt-panel lxqt-policykit lxqt-powermanagement lxqt-qtplugin lxqt-runner lxqt-session lxqt- -y")
                if os.path.isfile(en):
                    text1.config(text="Everything has been removed except the OpenBox that LXQt uses.")
                    button1.config(text="Not uninstall OpenBox used by LXQt\nRestart computer immediately", command=reboot)
                    button2.config(text="Uninstall OpenBox used by LXQt\nRestart computer when OpenBox is uninstalled", command=openboxuninstall)
                elif os.path.isfile(tr):
                    text1.config(text="LXQt 'in kullandığı OpenBox hariç her şey kaldırıldı.")
                    button1.config(text="LXQt 'in kullandığı OpenBox'ı kaldırma\nHemen bilgisayarı yeniden başlat", command=reboot)
                    button2.config(text="LXQt 'in kullandığı OpenBox'i kaldır\nOpenBox 'i kaldırılınca bilgisayarı yeniden başlat", command=openboxuninstall)
                button3.destroy()
            elif os.path.isfile(fedora):
                os.system(" dnf remove @lxqt-desktop -y")
                if os.path.isfile(en):
                    messagebox.showinfo("Information","LXQt uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","LXQt kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for LXQt?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="LXQt için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    def openbox():
        def install():
            if os.path.isfile(debian):
                os.system(" apt install openbox -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install openbox obconf -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","OpenBox installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","OpenBox kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall openbox -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall openbox obconf -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","OpenBox reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","OpenBox yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge openbox -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove openbox obconf -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","OpenBox uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","OpenBox kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for OpenBox?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="OpenBox için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    def i3():
        def install():
            if os.path.isfile(debian):
                os.system(" apt install i3 -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install i3 i3status i3lock dmenu -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","i3 installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","i3 kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall i3 -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall i3 i3status i3lock dmenu -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","i3 reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","i3 yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge i3* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove i3 i3status i3lock dmenu -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","i3 uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","i3 kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for i3?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="i3 için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    def pantheon():
        def install():
            os.system(" dnf group install 'pantheon desktop' -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Pantheon installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Pantheon kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            os.system(" dnf group reinstall 'pantheon desktop' -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Pantheon reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Pantheon yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            os.system(" dnf group remove 'pantheon desktop' -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Pantheon uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Pantheon kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for Pantheon?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="Pantheon için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    if os.path.isfile(en):
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Which one do you want to view?")
    elif os.path.isfile(tr):    
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Hangisini görüntülemek istiyorsunuz?")
    text1.pack(fill="x")
    space1=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
    space1.pack(fill="x")
    button1=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="KDE Plasma",command=kde)
    button1.pack(fill="x")
    button2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="GNOME",command=gnome)
    button2.pack(fill="x")
    button3=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Cinnamon",command=cinnamon)
    button3.pack(fill="x")
    button4=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Mate",command=mate)
    button4.pack(fill="x")
    button5=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Xfce",command=xfce)
    button5.pack(fill="x")
    button6=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Deepin",command=deepin)
    button6.pack(fill="x")
    button7=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="LXDE",command=lxde)
    button7.pack(fill="x")
    button8=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="LXQt",command=lxqt)
    button8.pack(fill="x")
    button9=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="OpenBox",command=openbox)
    button9.pack(fill="x")
    button10=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="i3",command=i3)
    button10.pack(fill="x")
    if os.path.isfile(fedora):
        button11=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Pantheon",command=pantheon)
        button11.pack(fill="x")
    
    
if os.path.isfile(solus):
    def kde():
        def install():
            os.system(" eopkg it -c desktop.kde -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","KDE Plasma installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            os.system(" eopkg it -c desktop.kde --rei -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","KDE Plasma reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            os.system(" eopkg rm -c desktop.kde --purge -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","KDE Plasma uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for KDE Plasma?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="KDE Plasma için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    def gnome():
        def install():
            os.system(" eopkg it -c desktop.gnome -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","GNOME installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","GNOME kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            os.system(" eopkg it -c desktop.gnome --rei -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","GNOME reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","GNOME yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            os.system(" eopkg rm -c desktop.gnome --purge -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","GNOME uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","GNOME kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for GNOME?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="GNOME için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    def budgie():
        def install():
            os.system(" eopkg it -c desktop.budgie -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Budgie installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Budgie kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            os.system(" eopkg it -c desktop.budgie --rei -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Budgie reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Budgie yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            os.system(" eopkg rm -c desktop.budgie --purge -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Budgie uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Budgie kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for Budgie?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="Budgie için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    def mate():
        def install():
            os.system(" eopkg it -c desktop.mate -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Mate installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Mate kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            os.system(" eopkg it -c desktop.mate --rei -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Mate reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Mate yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            os.system(" eopkg rm -c desktop.mate --purge -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Mate uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Mate kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for Mate?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="Mate için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")   
    def openbox():
        def install():
            os.system(" eopkg it openbox obconf -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","OpenBox installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","OpenBox  kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            os.system(" eopkg it openbox obconf --rei -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","OpenBox reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","OpenBox yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            os.system(" eopkg rm openbox obconf --purge -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","OpenBox uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","OpenBox kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for OpenBox?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="OpenBox için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    def i3():
        def install():
            os.system(" eopkg it i3 -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","i3 installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","i3 kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            os.system(" eopkg it i3 --rei -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","i3 reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","i3 yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            os.system(" eopkg rm -c i3 --purge -y")
            if os.path.isfile(en):
                messagebox.showinfo("Information","i3 uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","i3 kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            text1.config(text="What do you want to do for i3?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(tr):
            text1.config(text="i3 için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        if os.path.isfile(en):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Back to menu", command=reopen)
        elif os.path.isfile(tr):
            button_2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="4", text="Menüye dön", command=reopen)
        button_2.pack(fill="x")
    if os.path.isfile(en):
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Which one do you want to view?")
    elif os.path.isfile(tr):    
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Hangisini görüntülemek istiyorsunuz?")
    text1.pack(fill="x")
    space1=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
    space1.pack(fill="x")
    button1=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="KDE Plasma",command=kde)
    button1.pack(fill="x")
    button2=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="GNOME",command=gnome)
    button2.pack(fill="x")
    button3=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Budgie",command=budgie)
    button3.pack(fill="x")
    button4=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="Mate",command=mate)
    button4.pack(fill="x")
    button5=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="İ3",command=i3)
    button5.pack(fill="x")
    button6=Button(parent, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="4", text="OpenBox",command=openbox)
    button6.pack(fill="x")

mainloop()