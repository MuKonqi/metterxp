#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

def kapat():
    print("\nModül kapatılıyor...")
    exit()
def reopen():
    print("\nModül yeniden başlatılıyor...")
    pencere.destroy()
    os.system("sudo python3 /usr/local/bin/metterxp/modules/gnupluslinux.py")

def mx():
    yazi1.config(text="MX Linux, Debian GNU/Linux tabanlı ve varsayılan olarak Xfce masaüstü ortamını kullanan hafif bir dağıtımdır.\n\nİnternet sitesi: https://mxlinux.org/")
    islemsecimbuton1.config(text="Bağlantıyı aç",command=mxopen)
    islemsecimbuton2.config(text="Bağlantıyı kopyala",command=mxcopy)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    buton_2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
    buton_2.pack()
def mxopen():
    try:
        os.system("xdg-open https://mxlinux.org")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def mxcopy():
    try:
        pencere.clipboard_append("https://mxlinux.org")
        pencere.update()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def manjaro():
    yazi1.config(text="Manjaro, Arch Linux tabanlı ve son kullanıcı odaklı bir dağıtımdır.\nManjaro'nun kendisine ait araçları vardır. Örneğin: Pamac\n\nİnternet sitesi: https://manjaro.org/")
    islemsecimbuton1.config(text="Bağlantıyı aç",command=manjaroopen)
    islemsecimbuton2.config(text="Bağlantıyı kopyala",command=manjarocopy)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    buton_2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
    buton_2.pack()
def manjaroopen():
    try:
        os.system("xdg-open https://manjaro.org")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()    
def manjarocopy():
    try:
        pencere.clipboard_append("https://manjaro.org")
        pencere.update()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def mint():
    yazi1.config(text="Linux Mint, Ubuntu tabanlı, son kullanıcı odaklı bir dağıtımdır.\nLinux Mint, kendi masaüstü ortamı olan Cinnamon'u varsayılan olarak kullanmasıyla beraber Mate ve Xfce masaüstü ortamı seçeneklerini de sunar.\n\nİnternet sitesi: https://linuxmint.com/")
    islemsecimbuton1.config(text="Bağlantıyı aç",command=mintopen)
    islemsecimbuton2.config(text="Bağlantıyı kopyala",command=mintcopy)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    buton_2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
    buton_2.pack()
def mintopen():
    try:
        os.system("xdg-open https://linuxmint.com")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def mintcopy():
    try:
        pencere.clipboard_append("https://linuxmint.com")
        pencere.update()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def ubuntu():
    yazi1.config(text="Ubuntu, Canonical tarafından geliştirilen ve Debian GNU/Linux tabanlı en pöpüler GNU/Linux dağıtımlarından biridir.\nUbuntu, GNOME'u varsayılan masaüstü ortamı olarak kullanır. Ubuntu için alternatif masaüstü ortamları topluluk tarafından yayınlanmıştır.\n\nİnternet sitesi: https://ubuntu.com/")
    islemsecimbuton1.config(text="Bağlantıyı aç",command=ubuntuopen)
    islemsecimbuton2.config(text="Bağlantıyı kopyala",command=ubuntucopy)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    buton_2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
    buton_2.pack()
def ubuntuopen():
    try:
        os.system("xdg-open https://ubuntu.com")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def ubuntucopy():
    try:
        pencere.clipboard_append("https://ubuntu.com")
        pencere.update()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def debian():
    yazi1.config(text="Debian GNU/Linux, ilk çıkan GNU/Linux dağıtımlarından birisidir ve bağımsızdır.\nBir çok dağıtım, Debian GNU/Linux'u taban almaktadır.\nStable sürümümün deposunda barındırdığı paketler güncel değildir fakat güncel olan sürümleri (Testing, Unstable) de vardır.\nGünümüzde desteklenmeye eski olmasına rağmen devam etmektedir.\n\nİnternet sitesi: https://www.debian.org/")
    islemsecimbuton1.config(text="Bağlantıyı aç",command=debianopen)
    islemsecimbuton2.config(text="Bağlantıyı kopyala",command=debiancopy)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    buton_2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
    buton_2.pack()
def debianopen():
    try:
        os.system("xdg-open https://www.debian.org")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()     
def debiancopy():
    try:
        pencere.clipboard_append("https://www.debian.org")
        pencere.update()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def elementary():
    yazi1.config(text="ElementaryOS, Debian GNU/Linux tabanlı olup, kendi masaüstü ortamı olan Pantheon'u varsayılan olarak kullanır.\n\nİnternet sitesi: https://elementary.io/")
    islemsecimbuton1.config(text="Bağlantıyı aç",command=elementaryopen)
    islemsecimbuton2.config(text="Bağlantıyı kopyala",command=elementarycopy)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    buton_2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
    buton_2.pack()
