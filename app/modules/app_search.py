#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
from subprocess import *
import subprocess
import os

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

def kapat():
    print("\nModül kapatılıyor...")
    exit()

def paketara():
    if os.path.isfile(debian):
        try:
            c1_paketara="apt search "
            get_paketadi=paketadi.get()
            cf_paketara=c1_paketara+get_paketadi
            run_cf_paketara = subprocess.Popen(cf_paketara, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            (out, err) = run_cf_paketara.communicate()
            pencere_2=Toplevel()
            pencere_2.title("Program/Paket Arama Sonuçları | MetterXP")
            pencere_2.config(background="#000000")
            pencere_2.resizable(0, 0)
            kaydirma=Scrollbar(pencere_2)
            kaydirma.pack(side=RIGHT,fill=Y)
            yazi2=Label(pencere_2, background="#000000", foreground="#FFFFFF", font="arial 11 bold", text="\nBilgilendirme: İstediğiniz program/paket arandı.\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
            yazi2.pack()
            yazi3=Text(pencere_2, yscrollcommand=kaydirma.set)
            yazi3.pack()
            yazi3.insert(END, out)
            kaydirma.config(command=yazi3.yview)
            b_metin3=Label(pencere_2, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
            b_metin3.pack()
            buton_2=Button(pencere_2, font="arial 11", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat", command=pencere_2.destroy)
            buton_2.pack()
        except:
            messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
            kapat()
    if os.path.isfile(fedora):
        try:
            c1_paketara="dnf search "
            get_paketadi=paketadi.get()
            cf_paketara=c1_paketara+get_paketadi
            run_cf_paketara = subprocess.Popen(cf_paketara, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            (out, err) = run_cf_paketara.communicate()
            pencere_2=Toplevel()
            pencere_2.title("Program/Paket Arama Sonuçları | MetterXP")
            pencere_2.config(background="#000000")
            pencere_2.resizable(0, 0)
            kaydirma=Scrollbar(pencere_2)
            kaydirma.pack(side=RIGHT,fill=Y)
            yazi2=Label(pencere_2, background="#000000", foreground="#FFFFFF", font="arial 11 bold", text="\nBilgilendirme: İstediğiniz program/paket arandı.\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
            yazi2.pack()
            yazi3=Text(pencere_2, yscrollcommand=kaydirma.set)
            yazi3.pack()
            yazi3.insert(END, out)
            kaydirma.config(command=yazi3.yview)
            b_metin3=Label(pencere_2, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
            b_metin3.pack()
            buton_2=Button(pencere_2, font="arial 11", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat", command=pencere_2.destroy)
            buton_2.pack()
        except:
            messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
            kapat()
    if os.path.isfile(solus):
        try:
            c1_paketara="eopkg search "
            get_paketadi=paketadi.get()
            cf_paketara=c1_paketara+get_paketadi
            run_cf_paketara = subprocess.Popen(cf_paketara, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            (out, err) = run_cf_paketara.communicate()
            pencere_2=Toplevel()
            pencere_2.title("Program/Paket Arama Sonuçları | MetterXP")
            pencere_2.config(background="#000000")
            pencere_2.resizable(0, 0)
            kaydirma=Scrollbar(pencere_2)
            kaydirma.pack(side=RIGHT,fill=Y)
            yazi2=Label(pencere_2, background="#000000", foreground="#FFFFFF", font="arial 11 bold", text="\nBilgilendirme: İstediğiniz program/paket arandı.\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
            yazi2.pack()
            yazi3=Text(pencere_2, yscrollcommand=kaydirma.set)
            yazi3.pack()
            yazi3.insert(END, out)
            kaydirma.config(command=yazi3.yview)
            b_metin3=Label(pencere_2, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
            b_metin3.pack()
            buton_2=Button(pencere_2, font="arial 11", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat", command=pencere_2.destroy)
            buton_2.pack()
        except:
            messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
            kapat()
            
pencere=Tk()
pencere.title("Program arama | MetterXP")
pencere.config(background="#000000")
pencere.resizable(0, 0)

yazi1=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 10 bold", text="Lütfen aratmak istediğiniz programın/paketin adını giriniz.")
yazi1.pack()
b_metin1=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
b_metin1.pack()
paketadi=Entry(pencere)
paketadi.pack()
b_paketara=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Ara",command=paketara)
b_paketara.pack()
b_metin2=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 1")
b_metin2.pack()
yazi2=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 9 bold", text="Bilgilendirme: Açılacak komut çıktısında bazı hatalar (anlamsız harfler, sayılar vb.) olabilir.\nLütfen bunu dikkate almayınız.")
yazi2.pack()
b_metin3=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
b_metin3.pack()
buton_1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Ana menüye dön\nModülü kapat", command=kapat)
buton_1.pack()

mainloop()