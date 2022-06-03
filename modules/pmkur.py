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
    os.system(" python3 /usr/local/bin/metterxp/modules/pmkur.py")
    
def reboot():
    print("Bilgisiyarınız yeniden başlatılıyor...")
    os.system(" reboot now")

def flatpak():
    def kur():
        if os.path.isfile(debian):
            print("\nFlatpak kuruluyor...")
            os.system(" apt install flatpak -y")
        elif os.path.isfile(fedora):
            print("\nFlatpak kuruluyor...")
            os.system(" dnf install flatpak -y")
        elif os.path.isfile(solus):
            print("\nFlatpak kuruluyor...")
            os.system(" eopkg install flatpak -y")
        print("\nFlatpak'a Flathub deposu ekleniyor...")
        os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
        messagebox.showinfo("Bilgilendirme","Flatpak başarıyla kuruldu, değişikliklerin tamamlanması için 'OK' tuşuna bastığınızda bilgisiyarınız yeniden başlatılacak.")    
        reboot()    
    def rekur():
        if os.path.isfile(debian):
            print("\nFlatpak yeniden kuruluyor...")
            os.system(" apt reinstall flatpak -y")
        elif os.path.isfile(fedora):
            print("\nFlatpak yeniden kuruluyor...")
            os.system(" dnf reinstall flatpak -y")
        elif os.path.isfile(solus):
            print("\nFlatpak yeniden kuruluyor...")
            os.system(" eopkg install flatpak --rei -y")
        print("\nFlatpak'a Flathub deposu ekleniyor...")
        os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
        messagebox.showinfo("Bilgilendirme","Flatpak başarıyla yeniden kuruldu, değişikliklerin tamamlanması için 'OK' tuşuna bastığınızda bilgisiyarınız yeniden başlatılacak.")    
        reboot()
    islemsecimbuton1.destroy()
    islemsecimbuton2.destroy()
    b_metin2.destroy()
    buton_1.destroy()
    yazi1.config(text="Flatpak için ne yapmak istiyorsunuz?")
    if os.path.isfile(debian):
        def oldubuntukur():
            print("Flatpak kuruluyor...")
            os.system(" add-apt-repository ppa:flatpak/stable")
            os.system(" apt update")
            os.system(" apt install flatpak")
            print("\nFlatpak'a Flathub deposu ekleniyor...")
            os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
            messagebox.showinfo("Bilgilendirme","Flatpak başarıyla kuruldu, değişikliklerin tamamlanması için 'OK' tuşuna bastığınızda bilgisiyarınız yeniden başlatılacak.")    
            reboot() 
        flatpakbuton1_1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Kur\n(Ubuntu 18.04 ve sonrası ya da Debian GNU/Linux'u taban alanlar)", command=kur)
        flatpakbuton1_1.pack()
        flatpakbuton1_2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Kur\n(Ubuntu 17.10 ve öncesini taban alanlar)", command=oldubuntukur)
        flatpakbuton1_2.pack()
    else:
        flatpakbuton1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Kur", command=kur)
        flatpakbuton1.pack()        
    flatpakbuton2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Yeniden kur", command=rekur)
    flatpakbuton2.pack()
    flatpakb_metin1=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
    flatpakb_metin1.pack()
    flatpakbuton_1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Ana menüye dön\nModülü kapat", command=kapat)
    flatpakbuton_1.pack()
    flatpakbuton_2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
    flatpakbuton_2.pack()
def snap():
    def kur():
        if os.path.isfile(debian):
            print("\nSnap kuruluyor...")
            os.system(" apt install snapd -y")
        elif os.path.isfile(fedora):
            print("\nSnap kuruluyor...")
            os.system(" dnf install snapd -y")
        elif os.path.isfile(solus):
            print("\nSnap kuruluyor...")
            os.system(" eopkg install snapd -y")
        messagebox.showinfo("Bilgilendirme","Snap başarıyla kuruldu, değişikliklerin tamamlanması için 'OK' tuşuna bastığınızda bilgisiyarınız yeniden başlatılacak.")    
        reboot() 
    def rekur():
        if os.path.isfile(debian):
            print("\nSnap yeniden kuruluyor...")
            os.system(" apt reinstall snapd -y")
        elif os.path.isfile(fedora):
            print("\nSnap yeniden kuruluyor...")
            os.system(" dnf reinstall snapd -y")
        elif os.path.isfile(solus):
            print("\nSnap yeniden kuruluyor...")
            os.system(" eopkg install snapd --rei -y")
        messagebox.showinfo("Bilgilendirme","Snap başarıyla yeniden kuruldu, değişikliklerin tamamlanması için 'OK' tuşuna bastığınızda bilgisiyarınız yeniden başlatılacak.")    
        reboot() 
    yazi1.config(text="Snap için ne yapmak istiyorsunuz?")
    islemsecimbuton1.config(text="Kur",command=kur)
    islemsecimbuton2.config(text="Yeniden kur",command=rekur)
    buton_2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
    buton_2.pack()

pencere=Tk()
pencere.title("Paket yöneticisi kur/yeniden kur/kaldır | MetterXP")
pencere.config(background="#000000")
pencere.resizable(0, 0)

yazi1=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 10 bold", text="Lütfen bir paket yöneticisi seçiniz.")
yazi1.pack()
b_metin1=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
b_metin1.pack()
islemsecimbuton1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Flatpak", command=flatpak)
islemsecimbuton1.pack()
islemsecimbuton2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Snap", command=snap)
islemsecimbuton2.pack()
b_metin2=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
b_metin2.pack()
buton_1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Ana menüye dön\nModülü kapat", command=kapat)
buton_1.pack()

mainloop()