def elementaryopen():
    try:
        os.system("xdg-open https://elementary.io")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def elementarycopy():
    try:
        pencere.clipboard_append("https://elementary.io")
        pencere.update()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def solus():
    yazi1.config(text="Solus, PiSi tabanlı EOPKG adlı paket yöneticisini kullanan bağımsız bir dağıtımdır.\nYarı yuvarlanan sürüm mantığına sahiptir.\nVarsayılan olarak Budgie masaüstü ortamını kullanmasıyla beraber KDE Plasma, GNOME, Mate masaüstü ortamlarını da seçenek olarak sunar.\n\nİnternet sitesi: https://getsol.us/home/")
    islemsecimbuton1.config(text="Bağlantıyı aç",command=solusopen)
    islemsecimbuton2.config(text="Bağlantıyı kopyala",command=soluscopy)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    buton_2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
    buton_2.pack()
def solusopen():
    try:
        os.system("xdg-open https://getsol.us/home")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def soluscopy():
    try:
        pencere.clipboard_append("https://getsol.us/home")
        pencere.update()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def fedora():
    yazi1.config(text="Fedora Linux, YUM'un geliştirilmiş hali olan DNF adlı paket yöneticisini kullanan bağımsız bir dağıtımdır.\nGNOME masaüstü ortamıyla gelir fakat diğer masaüstü ortamları için spinleri de vardır.\nRHEL'e (Red Hat Enterprise Linux) gelmeden önce paketler Fedora Linux'a gelir.\n\nİnternet sitesi: https://getfedora.org/tr/")
    islemsecimbuton1.config(text="Bağlantıyı aç",command=fedoraopen)
    islemsecimbuton2.config(text="Bağlantıyı kopyala",command=fedoracopy)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    buton_2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
    buton_2.pack()
def fedoraopen():
    try:
        os.system("xdg-open https://getfedora.org")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def fedoracopy():
    try:
        pencere.clipboard_append("https://getfedora.org")
        pencere.update()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def pop():
    yazi1.config(text="Pop!_OS, system76 tarafından geliştirilen Ubuntu tabanlı bir dağıtımdır.\nVarsayılan olarak GNOME masaüstü ortamını kullanır.\nPop!_OS'in NVIDIA sürücüleri olan ISO imajını indirme imkanı sunması dikkat çekmektedir.\n\nİnternet sitesi: https://pop.system76.com/")
    islemsecimbuton1.config(text="Bağlantıyı aç",command=popopen)
    islemsecimbuton2.config(text="Bağlantıyı kopyala",command=popcopy)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    buton_2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
    buton_2.pack()
def popopen():
    try:
        os.system("xdg-open https://pop.system76.com")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def popcopy():
    try:
        pencere.clipboard_append("https://pop.system76.com")
        pencere.update()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def zorin():
    yazi1.config(text="Zorin OS, Ubuntu tabanlı Xfce ve GNOME'un değişitirilmiş halini kullanan bir dağıtımdır.\nZorin OS'in en üst sürümü para ödenerek edinilebilir.\n\nİnternet sitesi: https://zorin.com/os")
    islemsecimbuton1.config(text="Bağlantıyı aç",command=zorinopen)
    islemsecimbuton2.config(text="Bağlantıyı kopyala",command=zorincopy)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    buton_2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
    buton_2.pack()
def zorinopen():
    try:
        os.system("xdg-open https://zorin.com/os")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def zorincopy():
    try:
        pencere.clipboard_append("https://zorin.com/os")
        pencere.update()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()

pencere=Tk()
pencere.title("Bazı GNU/Linux dağıtımları hakkında | MetterXP")
pencere.config(background="#000000")
pencere.resizable(0, 0)

yazi1=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 10 bold", text="Hangi dağıtım hakkında kısa bilgi edinmek istersiniz?")
yazi1.pack()
b_metin1=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
b_metin1.pack()
islemsecimbuton1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="MX Linux", command=mx)
islemsecimbuton1.pack()
islemsecimbuton2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Manjaro", command=manjaro)
islemsecimbuton2.pack()
islemsecimbuton3=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Linux Mint", command=mint)
islemsecimbuton3.pack()
islemsecimbuton4=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Ubuntu", command=ubuntu)
islemsecimbuton4.pack()
islemsecimbuton5=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Debian GNU/Linux", command=debian)
islemsecimbuton5.pack()
islemsecimbuton6=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Elementary OS", command=elementary)
islemsecimbuton6.pack()
islemsecimbuton7=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Solus", command=solus)
islemsecimbuton7.pack()
islemsecimbuton8=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Fedora Linux", command=fedora)
islemsecimbuton8.pack()
islemsecimbuton9=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pop!_OS", command=pop)
islemsecimbuton9.pack()
islemsecimbuton10=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Zorin OS", command=zorin)
islemsecimbuton10.pack()
b_metin2=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
b_metin2.pack()
buton_1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Ana menüye dön\nModülü kapat", command=kapat)
buton_1.pack()

mainloop()