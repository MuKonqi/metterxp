#!/usr/bin/env python3

# Copyright (C) 2021, 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp/settings/lang/en.txt"


def reopen():
    window.destroy()
    os.system("python3 /usr/local/bin/metterxp/modules/distros.py")


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


def mx():
    if os.path.isfile(lang_en):
        text1.config(text="MX Linux is a lightweight distribution based on Debian GNU/Linux and using the Xfce desktop environment by default.\n\nMetterXP's MX Linux support: Available\nWebsite: https://mxlinux.org/")
        button1.config(text="Open link",command=mxopen)
        button2.config(text="Copy link",command=mxcopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Back to menu", command=reopen)
    elif os.path.isfile(lang_tr):
        text1.config(text="MX Linux, Debian GNU/Linux tabanlı ve varsayılan olarak Xfce masaüstü ortamını kullanan hafif bir dağıtımdır.\n\nMetterXP'ın MX Linux desteği: Mevcut\nİnternet sitesi: https://mxlinux.org/")
        button1.config(text="Bağlantıyı aç",command=mxopen)
        button2.config(text="Bağlantıyı kopyala",command=mxcopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Menüye dön", command=reopen)
    button_2.pack(fill="x")
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
def mxopen():
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Links cannot be opened while rooted.")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
    if not os.getuid() == 0:
        os.system("xdg-open https://mxlinux.org")
def mxcopy():
    window.clipboard_append("https://mxlinux.org")
    window.update()
def manjaro():
    if os.path.isfile(lang_en):
        text1.config(text="Manjaro is an Arch Linux based and end user oriented distribution.\nManjaro has its own tools. For example: Pamac\n\nMetterXP's Manjaro support: Not available\nWebsite: https://manjaro.org/")
        button1.config(text="Open link",command=manjaroopen)
        button2.config(text="Copy link",command=manjarocopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Back to menu", command=reopen) 
    elif os.path.isfile(lang_tr):
        text1.config(text="Manjaro, Arch Linux tabanlı ve son kullanıcı odaklı bir dağıtımdır.\nManjaro'nun kendisine ait araçları vardır. Örneğin: Pamac\n\nMetterXP'ın Manjaro desteği: Mevcut değil\nİnternet sitesi: https://manjaro.org/")
        button1.config(text="Bağlantıyı aç",command=manjaroopen)
        button2.config(text="Bağlantıyı kopyala",command=manjarocopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Menüye dön", command=reopen)
    button_2.pack(fill="x")   
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
def manjaroopen():
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Links cannot be opened while rooted.")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
    if not os.getuid() == 0:
        os.system("xdg-open https://manjaro.org") 
def manjarocopy():
    window.clipboard_append("https://manjaro.org")
    window.update()
def mint():
    if os.path.isfile(lang_en):
        text1.config(text="Linux Mint is an Ubuntu-based, end-user focused distribution.\nLinux Mint uses its own desktop environment, Cinnamon, by default, but also offers Mate and Xfce desktop environment options.\n\nMetterXP's Linux Mint support: Available\nWebsite: https://linuxmint.com/")
        button1.config(text="Open link",command=mintopen)
        button2.config(text="Copy link",command=mintcopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Back to menu", command=reopen)
    elif os.path.isfile(lang_tr):    
        text1.config(text="Linux Mint, Ubuntu tabanlı, son kullanıcı odaklı bir dağıtımdır.\nLinux Mint, kendi masaüstü ortamı olan Cinnamon'u varsayılan olarak kullanmasıyla beraber Mate ve Xfce masaüstü ortamı seçeneklerini de sunar.\n\nMetterXP'ın Linux Mint desteği: Mevcut\nİnternet sitesi: https://linuxmint.com/")
        button1.config(text="Bağlantıyı aç",command=mintopen)
        button2.config(text="Bağlantıyı kopyala",command=mintcopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Menüye dön", command=reopen)
    button_2.pack(fill="x")
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    button_2.pack(fill="x")
def mintopen():
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Links cannot be opened while rooted.")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
    if not os.getuid() == 0:
        os.system("xdg-open https://linuxmint.com")
def mintcopy():
    window.clipboard_append("https://linuxmint.com")
    window.update()
def ubuntu():
    if os.path.isfile(lang_en):
        text1.config(text="Ubuntu is one of the most popular GNU/Linux distributions developed by Canonical and based on Debian GNU/Linux.\nUbuntu uses GNOME as its default desktop environment. Alternative desktop environments for Ubuntu have been published by the community.\n\nMetterXP's Ubuntu support: Available\nWebsite: https://ubuntu.com/")
        button1.config(text="Open link",command=ubuntuopen)
        button2.config(text="Copy link",command=ubuntucopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Back to menu", command=reopen)
    elif os.path.isfile(lang_tr):
        text1.config(text="Ubuntu, Canonical tarafından geliştirilen ve Debian GNU/Linux tabanlı en pöpüler GNU/Linux dağıtımlarından biridir.\nUbuntu, GNOME'u varsayılan masaüstü ortamı olarak kullanır. Ubuntu için alternatif masaüstü ortamları topluluk tarafından yayınlanmıştır.\n\nMetterXP'ın Ubuntu desteği: Mevcut\nİnternet sitesi: https://ubuntu.com/")
        button1.config(text="Bağlantıyı aç",command=ubuntuopen)
        button2.config(text="Bağlantıyı kopyala",command=ubuntucopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Menüye dön", command=reopen)
    button_2.pack(fill="x")
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
def ubuntuopen():
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Links cannot be opened while rooted.")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
    if not os.getuid() == 0:
        os.system("xdg-open https://ubuntu.com")
def ubuntucopy():
    window.clipboard_append("https://ubuntu.com")
    window.update()
def debian_():
    if os.path.isfile(lang_en):
        text1.config(text="It is one of the first and is indedepent.\nIt uses dpkg.\nMany distributions are based on Debian.\nPackages in the Stable repository are not very up-to-date.\nPackages in other repository are more up-to-date than Stable.\n\nMetterXP's Debian GNU/Linux support: Available\nWebsite: https://www.debian.org/")
        button1.config(text="Open link",command=debianopen)
        button2.config(text="Copy link",command=debiancopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Back to menu", command=reopen)
    elif os.path.isfile(lang_tr):
        text1.config(text="İlk çıkanlardan birisidir ve bağımsızdır.\ndpkg kullanmaktadır.\nBir çok dağıtım, Debian'ı taban almaktadır.\nStable deposundaki paketler çok güncel değildir.\nDiğer depolardaki paketler, Stable'dan daha günceldir.\n\nMetterXP'ın Debian GNU/Linux desteği: Mevcut\nİnternet sitesi: https://www.debian.org/")
        button1.config(text="Bağlantıyı aç",command=debianopen)
        button2.config(text="Bağlantıyı kopyala",command=debiancopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Menüye dön", command=reopen)
    button_2.pack(fill="x")
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
def debianopen():
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Links cannot be opened while rooted.")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
    if not os.getuid() == 0:
        os.system("xdg-open https://www.debian.org")     
def debiancopy():
    window.clipboard_append("https://www.debian.org")
    window.update()
def elementary():
    if os.path.isfile(lang_en):
        text1.config(text="ElementaryOS is based on Debian GNU/Linux and uses its own desktop environment, Pantheon, by default.\n\nMetterXP's ElementaryOS support: Available\nWebsite: https://elementary.io/" )
        button1.config(text="Open link",command=elementaryopen)
        button2.config(text="Copy link",command=elementarycopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Back to menu", command=reopen)
    elif os.path.isfile(lang_tr):
        text1.config(text="ElementaryOS, Debian GNU/Linux tabanlı olup, kendi masaüstü ortamı olan Pantheon'u varsayılan olarak kullanır.\n\nMetterXP'ın ElementaryOS desteği: Mevcut\nİnternet sitesi: https://elementary.io/")
        button1.config(text="Bağlantıyı aç",command=elementaryopen)
        button2.config(text="Bağlantıyı kopyala",command=elementarycopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Menüye dön", command=reopen)
    button_2.pack(fill="x")
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
def elementaryopen():
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Links cannot be opened while rooted.")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
    if not os.getuid() == 0:
        os.system("xdg-open https://elementary.io")
def elementarycopy():
    window.clipboard_append("https://elementary.io")
    window.update()
def solus_():
    if os.path.isfile(lang_en):
        text1.config(text="nIt is a indedepent distribution.\nIt uses EOPKG, it is fork of PiSi from not Debian based Pardus.\nIt has semi-rolling release logic.\nAfter the changes in the developer team, 4.4 was released about 2 years after 4.3.\n\nMetterXP's Solus support: Available\nWebsite: https://getsol.us/home/")
        button1.config(text="Open link",command=solusopen)
        button2.config(text="Copy link",command=soluscopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Back to menu", command=reopen)
    elif os.path.isfile(lang_tr):
        text1.config(text="Bağımsız bir dağıtımdır.\nDebian'dan önceki Pardus'ta kullanılan PiSi'ın çatalı EOPKG'i kullanır.\nYarı yuvarlanan sürüm mantığına sahiptir.\nGeliştirici takımındaki değişiklikler sonrası 4.3'ten yaklaşık 2 yıl sonra 4.4 çıkmıştır\n\nMetterXP'ın Solus desteği: Mecvut\nİnternet sitesi: https://getsol.us/home/")
        button1.config(text="Bağlantıyı aç",command=solusopen)
        button2.config(text="Bağlantıyı kopyala",command=soluscopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Menüye dön", command=reopen)
    button_2.pack(fill="x")
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
def solusopen():
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Links cannot be opened while rooted.")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
    if not os.getuid() == 0:
        os.system("xdg-open https://getsol.us/home")
def soluscopy():
    window.clipboard_append("https://getsol.us/home")
    window.update()
def fedora_():
    if os.path.isfile(lang_en):
        text1.config(text="It is a indedepent distribution.\nIt uses DNF, improved of YUM.\nnThe news says Linus Torvalds is using Fedora.\nPackages come to Fedora before they come to RHEL.\n\nMetterXP's Fedora Linux support: Available\nWebsite: https://getfedora.org/")
        button1.config(text="Open link",command=fedoraopen)
        button2.config(text="Copy link",command=fedoracopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Back to menu", command=reopen)
    elif os.path.isfile(lang_tr):
        text1.config(text="Bağımsız bir dağıtımdır.\nYUM'un geliştirilmiş hali olan DNF'i kullanır.\nHaberlerde Linus Torvalds'ın Fedora kullandığı yazmaktadır.\nRHEL'e gelmeden önce paketler Fedora'ya gelir.\n\nMetterXP'ın Fedora Linux desteği: Mevcut\nİnternet sitesi: https://getfedora.org/tr/")
        button1.config(text="Bağlantıyı aç",command=fedoraopen)
        button2.config(text="Bağlantıyı kopyala",command=fedoracopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Menüye dön", command=reopen)
    button_2.pack(fill="x")
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
def fedoraopen():
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Links cannot be opened while rooted.")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
    if not os.getuid() == 0:
        os.system("xdg-open https://getfedora.org")
def fedoracopy():
    window.clipboard_append("https://getfedora.org")
    window.update()
def pop():
    if os.path.isfile(lang_en):
        text1.config(text="Pop!_OS is an Ubuntu-based distribution developed by system76.\nUses the GNOME desktop environment by default.\nPop!_OS offers the possibility to download an ISO image with NVIDIA drivers.\n\nMetterXP's Pop!_OS support: Available\nWebsite: https://pop.system76.com/")
        button1.config(text="Open link",command=popopen)
        button2.config(text="Copy link",command=popcopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Back to menu", command=reopen)
    elif os.path.isfile(lang_tr):
        text1.config(text="Pop!_OS, system76 tarafından geliştirilen Ubuntu tabanlı bir dağıtımdır.\nVarsayılan olarak GNOME masaüstü ortamını kullanır.\nPop!_OS'in NVIDIA sürücüleri olan ISO imajını indirme imkanı sunması dikkat çekmektedir.\n\nMetterXP'ın Pop!_OS desteği: Mevcut\nİnternet sitesi: https://pop.system76.com/")
        button1.config(text="Bağlantıyı aç",command=popopen)
        button2.config(text="Bağlantıyı kopyala",command=popcopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Menüye dön", command=reopen)
    button_2.pack(fill="x")
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
def popopen():
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Links cannot be opened while rooted.")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
    if not os.getuid() == 0:
        os.system("xdg-open https://pop.system76.com")
def popcopy():
    window.clipboard_append("https://pop.system76.com")
    window.update()
def zorin():
    if os.path.isfile(lang_en):
        text1.config(text="Zorin OS is an Ubuntu-based distribution that uses a modified version of Xfce and GNOME.\nThe latest version of Zorin OS is available for payment.\n\nMetterXP's Zorin OS support: Available\nWebsite: https://zorin.com/os")
        button1.config(text="Open link",command=zorinopen)
        button2.config(text="Copy link",command=zorincopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Back to menu", command=reopen)
    elif os.path.isfile(lang_tr):
        text1.config(text="Zorin OS, Ubuntu tabanlı Xfce ve GNOME'un değişitirilmiş halini kullanan bir dağıtımdır.\nZorin OS'in en üst sürümü para ödenerek edinilebilir.\n\nMetterXP'ın Zorin OS desteği: Mevcut\nİnternet sitesi: https://zorin.com/os")
        button1.config(text="Bağlantıyı aç",command=zorinopen)
        button2.config(text="Bağlantıyı kopyala",command=zorincopy)
        button_2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Menüye dön", command=reopen)
    button_2.pack(fill="x")
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
def zorinopen():
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Links cannot be opened while rooted.")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
    if not os.getuid() == 0:
        os.system("xdg-open https://zorin.com/os")
def zorincopy():
    window.clipboard_append("https://zorin.com/os")
    window.update()

window=Tk()
window.config(background=bg)
window.resizable(0, 0)
window.geometry("600x600")
parent = Frame(window)
parent.pack(expand=1)
if os.path.isfile(lang_en):
    window.title("About some GNU/Linux distros | MetterXP")
    if os.path.isfile(debian):
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Which distribution would you like to know briefly about?\n\nYou are using Debian GNU/Linux. So:\nIt is one of the first and is indedepent.\nIt uses dpkg.\nMany distributions are based on Debian.\nPackages in the Stable repository are not very up-to-date.\nPackages in other repository are more up-to-date than Stable.")
    elif os.path.isfile(fedora):
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Which distribution would you like to know briefly about?\n\nYou are using Fedora Linux. So:\nIt is a indedepent distribution.\nIt uses DNF, improved of YUM.\nnThe news says Linus Torvalds is using Fedora.\nPackages come to Fedora before they come to RHEL.")
    elif os.path.isfile(solus):
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Which distribution would you like to know briefly about?\n\nYou are using Solus. So:\nIt is a indedepent distribution.\nIt uses EOPKG, it is fork of PiSi from not Debian based Pardus.\nIt has semi-rolling release logic.\nAfter the changes in the developer team, 4.4 was released about 2 years after 4.3.")
    else:
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Which distribution would you like to know briefly about?")
elif os.path.isfile(lang_tr):
    window.title("Bazı GNU/Linux dağıtımları hakkında | MetterXP")
    if os.path.isfile(debian):
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Hangi dağıtım hakkında kısa bilgi edinmek istersiniz?\n\nDebian GNU/Linux kullanıyorsunuz. Bu yüzden:\nİlk çıkanlardan birisidir ve bağımsızdır.\ndpkg kullanmaktadır.\nBir çok dağıtım, Debian'ı taban almaktadır.\nStable deposundaki paketler çok güncel değildir.\nDiğer depolardaki paketler, Stable'dan daha günceldir.")
    elif os.path.isfile(fedora):
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Hangi dağıtım hakkında kısa bilgi edinmek istersiniz?\n\nFedora Linux kullanıyorsunuz. Bu yüzden:\nBağımsız bir dağıtımdır.\nYUM'un geliştirilmiş hali olan DNF'i kullanır.\nHaberlerde Linus Torvalds'ın Fedora kullandığı yazmaktadır.\nRHEL'e gelmeden önce paketler Fedora'ya gelir.")
    elif os.path.isfile(solus):
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Hangi dağıtım hakkında kısa bilgi edinmek istersiniz?\n\nSolus kullanıyorsunuz. Bu yüzden:\nBağımsız bir dağıtımdır.\nDebian'dan önceki Pardus'ta kullanılan PiSi'ın çatalı EOPKG'i kullanır.\nYarı yuvarlanan sürüm mantığına sahiptir.\nGeliştirici takımındaki değişiklikler sonrası 4.3'ten yaklaşık 2 yıl sonra 4.4 çıkmıştır.")
    else:
        text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Hangi dağıtım hakkında kısa bilgi edinmek istersiniz?")
text1.pack(fill="x")
space1=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
space1.pack(fill="x")
button1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="MX Linux", command=mx)
button1.pack(fill="x")
button2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Manjaro", command=manjaro)
button2.pack(fill="x")
button3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Linux Mint", command=mint)
button3.pack(fill="x")
button4=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Ubuntu", command=ubuntu)
button4.pack(fill="x")
if not os.path.isfile(debian):
    button5=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Debian GNU/Linux", command=debian_)
    button5.pack(fill="x")
button6=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Elementary OS", command=elementary)
button6.pack(fill="x")
if not os.path.isfile(solus):
    button7=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Solus", command=solus_)
    button7.pack(fill="x")
if not os.path.isfile(fedora):
    button8=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Fedora Linux", command=fedora_)
    button8.pack(fill="x")
button9=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Pop!_OS", command=pop)
button9.pack(fill="x")
button10=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="7", text="Zorin OS", command=zorin)
button10.pack(fill="x")
mainloop()
