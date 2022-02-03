#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
from subprocess import *
import os
import subprocess

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"


def kapat():
    print("\nModül kapatılıyor...")
    exit()
def reopen():
    print("\nModül yeniden başlatılıyor...")
    pencere.destroy()
    os.system("sudo python3 /usr/local/bin/metterxp/modules/prkurkaldır.py")

pencere=Tk()
pencere.title("Program kur/yeniden kur/kaldır | MetterXP")
pencere.config(background="#000000")
pencere.resizable(0, 0)

def main():
    def to_other():
        islemsecimbuton1.destroy()
        islemsecimbuton2.destroy()
        islemsecimbuton3.destroy()
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        buton_1.destroy()
        buton_2.destroy()
        yazi1.destroy()
        b_metin1.destroy()
        b_metin2.destroy()
        b_metin3.destroy()
        other()
        
    def firefox():
        def kur():
            try:
                print("\nMozilla Firefox kurulumu başlatılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt install firefox -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install firefox -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install firefox -y")
                messagebox.showinfo("Bilgilendirme","Mozilla Firefox başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def rekur():
            try:
                print("\nMozilla Firefox yeniden kuruluyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt reinstall firefox -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf reinstall firefox -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install firefox -y --rei")
                messagebox.showinfo("Bilgilendirme","Mozilla Firefox yeniden başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def sil():
            try:
                print("\nMozilla Firefox kaldırılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt purge firefox* -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf remove firefox -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg remove firefox -y --purge")
                messagebox.showinfo("Bilgilendirme","Mozilla Firefox başarıyla kaldırıldı.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        yazi1.config(text="Mozilla Firefox internet tarayıcısı için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        buton_1.destroy()
        buton_3=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_3.pack()
    def brave():
        def kur():
            try:
                print("\Brave kurulumu başlatılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt install apt-transport-https curl")
                    os.system("sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
                    os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
                    os.system("sudo apt update")
                    os.system("sudo apt install brave-browser")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install dnf-plugins-core")
                    os.system("sudo dnf config-manager --add-repo https://brave-browser-rpm-release.s3.brave.com/x86_64")
                    os.system('sudo rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc')
                    os.system("sudo dnf install brave-browser")                
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install brave -y")
                messagebox.showinfo("Bilgilendirme","Brave başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def rekur():
            try:
                print("\nBrave yeniden kuruluyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt reinstall brave-browser -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf reinstall brave-browser -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install brave -y --rei")
                messagebox.showinfo("Bilgilendirme","Brave yeniden başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def sil():
            try:
                print("\Brave kaldırılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt purge brave-browser* -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf remove brave-browser -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg remove brave -y --purge")
                messagebox.showinfo("Bilgilendirme","Brave başarıyla kaldırıldı.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        yazi1.config(text="Brave internet tarayıcısı için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        buton_1.destroy()
        buton_3=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_3.pack()
    def vlc():
        def kur():
            try:
                print("\nVLC kurulumu başlatılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt install vlc -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install vlc -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install vlc -y")
                messagebox.showinfo("Bilgilendirme","VLC başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def rekur():
            try:
                print("\nVLC yeniden kuruluyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt reinstall vlc -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf reinstall vlc -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install vlc -y --rei")
                messagebox.showinfo("Bilgilendirme","VLC yeniden başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def sil():
            try:
                print("\nVLC kaldırılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt purge vlc* -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf remove vlc -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg remove vlc -y --purge")
                messagebox.showinfo("Bilgilendirme","VLC başarıyla kaldırıldı.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        yazi1.config(text="VLC medya oynatıcısı için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        buton_1.destroy()
        buton_3=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_3.pack()
    def libreoffice():
        def kur():
            try:
                print("\nLibreOffice kurulumu başlatılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo add-apt-repository ppa:libreoffice/ppa")
                    os.system("sudo apt update")
                    os.system("sudo apt install libreoffice libreoffice-l10n-tr libreoffice-help-tr -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install libreoffice -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install libreoffice -y")
                messagebox.showinfo("Bilgilendirme","LibreOffice başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def rekur():
            try:
                print("\nLibreOffice yeniden kuruluyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt reinstall libreoffice libreoffice-l10n-tr libreoffice-help-tr -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf reinstall libreoffice -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install libreoffice -y --rei")
                messagebox.showinfo("Bilgilendirme","LibreOffice yeniden başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def sil():
            try:
                print("\nLibreOffice kaldırılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt purge libreoffice libreoffice-l10n-tr libreoffice-help-tr -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf remove libreoffice -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg remove libreoffice -y --purge")
                messagebox.showinfo("Bilgilendirme","LibreOffice başarıyla kaldırıldı.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        yazi1.config(text="LibreOffice ofis programı için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        buton_1.destroy()
        buton_3=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_3.pack()
    def cups():
        def kur():
            try:
                print("\nCups kurulumu başlatılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt install cups -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install cups -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install cups -y")
                messagebox.showinfo("Bilgilendirme","Cups başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def rekur():
            try:
                print("\nCups yeniden kuruluyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt reinstall cups -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf reinstall cups -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install cups -y --rei")
                messagebox.showinfo("Bilgilendirme","Cups yeniden başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def sil():
            try:
                print("\nCups kaldırılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt purge cups* -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf remove cups -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg remove cups -y --purge")
                messagebox.showinfo("Bilgilendirme","Cups başarıyla kaldırıldı.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        yazi1.config(text="Cups yazıcı yöneticisi için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        buton_1.destroy()
        buton_3=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_3.pack()
    def gparted():
        def kur():
            try:
                print("\nGParted kurulumu başlatılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt install gparted -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install gparted -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install gparted -y")
                messagebox.showinfo("Bilgilendirme","GParted başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def rekur():
            try:
                print("\nGParted yeniden kuruluyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt reinstall gparted -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf reinstall gparted -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install gparted -y --rei")
                messagebox.showinfo("Bilgilendirme","GParted yeniden başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def sil():
            try:
                print("\nGParted kaldırılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt purge gparted* -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf remove gparted -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg remove gparted -y --purge")
                messagebox.showinfo("Bilgilendirme","GParted başarıyla kaldırıldı.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        yazi1.config(text="GParted disk bölümü düzenleyicisi için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        buton_1.destroy()
        buton_3=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_3.pack()
    def gimp():
        def kur():
            try:
                print("\nGIMP kurulumu başlatılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt install gimp -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install gimp -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install gimp -y")
                messagebox.showinfo("Bilgilendirme","GIMP başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def rekur():
            try:
                print("\nGIMP yeniden kuruluyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt reinstall gimp -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf reinstall gimp -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install gimp -y --rei")
                messagebox.showinfo("Bilgilendirme","GIMP yeniden başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def sil():
            try:
                print("\nGIMP kaldırılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt purge gimp* -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf remove gimp -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg remove gimp -y --purge")
                messagebox.showinfo("Bilgilendirme","GIMP başarıyla kaldırıldı.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        yazi1.config(text="GIMP resim editörü için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        buton_1.destroy()
        buton_3=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_3.pack()
    def wine():
        def kur():
            try:
                print("\nWine kurulumu başlatılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo dpkg --add-architecture i386")
                    os.system("sudo apt install wine-stable -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install wine -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install wine -y")
                messagebox.showinfo("Bilgilendirme","Wine başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def rekur():
            try:
                print("\nWine yeniden kuruluyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt reinstall wine-stable -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf reinstall wine -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install wine -y --rei")
                messagebox.showinfo("Bilgilendirme","Wine yeniden başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def sil():
            try:
                print("\nWine kaldırılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt purge wine-stable* -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf remove wine -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg remove wine -y --purge")
                messagebox.showinfo("Bilgilendirme","Wine başarıyla kaldırıldı.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        yazi1.config(text="Wine için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        buton_1.destroy()
        buton_3=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_3.pack()
    def plank():
        def kur():
            try:
                print("\nPlank kurulumu başlatılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt install plank -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf install plank -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install plank -y")
                messagebox.showinfo("Bilgilendirme","Plank başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def rekur():
            try:
                print("\nPlank yeniden kuruluyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt reinstall plank -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf reinstall plank -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg install plank -y --rei")
                messagebox.showinfo("Bilgilendirme","Plank yeniden başarıyla kuruldu.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        def sil():
            try:
                print("\nPlank kaldırılıyor...")
                if os.path.isfile(debian):
                    os.system("sudo apt purge plank* -y")
                elif os.path.isfile(fedora):
                    os.system("sudo dnf remove Plank -y")
                elif os.path.isfile(solus):
                    os.system("sudo eopkg remove plank -y --purge")
                messagebox.showinfo("Bilgilendirme","Plank başarıyla kaldırıldı.")
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        yazi1.config(text="Plank için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        buton_1.destroy()
        buton_3=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_3.pack()
        
    yazi1=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 10 bold", text="Hangi programı kurmak ya da kaldırmak istiyorsunuz?")
    yazi1.pack()
    b_metin1=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
    b_metin1.pack()
    islemsecimbuton1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Mozilla Firefox internet tarayıcısı",command=firefox)
    islemsecimbuton1.pack()
    islemsecimbuton2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Brave internet tarayıcısı",command=brave)
    islemsecimbuton2.pack()
    islemsecimbuton3=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="VLC oynatıcısı",command=vlc)
    islemsecimbuton3.pack()
    islemsecimbuton4=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="LibreOffice ofis programı",command=libreoffice)
    islemsecimbuton4.pack()
    islemsecimbuton5=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="CUPS yazıcı yöneticisi",command=cups)
    islemsecimbuton5.pack()
    islemsecimbuton6=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="GParted disk bölümü düzenleyicisi",command=gparted)
    islemsecimbuton6.pack()
    islemsecimbuton7=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="GIMP görüntü işleme programı",command=gimp)
    islemsecimbuton7.pack()
    islemsecimbuton8=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Wine",command=wine)
    islemsecimbuton8.pack()
    islemsecimbuton9=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Plank",command=plank)
    islemsecimbuton9.pack()
    b_metin2=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 1")
    b_metin2.pack()
    buton_1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Diğer", command=to_other)
    buton_1.pack()
    b_metin3=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
    b_metin3.pack()
    buton_2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü kapat\nAna menüye dön", command=kapat)
    buton_2.pack()
    
def other():
    def paketkur():
        if os.path.isfile(debian):
            try:
                c1_paketkur="sudo apt install "
                get_paketadi=paketadi.get()
                c2_paketkur=" -y"
                cf_paketkur=c1_paketkur+get_paketadi+c2_paketkur
                run_cf_paketkur = subprocess.Popen(cf_paketkur, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
                (out, err) = run_cf_paketkur.communicate()
                pencere_2=Toplevel()
                pencere_2.title("Çıktı | BetterXP")
                pencere_2.config(background="#000000")
                pencere_2.resizable(0, 0)
                kaydirma=Scrollbar(pencere_2)
                kaydirma.pack(side=RIGHT,fill=Y)
                yazi3=Label(pencere_2, background="#000000", foreground="#FFFFFF", font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
                yazi3.pack()
                yazi4=Text(pencere_2, yscrollcommand=kaydirma.set)
                yazi4.pack()
                yazi4.insert(END, out)
                kaydirma.config(command=yazi4.yview)
                b_metin6=Label(pencere_2, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
                b_metin6.pack()
                buton_6=Button(pencere_2, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat", command=pencere_2.destroy)
                buton_6.pack()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        elif os.path.isfile(fedora):
            try:
                c1_paketkur="sudo dnf install "
                get_paketadi=paketadi.get()
                c2_paketkur=" -y"
                cf_paketkur=c1_paketkur+get_paketadi+c2_paketkur
                run_cf_paketkur = subprocess.Popen(cf_paketkur, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
                (out, err) = run_cf_paketkur.communicate()
                pencere_2=Toplevel()
                pencere_2.title("Çıktı | BetterXP")
                pencere_2.config(background="#000000")
                pencere_2.resizable(0, 0) 
                kaydirma=Scrollbar(pencere_2)
                kaydirma.pack(side=RIGHT,fill=Y)
                yazi3=Label(pencere_2, background="#000000", foreground="#FFFFFF", font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
                yazi3.pack()
                yazi4=Text(pencere_2, yscrollcommand=kaydirma.set)
                yazi4.pack()
                yazi4.insert(END, out)
                kaydirma.config(command=yazi4.yview)
                b_metin6=Label(pencere_2, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
                b_metin6.pack()
                buton_6=Button(pencere_2, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat", command=pencere_2.destroy)
                buton_6.pack()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        elif os.path.isfile(solus):
            try:
                c1_paketkur="sudo eopkg install "
                get_paketadi=paketadi.get()
                c2_paketkur=" -y"
                cf_paketkur=c1_paketkur+get_paketadi+c2_paketkur
                run_cf_paketkur = subprocess.Popen(cf_paketkur, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
                (out, err) = run_cf_paketkur.communicate()
                pencere_2=Toplevel()
                pencere_2.title("Çıktı | BetterXP")
                pencere_2.config(background="#000000")
                pencere_2.resizable(0, 0) 
                kaydirma=Scrollbar(pencere_2)
                kaydirma.pack(side=RIGHT,fill=Y)
                yazi3=Label(pencere_2, background="#000000", foreground="#FFFFFF", font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
                yazi3.pack()
                yazi4=Text(pencere_2, yscrollcommand=kaydirma.set)
                yazi4.pack()
                yazi4.insert(END, out)
                kaydirma.config(command=yazi4.yview)
                b_metin6=Label(pencere_2, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
                b_metin6.pack()
                buton_6=Button(pencere_2, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat", command=pencere_2.destroy)
                buton_6.pack()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
    def paketrekur():
        if os.path.isfile(debian):
            try:
                c1_paketrekur="sudo apt reinstall "
                get_paketadi=paketadi.get()
                c2_paketrekur=" -y"
                cf_paketrekur=c1_paketrekur+get_paketadi+c2_paketrekur
                run_cf_paketrekur = subprocess.Popen(cf_paketrekur, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
                (out, err) = run_cf_paketrekur.communicate()
                pencere_2=Toplevel()
                pencere_2.title("Çıktı | BetterXP")
                pencere_2.config(background="#000000")
                pencere_2.resizable(0, 0)
                kaydirma=Scrollbar(pencere_2)
                kaydirma.pack(side=RIGHT,fill=Y)
                yazi3=Label(pencere_2, background="#000000", foreground="#FFFFFF", font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
                yazi3.pack()
                yazi4=Text(pencere_2, yscrollcommand=kaydirma.set)
                yazi4.pack()
                yazi4.insert(END, out)
                kaydirma.config(command=yazi4.yview)
                b_metin6=Label(pencere_2, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
                b_metin6.pack()
                buton_6=Button(pencere_2, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat", command=pencere_2.destroy)
                buton_6.pack()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        elif os.path.isfile(fedora):
            try:
                c1_paketrekur="sudo dnf reinstall "
                get_paketadi=paketadi.get()
                c2_paketrekur=" -y"
                cf_paketrekur=c1_paketrekur+get_paketadi+c2_paketrekur
                run_cf_paketrekur = subprocess.Popen(cf_paketrekur, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
                (out, err) = run_cf_paketrekur.communicate()
                pencere_2=Toplevel()
                pencere_2.title("Çıktı | BetterXP")
                pencere_2.config(background="#000000")
                pencere_2.resizable(0, 0) 
                kaydirma=Scrollbar(pencere_2)
                kaydirma.pack(side=RIGHT,fill=Y)
                yazi3=Label(pencere_2, background="#000000", foreground="#FFFFFF", font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
                yazi3.pack()
                yazi4=Text(pencere_2, yscrollcommand=kaydirma.set)
                yazi4.pack()
                yazi4.insert(END, out)
                kaydirma.config(command=yazi4.yview)
                b_metin6=Label(pencere_2, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
                b_metin6.pack()
                buton_6=Button(pencere_2, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat", command=pencere_2.destroy)
                buton_6.pack()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        elif os.path.isfile(solus):
            try:
                c1_paketrekur="sudo eopkg install "
                get_paketadi=paketadi.get()
                c2_paketrekur=" -y --rei"
                cf_paketrekur=c1_paketrekur+get_paketadi+c2_paketrekur
                run_cf_paketrekur = subprocess.Popen(cf_paketrekur, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
                (out, err) = run_cf_paketrekur.communicate()
                pencere_2=Toplevel()
                pencere_2.title("Çıktı | BetterXP")
                pencere_2.config(background="#000000")
                pencere_2.resizable(0, 0) 
                kaydirma=Scrollbar(pencere_2)
                kaydirma.pack(side=RIGHT,fill=Y)
                yazi3=Label(pencere_2, background="#000000", foreground="#FFFFFF", font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
                yazi3.pack()
                yazi4=Text(pencere_2, yscrollcommand=kaydirma.set)
                yazi4.pack()
                yazi4.insert(END, out)
                kaydirma.config(command=yazi4.yview)
                b_metin6=Label(pencere_2, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
                b_metin6.pack()
                buton_6=Button(pencere_2, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat", command=pencere_2.destroy)
                buton_6.pack()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()        
    def paketsil():
        if os.path.isfile(debian):
            try:
                c1_paketsil="sudo apt purge "
                get_paketadi=paketadi.get()
                c2_paketsil="* -y"
                cf_paketsil=c1_paketsil+get_paketadi+c2_paketsil
                run_cf_paketsil = subprocess.Popen(cf_paketsil, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
                (out, err) = run_cf_paketsil.communicate()
                pencere_2=Toplevel()
                pencere_2.title("Çıktı | BetterXP")
                pencere_2.config(background="#000000")
                pencere_2.resizable(0, 0) 
                kaydirma=Scrollbar(pencere_2)
                kaydirma.pack(side=RIGHT,fill=Y)
                yazi3=Label(pencere_2, background="#000000", foreground="#FFFFFF", font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
                yazi3.pack()
                yazi4=Text(pencere_2, yscrollcommand=kaydirma.set)
                yazi4.pack()
                yazi4.insert(END, out)
                kaydirma.config(command=yazi4.yview)
                b_metin6=Label(pencere_2, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
                b_metin6.pack()
                buton_6=Button(pencere_2, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat", command=pencere_2.destroy)
                buton_6.pack()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        elif os.path.isfile(fedora):
            try:
                c1_paketsil="sudo dnf remove "
                get_paketadi=paketadi.get()
                c2_paketsil=" -y"
                cf_paketsil=c1_paketsil+get_paketadi+c2_paketsil
                run_cf_paketsil = subprocess.Popen(cf_paketsil, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
                (out, err) = run_cf_paketsil.communicate()
                pencere_2=Toplevel()
                pencere_2.title("Çıktı | BetterXP")
                pencere_2.config(background="#000000")
                pencere_2.resizable(0, 0) 
                kaydirma=Scrollbar(pencere_2)
                kaydirma.pack(side=RIGHT,fill=Y)
                yazi3=Label(pencere_2, background="#000000", foreground="#FFFFFF", font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
                yazi3.pack()
                yazi4=Text(pencere_2, yscrollcommand=kaydirma.set)
                yazi4.pack()
                yazi4.insert(END, out)
                kaydirma.config(command=yazi4.yview)
                b_metin6=Label(pencere_2, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
                b_metin6.pack()
                buton_6=Button(pencere_2, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat", command=pencere_2.destroy)
                buton_6.pack()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
        elif os.path.isfile(solus):
            try:
                c1_paketsil="sudo eopkg remove "
                get_paketadi=paketadi.get()
                c2_paketsil=" -y"
                cf_paketsil=c1_paketsil+get_paketadi+c2_paketsil
                run_cf_paketsil = subprocess.Popen(cf_paketsil, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
                (out, err) = run_cf_paketsil.communicate()
                pencere_2=Toplevel()
                pencere_2.title("Çıktı | BetterXP")
                pencere_2.config(background="#000000")
                pencere_2.resizable(0, 0) 
                kaydirma=Scrollbar(pencere_2)
                kaydirma.pack(side=RIGHT,fill=Y)
                yazi3=Label(pencere_2, background="#000000", foreground="#FFFFFF", font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
                yazi3.pack()
                yazi4=Text(pencere_2, yscrollcommand=kaydirma.set)
                yazi4.pack()
                yazi4.insert(END, out)
                kaydirma.config(command=yazi4.yview)
                b_metin6=Label(pencere_2, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
                b_metin6.pack()
                buton_6=Button(pencere_2, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat", command=pencere_2.destroy)
                buton_6.pack()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
                programkapat()
    yazi2=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 10 bold", text="Lütfen kaldırmak ya da kurmak istediğiniz programın/paketin adını giriniz.\nNot: Paket adını doğru girmeniz gerekmektedir!")
    yazi2.pack()
    b_metin4=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
    b_metin4.pack()
    paketadi=Entry(pencere)
    paketadi.pack()
    b_paketkur=Button(pencere,  cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Kur",command=paketkur)
    b_paketkur.pack()
    b_paketrekur=Button(pencere,  cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Yeniden kur",command=paketrekur)
    b_paketrekur.pack()
    b_paketsil=Button(pencere,  cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Kaldır",command=paketsil)
    b_paketsil.pack()
    b_metin5=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 1")
    b_metin5.pack()
    yazi3=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 9 bold", text="Bilgilendirme: Açılacak komut çıktısında bazı hatalar (anlamsız harfler, sayılar vb.) olabilir.\nLütfen bunu dikkate almayınız.")
    yazi3.pack()
    b_metin6=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
    b_metin6.pack()
    buton_4=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü kapat\nAna menüye dön", command=kapat)
    buton_4.pack()
    buton_5=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
    buton_5.pack()
    
main()

mainloop()