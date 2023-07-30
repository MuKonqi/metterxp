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
    os.system("pkexec /usr/bin/metterxp pm_store "+str(sys.argv[1]))

def reboot():
    os.system("reboot now")


window=Tk(className="MetterXP")
if os.path.isfile(en):
    window.title("Package manager store | MetterXP")
elif os.path.isfile(tr):
    window.title("Paket yöneticisi mağazası | MetterXP")
window.config(background=bg)
window.resizable(0, 0)
window.geometry("350x200")
parent = Frame(window)
parent.pack(expand=1)
icon = PhotoImage(file="/usr/local/bin/metterxp/icon.png")
window.iconphoto(True, icon)

def flatpak():
    window.geometry("365x365")
    def install():
        if os.path.isfile(debian):
            os.system(" apt install flatpak -y")
        elif os.path.isfile(fedora):
            os.system(" dnf install flatpak -y")
        elif os.path.isfile(solus):
            os.system(" eopkg install flatpak -y")
        os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
        if os.path.isfile(en):
            messagebox.showinfo("Information","Process completed. Press the 'OK' button and your computer will restart.")
        elif os.path.isfile(tr):
            messagebox.showinfo("Bilgilendirme","İşlem tamamlandı. 'OK' tuşuna bastığınızda bilgisayarınız yeniden başlatılacak.")
        reboot()
    def reinstall():
        if os.path.isfile(debian):
            os.system(" apt reinstall flatpak -y")
        elif os.path.isfile(fedora):
            os.system(" dnf reinstall flatpak -y")
        elif os.path.isfile(solus):
            os.system(" eopkg install flatpak --rei -y")
        os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
        if os.path.isfile(en):
            messagebox.showinfo("Information","Process completed. Press the 'OK' button and your computer will restart.")
        elif os.path.isfile(tr):
            messagebox.showinfo("Bilgilendirme","İşlem tamamlandı. 'OK' tuşuna bastığınızda bilgisayarınız yeniden başlatılacak.")
        reboot()
    button1.destroy()
    button2.destroy()
    space2.destroy()
    if os.path.isfile(debian):
        def oldubuntuinstall():
            os.system(" add-apt-repository ppa:flatpak/stable")
            os.system(" apt update")
            os.system(" apt install flatpak")
            os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
            if os.path.isfile(en):
                messagebox.showinfo("Information","Process completed. Press the 'OK' button and your computer will restart.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","İşlem tamamlandı. 'OK' tuşuna bastığınızda bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(en):
            flatpakbutton1_1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Install\n(Ubuntu 18.04) and later or based on Debian GNU/Linux)", command=install)
            flatpakbutton1_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Install\n(Ubuntu 17.10) and before)", command=oldubuntuinstall)
        elif os.path.isfile(tr):
            flatpakbutton1_1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Kur\n(Ubuntu 18.04 ve sonrası ya da Debian GNU/Linux'u taban alanlar)", command=install)
            flatpakbutton1_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Kur\n(Ubuntu 17.10 ve öncesini taban alanlar)", command=oldubuntuinstall)
        flatpakbutton1_1.pack(fill="x")
        flatpakbutton1_2.pack(fill="x")
    else:
        if os.path.isfile(en):
            flatpakbutton1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Install", command=install)
        elif os.path.isfile(tr):
            flatpakbutton1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Kur", command=install)
        flatpakbutton1.pack(fill="x")        
    if os.path.isfile(en):
        text1.config(text="What do you want to do for Flatpak?")
        flatpakbutton2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Reinstall",command=reinstall)
        button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Back to menu", command=reopen)
        space3=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")        
    elif os.path.isfile(tr):
        text1.config(text="Flatpak için ne yapmak istiyorsunuz?")
        flatpakbutton2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Yeniden kur",command=reinstall)
        space3=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")    
        button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Menüye dön", command=reopen)
    flatpakbutton2.pack(fill="x")
    space3.pack(fill="x")
    button_3.pack(fill="x")
def snap():
    window.geometry("365x365")
    button1.destroy()
    button2.destroy()
    space2.destroy()
    def install():
        if os.path.isfile(debian):
            os.system(" apt install snapd -y")
        elif os.path.isfile(fedora):
            os.system(" dnf install snapd -y")
        elif os.path.isfile(solus):
            os.system(" eopkg install snapd -y")
        if os.path.isfile(en):
            messagebox.showinfo("Information","Process completed. Press the 'OK' button and your computer will restart.")
        elif os.path.isfile(tr):
            messagebox.showinfo("Bilgilendirme","İşlem tamamlandı. 'OK' tuşuna bastığınızda bilgisayarınız yeniden başlatılacak.")
        reboot()
    def reinstall():
        if os.path.isfile(debian):
            os.system(" apt reinstall snapd -y")
        elif os.path.isfile(fedora):
            os.system(" dnf reinstall snapd -y")
        elif os.path.isfile(solus):
            os.system(" eopkg install snapd --rei -y")
        if os.path.isfile(en):
            messagebox.showinfo("Information","Process completed. Press the 'OK' button and your computer will restart.")
        elif os.path.isfile(tr):
            messagebox.showinfo("Bilgilendirme","İşlem tamamlandı. 'OK' tuşuna bastığınızda bilgisayarınız yeniden başlatılacak.")
        reboot()
    if os.path.isfile(en):
        text1.config(text="What do you want to do for Snap?")
        snapbutton1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Install",command=install)
        snapbutton2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Reinstall",command=reinstall)
        space3=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")        
        button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Back to menu", command=reopen)
    elif os.path.isfile(tr):
        text1.config(text="Snap için ne yapmak istiyorsunuz?")
        snapbutton1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Kur",command=install)
        snapbutton2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Yeniden kur",command=reinstall)
        space3=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
        button_3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Menüye dön", command=reopen)
    snapbutton1.pack(fill="x")
    snapbutton2.pack(fill="x")
    space3.pack(fill="x")
    button_3.pack(fill="x")

if os.path.isfile(en):
    text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="PLease, select a package manager.")
    space1=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
    button1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Flatpak", command=flatpak)
    button2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Snap", command=snap)
elif os.path.isfile(tr):    
    text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Lütfen bir paket yöneticisi seçiniz.")
    space1=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
    button1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Flatpak", command=flatpak)
    button2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Snap", command=snap)
    space2=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
text1.pack(fill="x")
space1.pack(fill="x")
button1.pack(fill="x")
button2.pack(fill="x")

mainloop()