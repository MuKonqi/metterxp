#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if not os.getuid() == 0:
    messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
    exit("\nSadece kök kullanıcı bu modülü çalıştırabilir!\nModül kapatılıyor...")

def kapat():
    print("\nModül kapatılıyor...")
    exit()
def reopen():
    print("\nModül yeniden başlatılıyor...")
    pencere.destroy()
    os.system(" python3 /usr/local/bin/metterxp/modules/gnupluslinux.py")

pencere=Tk()
pencere.title("Dosya yöneticilerini kök haklarıyla aç | MetterXP")
pencere.config(background="#000000")
pencere.resizable(0, 0)

def nautilus():
    try:
        os.system(" nautilus")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def nemo():
    try:
        os.system(" nemo")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def caja():
    try:
        os.system(" caja")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def thunar():
    try:
        os.system(" thunar")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def pcmanfmqt():
    try:
        os.system(" pcmanfm-qt")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()

yazi1=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 10 bold", text="Hangi dosya yöneticisini kök haklarıyla açmak istersiniz?")
yazi1.pack()
b_metin1=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
b_metin1.pack()
islemsecimbuton1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Nautilus\n(GNOME, Budgie masaüstü ortamlarıyla gelir)", command=nautilus)
islemsecimbuton1.pack()
islemsecimbuton2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Nemo\n(Cinnamon masaüstü ortamıyla gelir)", command=nemo)
islemsecimbuton2.pack()
islemsecimbuton3=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Caja\n(Mate masaüstü ortamıyla gelir)", command=caja)
islemsecimbuton3.pack()
islemsecimbuton4=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Thunar\n(Xfce masaüstü ortamıyla gelir)", command=thunar)
islemsecimbuton4.pack()
islemsecimbuton5=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="PCmanFM-Qt\n(LXQt masaüstü ortamıyla gelir)", command=pcmanfmqt)
islemsecimbuton5.pack()
b_metin2=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
b_metin2.pack()
buton_1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Ana menüye dön\nModülü kapat", command=kapat)
buton_1.pack()

mainloop()