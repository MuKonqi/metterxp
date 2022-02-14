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

pencere=Tk()
pencere.title("MetterXP seçenekleri | MetterXP")
pencere.config(background="#000000")
pencere.resizable(0, 0)

def metterxp():
    os.system("xdg-open https://mukonqi.github.io/metterxp")
def foss():
    os.system("xdg-open https://www.gnu.org/philosophy/free-sw.tr.html")
def yapimci():
    os.system("xdg-open https://mukonqi.github.io")
def lisans():
    os.system("xdg-open https://www.gnu.org/licenses/gpl-3.0-standalone.html")
def temel():
    os.system("xdg-open https://github.com/MuKonqi/betterxp/tree/betterxp")
def surum():
    pencere2=Toplevel()
    pencere2.title("MetterXP 1.0-2 hakkında | MetterXP")
    pencere2.config(background="#000000")
    pencere2.resizable(0, 0)

    yazi3=Label(pencere2, background="#000000", foreground="#FFFFFF", font="arial 12 bold italic", text="Yenilikler:\nHata düzeltmeleri.\n\nBazı özellikler:\nProgram kurma/yeniden kurma/kaldırma\nProgram/paket arama\nMasaüstü ortamı/pencere yöneticisi kurma/yeniden kurma/kaldımar\nPaket yöneticisi kurma/yeniden kurma\nSistemi güncelleme\nÇeşitli yapılandırmalar (.bashrc, GRUB, Cups, Plank, Wine ve bilgisayar adı)\nVe dahası...\n\nBilinen hatalar: Program kur/yeniden/kur/kaldır ile program arama özelliklerindeki çıktılarda bulunan anlamsız semboller\n\n\nMetterXP, yürüteceği herhangi bir işlem için garanti vermemektedir (bakınız GPLv3).\nÖnceki sürüm: Yok\n1.0-1")
    yazi3.pack()

b_metin1=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 7")
b_metin1.pack()
buton1=Button(pencere, font="arial 15 bold italic", cursor="hand2", activeforeground="#0099FF", activebackground="#000000", background="#000000", foreground="#FFFFFF", text="MetterXP\nMaksimum ve daha iyi deneyim için tasarlandı.", command=metterxp)
buton1.pack()
b_metin3=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 1")
b_metin3.pack()    
buton2=Button(pencere, font="arial 12 bold", cursor="hand2", activeforeground="#0099FF", activebackground="#000000", background="#000000", foreground="#FFFFFF", text="Yapılış şekli: Özgür ve Açık Kaynaklı Yazılım (FOSS)", command=foss)
buton2.pack()
buton3=Button(pencere, font="arial 12 bold", cursor="hand2", activeforeground="#0099FF", activebackground="#000000", background="#000000", foreground="#FFFFFF", text="Yapımcı: Muhammed Abdurrahman", command=yapimci)
buton3.pack()
buton4=Button(pencere, font="arial 12 bold", cursor="hand2", activeforeground="#0099FF", activebackground="#000000", background="#000000", foreground="#FFFFFF", text="Lisans: GNU General Public License, Version 3.0 (GPLv3)", command=lisans)
buton4.pack()
buton5=Button(pencere, font="arial 12 bold", cursor="hand2", activeforeground="#0099FF", activebackground="#000000", background="#000000", foreground="#FFFFFF", text="Temel: BetterXP 2.0.3-2, Terminalden kurtulun 2.0", command=temel)
buton5.pack()
buton6=Button(pencere, font="arial 12 bold", cursor="hand2", activeforeground="#0099FF", activebackground="#000000", background="#000000", foreground="#FFFFFF", text="Sürüm: 1.0-2", command=surum)
buton6.pack()

b_metin4=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
b_metin4.pack()
buton_1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Ana menüye dön\nModülü kapat", command=kapat)
buton_1.pack()

mainloop()
