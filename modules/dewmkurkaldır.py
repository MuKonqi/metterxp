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
    print("Modül kapatılıyor...")
    exit()
    
def reopen():
    print("\nModül yeniden başlatılıyor...")
    pencere.destroy()
    os.system(" python3 /usr/local/bin/metterxp/modules/dewmkurkaldır.py")

def reboot():
    print("\nBilgisayarınız yeniden başlatılıyor...")
    os.system(" reboot")


if os.path.isfile(debian):
    pencere=Tk()
    pencere.title("Masaüstü ortamı/pencere yöneticisi kur/yeniden kur/kaldır | MetterXP")
    pencere.config(background="#000000")
    pencere.resizable(0, 0)
    
    def kde():
        def kur():
            try:
                print("\nKDE Plasma DE kurulumu başlatılıyor...")
                os.system(" apt install kde-plasma-desktop -y")
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nKDE Plasma DE yeniden kuruluyor...")
                os.system(" apt reinstall kde-plasma-desktop -y")
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nKDE Plasma DE kaldırılıyor...")
                os.system(" apt purge kde-plasma-desktop* -y")
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="KDE Plasma DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def gnome():
        def kur():
            try:
                print("\nGNOME DE kurulumu başlatılıyor...")
                os.system(" apt install gnome gnome-shell -y")
                messagebox.showinfo("Bilgilendirme","GNOME DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nGNOME DE yeniden kuruluyor...")
                os.system(" apt reinstall gnome gnome-shell -y")
                messagebox.showinfo("Bilgilendirme","GNOME DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nGNOME DE kaldırılıyor...")
                os.system(" apt purge gnome* -y")
                messagebox.showinfo("Bilgilendirme","GNOME DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="GNOME DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def cinnamon():
        def kur():
            try:
                print("\nCinnamon DE kurulumu başlatılıyor...")
                os.system(" apt install cinnamon -y")
                messagebox.showinfo("Bilgilendirme","Cinnamon DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nCinnamon DE yeniden kuruluyor...")
                os.system(" apt reinstall cinnamon -y")
                messagebox.showinfo("Bilgilendirme","Cinnamon DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nCinnamon DE kaldırılıyor...")
                os.system(" apt purge cinnamon* -y")
                messagebox.showinfo("Bilgilendirme","Cinnamon DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="Cinnamon DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def mate():
        def kur():
            try:
                print("\nMate DE kurulumu başlatılıyor...")
                os.system(" apt install mate-desktop-enviroment mate-desktop-enviroment-core mate-desktop-enviroment-extra -y")
                messagebox.showinfo("Bilgilendirme","Mate DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nMate DE yeniden kuruluyor...")
                os.system(" apt reinstall mate-desktop-enviroment mate-desktop-enviroment-core mate-desktop-enviroment-extra -y")
                messagebox.showinfo("Bilgilendirme","Mate DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nMate DE kaldırılıyor...")
                os.system(" apt purge mate-desktop-enviroment* -y")
                messagebox.showinfo("Bilgilendirme","Mate DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="Mate DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def xfce():
        def kur():
            try:
                print("\nXfce DE kurulumu başlatılıyor...")
                os.system(" apt install xfce4 -y")
                messagebox.showinfo("Bilgilendirme","Xfce DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nXfce DE yeniden kuruluyor...")
                os.system(" apt reinstall xfce4 -y")
                messagebox.showinfo("Bilgilendirme","Xfce DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nXfce DE kaldırılıyor...")
                os.system(" apt purge xfce4* -y")
                messagebox.showinfo("Bilgilendirme","Xfce DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="Xfce DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def deepin():
        def kur():
            try:
                print("\nDeepin DE kurulumu başlatılıyor...")
                os.system(" apt install software-properties-common -y")
                os.system(" add-apt-repository ppa:ubuntudde-dev/stable -y")
                os.system(" apt update -y")
                os.system(" apt install dde -y")
                messagebox.showinfo("Bilgilendirme","Deepin DE kurulum işlemi tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nDeepin DE yeniden kuruluyor...")
                os.system(" apt reinstall dde -y")
                messagebox.showinfo("Bilgilendirme","Deepin DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nDeepin DE kaldırılıyor...")
                os.system(" apt purge dde* -y")
                messagebox.showinfo("Bilgilendirme","Deepin DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="Deepin DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        yazi2.config(text="Not: Deepin DE'i kurma işlemi tamamen stabil değildir.\nDE = Desktop Enviroment = Masaüstü Ortamı\nWM = Window Manager = Pencere Yöneticisi")
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def lxde():
        def kur():
            try:
                print("\nLXDE kurulumu başlatılıyor...")
                os.system(" apt install lxde -y")
                messagebox.showinfo("Bilgilendirme","LXDE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nLXDE yeniden kuruluyor...")
                os.system(" apt reinstall lxde -y")
                messagebox.showinfo("Bilgilendirme","LXDE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nLXDE kaldırılıyor...")
                os.system(" apt purge lxde* -y")
                messagebox.showinfo("Bilgilendirme","LXDE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="LXDE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def lxqt():
        def kur():
            try:
                print("\nLXQt DE kurulumu başlatılıyor...")
                os.system(" apt install openbox pcmanfm-qt lxqt-admin lxqt-common lxqt-config lxqt-globalkeys lxqt-notificationd lxqt-panel lxqt-policykit lxqt-powermanagement lxqt-qtplugin lxqt-runner lxqt-session lxqt- -y")
                messagebox.showinfo("Bilgilendirme","LXQt DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\LXQt DE yeniden kuruluyor...")
                os.system(" apt reinstall openbox pcmanfm-qt lxqt-admin lxqt-common lxqt-config lxqt-globalkeys lxqt-notificationd lxqt-panel lxqt-policykit lxqt-powermanagement lxqt-qtplugin lxqt-runner lxqt-session lxqt- -y")
                messagebox.showinfo("Bilgilendirme","LXQt DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            def openboxsil():
                try:
                    print("\nOpenBox WM kaldırılıyor...")
                    os.system(" apt purge openbox* -y")
                    messagebox.showinfo("Bilgilendirme","LXQt DE'in kullandığı OpenBox WM kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                    reboot()
                except:
                    messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                    kapat()
            try:
                print("\nLXQt DE OpenBox WM hariç kaldırılıyor...")
                os.system(" apt purge pcmanfm-qt lxqt-admin lxqt-common lxqt-config lxqt-globalkeys lxqt-notificationd lxqt-panel lxqt-policykit lxqt-powermanagement lxqt-qtplugin lxqt-runner lxqt-session lxqt- -y")
                yazi1.config(text="LXQt DE'in kullandığı OpenBox WM hariç her şey kaldırıldı.")
                islemsecimbuton1.config(text="LXQt DE'in kullandığı OpenBox WM'ı kaldırma\nHemen bilgisayarı yeniden başlat", command=reboot)
                islemsecimbuton2.config(text="LXQt DE'in kullandığı OpenBox WM'i kaldır\nOpenBox WM'i kaldırılınca bilgisayarı yeniden başlat", command=openboxsil)
                islemsecimbuton3.destroy()
                islemsecimbuton4.destroy()
                islemsecimbuton5.destroy()
                islemsecimbuton6.destroy()
                islemsecimbuton7.destroy()
                islemsecimbuton8.destroy()
                islemsecimbuton9.destroy()
                islemsecimbuton10.destroy()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="LXQt DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def openbox():
        def kur():
            try:
                print("\nOpenBox WM kurulumu başlatılıyor...")
                os.system(" apt install openbox -y")
                messagebox.showinfo("Bilgilendirme","OpenBox WM kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nOpenBox WM yeniden kuruluyor...")
                os.system(" apt reinstall openbox -y")
                messagebox.showinfo("Bilgilendirme","OpenBox WM yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nOpenBox WM kaldırılıyor...")
                os.system(" apt purge openbox* -y")
                messagebox.showinfo("Bilgilendirme","OpenBox WM kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="OpenBox WM için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def i3():
        def kur():
            try:
                print("\nİ3 WM kurulumu başlatılıyor...")
                os.system(" apt install i3 -y")
                messagebox.showinfo("Bilgilendirme","İ3 WM kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nİ3 WM yeniden kuruluyor...")
                os.system(" apt reinstall i3 -y")
                messagebox.showinfo("Bilgilendirme","İ3 WM yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nİ3 WM kaldırılıyor...")
                os.system(" apt purge i3* -y")
                messagebox.showinfo("Bilgilendirme","İ3 WM kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="İ3 WM için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    yazi1=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 10 bold", text="Hangi masaüstü ortamını/pencere yöneticisi kurmak ya da kaldırmak istiyorsunuz?")
    yazi1.pack()
    b_metin1=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
    b_metin1.pack()
    islemsecimbuton1=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="KDE Plasma DE",command=kde)
    islemsecimbuton1.pack()
    islemsecimbuton2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="GNOME DE",command=gnome)
    islemsecimbuton2.pack()
    islemsecimbuton3=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Cinnamon DE",command=cinnamon)
    islemsecimbuton3.pack()
    islemsecimbuton4=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Mate DE",command=mate)
    islemsecimbuton4.pack()
    islemsecimbuton5=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Xfce DE",command=xfce)
    islemsecimbuton5.pack()
    islemsecimbuton6=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Deepin DE",command=deepin)
    islemsecimbuton6.pack()
    islemsecimbuton7=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="LXDE",command=lxde)
    islemsecimbuton7.pack()
    islemsecimbuton8=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="LXQt DE",command=lxqt)
    islemsecimbuton8.pack()
    islemsecimbuton9=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="OpenBox WM",command=openbox)
    islemsecimbuton9.pack()
    islemsecimbuton10=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="İ3 WM",command=i3)
    islemsecimbuton10.pack()
    b_metin2=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 1")
    b_metin2.pack()
    yazi2=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 9 bold", text="DE = Desktop Enviroment = Masaüstü Ortamı\nWM = Window Manager = Pencere Yöneticisi")
    yazi2.pack()
    b_metin3=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
    b_metin3.pack()
    buton_1=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü kapat\nAna menüye dön", command=kapat)
    buton_1.pack()
    
    
elif os.path.isfile(fedora):
    pencere=Tk()
    pencere.title("Masaüstü ortamı/pencere yöneticisi kur/kaldır | MetterXP")
    pencere.config(background="#000000")
    pencere.resizable(0, 0)
    
    def kde():
        def kur():
            try:
                print("\nKDE Plasma DE kurulumu başlatılıyor...")
                os.system(" dnf install @kde-desktop -y")
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nKDE Plasma DE yeniden kuruluyor...")
                os.system(" dnf reinstall @kde-desktop -y")
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nKDE Plasma DE kaldırılıyor...")
                os.system(" dnf remove @kde-desktop -y")
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="KDE Plasma DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        islemsecimbuton11.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def gnome():
        def kur():
            try:
                print("\nGNOME DE kurulumu başlatılıyor...")
                os.system(" dnf install @gnome-desktop -y")
                messagebox.showinfo("Bilgilendirme","GNOME DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nGNOME DE yeniden kuruluyor...")
                os.system(" dnf reinstall @gnome-desktop -y")
                messagebox.showinfo("Bilgilendirme","GNOME DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nGNOME DE kaldırılıyor...")
                os.system(" dnf remove @gnome-desktop -y")
                messagebox.showinfo("Bilgilendirme","GNOME DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="GNOME DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        islemsecimbuton11.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def cinnamon():
        def kur():
            try:
                print("\nCinnamon DE kurulumu başlatılıyor...")
                os.system(" dnf install @cinnamon-desktop -y")
                messagebox.showinfo("Bilgilendirme","Cinnamon DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nCinnamon DE yeniden kuruluyor...")
                os.system(" dnf reinstall @cinnamon-desktop -y")
                messagebox.showinfo("Bilgilendirme","Cinnamon DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nCinnamon DE kaldırılıyor...")
                os.system(" dnf remove @cinnamon-desktop -y")
                messagebox.showinfo("Bilgilendirme","Cinnamon DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="Cinnamon DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        islemsecimbuton11.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def mate():
        def kur():
            try:
                print("\nMate DE kurulumu başlatılıyor...")
                os.system(" dnf install @mate-desktop")
                messagebox.showinfo("Bilgilendirme","Mate DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nMate DE yeniden kuruluyor...")
                os.system(" dnf reinstall @mate-desktop")
                messagebox.showinfo("Bilgilendirme","Mate DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nMate DE kaldırılıyor...")
                os.system(" dnf remove @mate-desktop -y")
                messagebox.showinfo("Bilgilendirme","Mate DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="Mate DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        islemsecimbuton11.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def xfce():
        def kur():
            try:
                print("\nXfce DE kurulumu başlatılıyor...")
                os.system(" dnf install @xfce-desktop -y")
                messagebox.showinfo("Bilgilendirme","Xfce DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nXfce DE yeniden kuruluyor...")
                os.system(" dnf reinstall @xfce-desktop -y")
                messagebox.showinfo("Bilgilendirme","Xfce DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nXfce DE kaldırılıyor...")
                os.system(" dnf remove @xfce-desktop -y")
                messagebox.showinfo("Bilgilendirme","Xfce DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="Xfce DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        islemsecimbuton11.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def deepin():
        def kur():
            try:
                print("\nDeepin DE kurulumu başlatılıyor...")
                os.system(" dnf install @deepin-desktop")
                messagebox.showinfo("Bilgilendirme","Deepin DE kurulum işlemi tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nDeepin DE yeniden kuruluyor...")
                os.system(" dnf reinstall @deepin-desktop -y")
                messagebox.showinfo("Bilgilendirme","Deepin DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nDeepin DE kaldırılıyor...")
                os.system(" dnf remove @deepin-desktop -y")
                messagebox.showinfo("Bilgilendirme","Deepin DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="Deepin DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        islemsecimbuton11.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def pantheon():
        def kur():
            try:
                print("\nPantheon DE kurulumu başlatılıyor...")
                os.system(" dnf group install 'pantheon desktop' -y")
                messagebox.showinfo("Bilgilendirme","Pantheon DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nPantheon DE yeniden kuruluyor...")
                os.system(" dnf group reinstall 'pantheon desktop' -y")
                messagebox.showinfo("Bilgilendirme","Pantheon DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nPantheon DE kaldırılıyor...")
                os.system(" dnf group remove 'pantheon desktop' -y")
                messagebox.showinfo("Bilgilendirme","Pantheon DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="Pantheon DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        islemsecimbuton11.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def lxde():
        def kur():
            try:
                print("\nLXDE kurulumu başlatılıyor...")
                os.system(" dnf install @lxde-desktop -y")
                messagebox.showinfo("Bilgilendirme","LXDE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nLXDE yeniden kuruluyor...")
                os.system(" dnf reinstall @lxde-desktop -y")
                messagebox.showinfo("Bilgilendirme","LXDE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nLXDE kaldırılıyor...")
                os.system(" dnf remove @lxde-desktop -y")
                messagebox.showinfo("Bilgilendirme","LXDE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="LXDE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        islemsecimbuton11.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def lxqt():
        def kur():
            try:
                print("\nLXQt DE kurulumu başlatılıyor...")
                os.system(" dnf install @lxqt-desktop -y")
                messagebox.showinfo("Bilgilendirme","LXQt DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\LXQt DE yeniden kuruluyor...")
                os.system(" dnf reinstall @lxqt-desktop -y")
                messagebox.showinfo("Bilgilendirme","LXQt DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nLXQt DE kaldırılıyor...")
                os.system(" dnf remove @lxqt-desktop")
                messagebox.showinfo("Bilgilendirme","LXQt DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="LXQt DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        islemsecimbuton11.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def openbox():
        def kur():
            try:
                print("\nOpenBox WM kurulumu başlatılıyor...")
                os.system(" dnf install openbox obconf -y")
                messagebox.showinfo("Bilgilendirme","OpenBox WM kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nOpenBox WM yeniden kuruluyor...")
                os.system(" dnf reinstall openbox obconf -y")
                messagebox.showinfo("Bilgilendirme","OpenBox WM yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nOpenBox WM kaldırılıyor...")
                os.system(" dnf remove openbox obconf -y")
                messagebox.showinfo("Bilgilendirme","OpenBox WM kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="OpenBox WM için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        islemsecimbuton11.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def i3():
        def kur():
            try:
                print("\nİ3 WM kurulumu başlatılıyor...")
                os.system(" dnf install i3 i3status i3lock dmenu -y")
                messagebox.showinfo("Bilgilendirme","İ3 WM kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nİ3 WM yeniden kuruluyor...")
                os.system(" dnf reinstall i3 i3status i3lock dmenu -y")
                messagebox.showinfo("Bilgilendirme","İ3 WM yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nİ3 WM kaldırılıyor...")
                os.system(" dnf remove i3 i3status i3lock dmenu -y")
                messagebox.showinfo("Bilgilendirme","İ3 WM kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="İ3 WM için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        islemsecimbuton11.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
            
    yazi1=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 10 bold", text="Hangi masaüstü ortamını/pencere yöneticisi kurmak ya da kaldırmak istiyorsunuz?")
    yazi1.pack()
    b_metin1=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
    b_metin1.pack()
    islemsecimbuton1=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="KDE Plasma DE",command=kde)
    islemsecimbuton1.pack()
    islemsecimbuton2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="GNOME DE",command=gnome)
    islemsecimbuton2.pack()
    islemsecimbuton3=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Cinnamon DE",command=cinnamon)
    islemsecimbuton3.pack()
    islemsecimbuton4=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Mate DE",command=mate)
    islemsecimbuton4.pack()
    islemsecimbuton5=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Xfce DE",command=xfce)
    islemsecimbuton5.pack()
    islemsecimbuton6=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Deepin DE",command=deepin)
    islemsecimbuton6.pack()
    islemsecimbuton7=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Pantheon DE",command=pantheon)
    islemsecimbuton7.pack()    
    islemsecimbuton8=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="LXDE",command=lxde)
    islemsecimbuton8.pack()
    islemsecimbuton9=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="LXQt DE",command=lxqt)
    islemsecimbuton9.pack()
    islemsecimbuton10=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="OpenBox WM",command=openbox)
    islemsecimbuton10.pack()
    islemsecimbuton11=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="İ3 WM",command=i3)
    islemsecimbuton11.pack()
    b_metin2=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 1")
    b_metin2.pack()
    yazi2=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 9 bold", text="DE = Desktop Enviroment = Masaüstü Ortamı\nWM = Window Manager = Pencere Yöneticisi")
    yazi2.pack()
    b_metin3=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
    b_metin3.pack()
    buton_1=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü kapat\nAna menüye dön", command=kapat)
    buton_1.pack()
    
    
elif os.path.isfile(solus):
    pencere=Tk()
    pencere.title("Masaüstü ortamı/pencere yöneticisi kur/kaldır | MetterXP")
    pencere.config(background="#000000")
    pencere.resizable(0, 0)
    
    def kde():
        def kur():
            try:
                print("\nKDE Plasma DE kurulumu başlatılıyor...")
                os.system(" eopkg it -c desktop.kde -y")
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nKDE Plasma DE yeniden kuruluyor...")
                os.system(" eopkg it -c desktop.kde --rei -y")
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nKDE Plasma DE kaldırılıyor...")
                os.system(" eopkg rm -c desktop.kde -y")
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="KDE Plasma DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def gnome():
        def kur():
            try:
                print("\nGNOME DE kurulumu başlatılıyor...")
                os.system(" eopkg it -c desktop.gnome -y")
                messagebox.showinfo("Bilgilendirme","GNOME DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nGNOME DE yeniden kuruluyor...")
                os.system(" eopkg it -c desktop.gnome --rei -y")
                messagebox.showinfo("Bilgilendirme","GNOME DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nGNOME DE kaldırılıyor...")
                os.system(" eopkg rm -c desktop.gnome -y")
                messagebox.showinfo("Bilgilendirme","GNOME DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="GNOME DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def budgie():
        def kur():
            try:
                print("\nBudgie DE kurulumu başlatılıyor...")
                os.system(" eopkg it -c desktop.budgie -y")
                messagebox.showinfo("Bilgilendirme","Budgie DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nBudgie DE yeniden kuruluyor...")
                os.system(" eopkg it -c desktop.budgie --rei -y")
                messagebox.showinfo("Bilgilendirme","Budgie DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nBudgie DE kaldırılıyor...")
                os.system(" eopkg rm -c desktop.budgie -y")
                messagebox.showinfo("Bilgilendirme","Budgie DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="Budgie DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def mate():
        def kur():
            try:
                print("\nMate DE kurulumu başlatılıyor...")
                os.system(" eopkg it -c desktop.mate -y")
                messagebox.showinfo("Bilgilendirme","Mate DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nMate DE yeniden kuruluyor...")
                os.system(" eopkg it -c desktop.mate --rei -y")
                messagebox.showinfo("Bilgilendirme","Mate DE yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nMate DE kaldırılıyor...")
                os.system(" eopkg rm -c desktop.mate -y")
                messagebox.showinfo("Bilgilendirme","Mate DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="Mate DE için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()    
    def openbox():
        def kur():
            try:
                print("\nOpenBox WM kurulumu başlatılıyor...")
                os.system(" eopkg it openbox obconf -y")
                messagebox.showinfo("Bilgilendirme","OpenBox WM kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nOpenBox WM yeniden kuruluyor...")
                os.system(" eopkg it openbox obconf --rei -y")
                messagebox.showinfo("Bilgilendirme","OpenBox WM yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nOpenBox WM kaldırılıyor...")
                os.system(" eopkg rm openbox obconf -y")
                messagebox.showinfo("Bilgilendirme","OpenBox WM kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="OpenBox WM için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
    def i3():
        def kur():
            try:
                print("\nİ3 WM kurulumu başlatılıyor...")
                os.system(" eopkg it i3 -y")
                messagebox.showinfo("Bilgilendirme","İ3 WM kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def rekur():
            try:
                print("\nİ3 WM yeniden kuruluyor...")
                os.system(" eopkg it i3 --rei -y")
                messagebox.showinfo("Bilgilendirme","İ3 WM yeniden kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        def sil():
            try:
                print("\nİ3 WM kaldırılıyor...")
                os.system(" eopkg rm i3 -y")
                messagebox.showinfo("Bilgilendirme","İ3 WM kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
            except:
                messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
                kapat()
        yazi1.config(text="İ3 WM için ne yapmak istiyorsunuz?")
        islemsecimbuton1.config(text="Kur", command=kur)
        islemsecimbuton2.config(text="Yeniden kur", command=rekur)
        islemsecimbuton3.config(text="Kaldır", command=sil)
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        buton_2.pack()
            
    yazi1=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 10 bold", text="Hangi masaüstü ortamını/pencere yöneticisi kurmak ya da kaldırmak istiyorsunuz?")
    yazi1.pack()
    b_metin1=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
    b_metin1.pack()
    islemsecimbuton1=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="KDE Plasma DE",command=kde)
    islemsecimbuton1.pack()
    islemsecimbuton2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="GNOME DE",command=gnome)
    islemsecimbuton2.pack()
    islemsecimbuton3=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Budgie DE",command=budgie)
    islemsecimbuton3.pack()
    islemsecimbuton4=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Mate DE",command=mate)
    islemsecimbuton4.pack()
    islemsecimbuton5=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="İ3 WM",command=i3)
    islemsecimbuton5.pack()
    islemsecimbuton6=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="OpenBox WM",command=openbox)
    islemsecimbuton6.pack()
    b_metin2=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 1")
    b_metin2.pack()
    yazi2=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 9 bold", text="DE = Desktop Enviroment = Masaüstü Ortamı\nWM = Window Manager = Pencere Yöneticisi")
    yazi2.pack()
    b_metin3=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
    b_metin3.pack()
    buton_1=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Modülü kapat\nAna menüye dön", command=kapat)
    buton_1.pack() 
       
       
else:
    print("Kullandığınız işletim sistemi/dağıtımı MetterXP desteklenmemektedir.")
    exit()
    

mainloop()