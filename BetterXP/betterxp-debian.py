#!/usr/bin/env python3

# Copyright (C) 2021, Muhammed Abdurrahman

# BetterXP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# BetterXP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with BetterXP.  If not, see <https://www.gnu.org/licenses/>.

from sys import exec_prefix
from tkinter import *
from tkinter import messagebox
import os
def reboot():
    print("\nBilgisayarınız yeniden başlatılıyor...")
    os.system("sudo reboot")
def programkapat():
    print("\nBetterXP kapatılıyor...")
    exit()
def bxpreopen():
    if os.path.isfile("/etc/debian-version"):
        print("\nBetterXP yeniden başlatılıyor...\n")
        pencere.destroy()
        os.system("python3 /usr/local/bin/BetterXP/betterxp-debian.py")
    elif os.path.isfile("/etc/fedora-release"):
        print("\nBetterXP yeniden başlatılıyor...\n")
        pencere.destroy()
        os.system("python3 /usr/local/bin/BetterXP/betterxp-fedora.py")
    elif os.path.isfile("/etc/solus-release"):
        print("\nBetterXP yeniden başlatılıyor...\n")
        pencere.destroy()
        os.system("python3 /usr/local/bin/BetterXP/betterxp-solus.py")
    else:
        if os.name == "nt":
            messagebox.showerror("Bilgilendirme","BetterXP, NT çekirdeğini kullanan işletim sistemlerinde (Windows, ReactOS) çalışmaz.\nLütfen 'OK' tuşuna basıp programı kapatın.")
            programkapat()
        messagebox.showerror("Bilgilendirme","Kullandığınız dağıtımı BetterXP desteklemiyor.\nLütfen 'OK' tuşuna basıp programı kapatın.")
        programkapat()
def dewmkurucu():
    yazi2.config(text="Lütfen kurmak istediğiniz masaüstü ortamını/pencere yöneticisini seçiniz.")
    islemsecimbuton1.config(text="KDE Plasma DE'i kur",command=kdekur)
    islemsecimbuton2.config(text="GNOME DE'i kur",command=gnomekur)
    islemsecimbuton3.config(text="Xfce DE'i kur",command=xfcekur)
    islemsecimbuton4.config(text="Cinnamon DE'i kur",command=cinnamonkur)
    islemsecimbuton5.config(text="Mate DE'i kur",command=matekur)
    islemsecimbuton6.config(text="Deepin DE'i kur",command=ddekur)
    islemsecimbuton7.config(text="LXDE'i kur",command=lxdekur)
    islemsecimbuton8.config(text="LXQt DE'i kur",command=lxqtkur)
    islemsecimbuton9.config(text="OpenBox WM'i kur",command=openboxkur)
    islemsecimbuton10.config(text="İ3 WM'i kur",command=i3kur)
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def gnomekur():
    try:
        print("\nGNOME DE kurulumu başlatılıyor...")
        os.system("sudo apt install gnome -y")
        os.system("sudo apt install gnome-shell")
        messagebox.showinfo("Bilgilendirme","GNOME DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def kdekur():
    try:
        print("\nKDE Plasma DE kurulumu başlatılıyor...")
        os.system("sudo apt install kde-plasma-desktop -y")
        messagebox.showinfo("Bilgilendirme","KDE Plasma DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def cinnamonkur():
    try:
        print("\nCinnamon DE kurulumu başlatılıyor...")
        os.system("sudo apt install cinnamon -y")
        messagebox.showinfo("Bilgilendirme","Cinnamon DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def lxdekur():
    try:
        print("\nLXDE kurulumu başlatılıyor...")
        os.system("sudo apt install lxde -y")
        messagebox.showinfo("Bilgilendirme","LXDE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def lxqtkur():
    try:
        print("\nLXQt DE kurulumu başlatılıyor...")
        os.system("sudo apt install software-properties-common -y")
        os.system("sudo add-apt-repository -y ppa:lubuntu-dev/lubuntu-daily")
        os.system("sudo apt-get update -y")
        os.system("sudo apt upgrade -y")
        os.system("sudo apt install openbox pcmanfm-qt lxqt-admin lxqt-common lxqt-config lxqt-globalkeys lxqt-notificationd lxqt-panel lxqt-policykit lxqt-powermanagement lxqt-qtplugin lxqt-runner lxqt-session lxqt-sudo")
        messagebox.showinfo("Bilgilendirme","LXQt DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def matekur():
    try:
        print("\nMate DE kurulumu başlatılıyor...")
        os.system("sudo apt install mate-desktop-environment-core -y")
        os.system("sudo apt install mate-desktop-environment -y")
        os.system("sudo apt install mate-desktop-environment-extras -y")
        messagebox.showinfo("Bilgilendirme","Mate DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def openboxkur():
    try:
        print("\nOpenBox WM kurulumu başlatılıyor...")
        os.system("sudo apt install openbox -y")
        messagebox.showinfo("Bilgilendirme","OpenBox WM kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def xfcekur():
    try:
        print("\nXfce DE kurulumu başlatılıyor...")
        os.system("sudo apt install xfce4 -y")
        messagebox.showinfo("Bilgilendirme","Xfce DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def i3kur():
    try:
        print("\nİ3 WM kurulumu başlatılıyor...")
        os.system("sudo apt install i3 -y")
        messagebox.showinfo("Bilgilendirme","İ3 WM kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def ddekur():
    try:
        print("\nDeepin DE kurulumu başlatılıyor...")
        os.system("sudo apt install software-properties-common -y")
        os.system("sudo add-apt-repository ppa:ubuntudde-dev/stable -y")
        os.system("sudo apt update -y")
        os.system("sudo apt install dde -y")
        messagebox.showinfo("Bilgilendirme","Deepin DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def dewmsilici():
    yazi2.config(text="Lütfen kaldırmak istediğiniz masaüstü ortamını/pencere yöneticisi seçiniz.")
    islemsecimbuton1.config(text="KDE Plasma DE'i kaldır",command=kdesil)
    islemsecimbuton2.config(text="GNOME DE'i kaldır",command=gnomesil)                          
    islemsecimbuton3.config(text="Xfce DE'i kaldır",command=xfcesil)
    islemsecimbuton4.config(text="Cinnamon DE'i kaldır",command=cinnamonsil)
    islemsecimbuton5.config(text="Mate DE'i kaldır",command=matesil)
    islemsecimbuton6.config(text="Deepin DE'i kaldır",command=ddesil)
    islemsecimbuton7.config(text="LXDE'i kaldır",command=lxdesil)
    islemsecimbuton8.config(text="LXQt DE'i kaldır",command=lxqtsil)
    islemsecimbuton9.config(text="OpenBox WM'i kaldır",command=openboxsil)
    islemsecimbuton10.config(text="İ3 WM'i kaldır",command=i3sil)
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def kdesil():
    try:
        print("\nKDE Plasma DE kaldırılıyor...")
        os.system("sudo apt purge kde* -y")
        messagebox.showinfo("Bilgilendirme","KDE Plasma DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def gnomesil():
    try:
        print("\nGNOME DE kaldırılıyor...")
        os.system("sudo apt purge gnome* -y")
        messagebox.showinfo("Bilgilendirme","GNOME DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def cinnamonsil():
    try:
        print("\nCinnamon DE kaldırılıyor...")
        os.system("sudo apt purge cinnamon* -y")
        messagebox.showinfo("Bilgilendirme","Cinnamon DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def lxdesil():
    try:
        print("\nLXDE kaldırılıyor...")
        os.system("sudo apt purge lxde* -y")
        os.system("sudo apt autoremove -y")
        messagebox.showinfo("Bilgilendirme","LXDE DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def lxqtsil():
    try:
        islemsecimbuton1.destroy()
        islemsecimbuton2.destroy()
        islemsecimbuton3.destroy()
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        islemsecimbuton11.destroy()
        islemsecimbuton12.destroy()
        buton1.destroy()
        buton2.destroy()
        b_metin1.destroy()
        print("\nLXQt DE kaldırılıyor...")
        os.system("sudo apt purge lxqt-admin lxqt-common lxqt-config lxqt-globalkeys lxqt-notificationd lxqt-panel lxqt-policykit lxqt-powermanagement lxqt-qtplugin lxqt-runner lxqt-session lxqt-sudo -y")
        os.system("sudo apt autoremove -y")
        yazi2.config(text="LXQt masaüstü ortamını kullandığı pencere yöneticisi olan OpenBox hariç herşeyin kaldırılma işlemi tamamlandı.")
        b_1_lxqt_rm=Button(pencere,  cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="LXQt'nin kullandığı WM olan OpenBox'ı kaldır",command=openboxsil)
        b_2_lxqt_rm=Button(pencere,  cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="LXQt'nin kullandığı WM olan OpenBox'ı kaldırma\nBilgisayarı yeniden başlat",command=reboot)
        b_1_lxqt_rm.pack()
        b_2_lxqt_rm.pack()
        b_metin2=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n")
        buton_1=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="BetterXP'ı kapat", command=programkapat)
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="BetterXP'ı yeniden aç", command=bxpreopen)
        b_metin2.pack()
        buton_1.pack()
        buton_2.pack()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def matesil():
    try:
        print("\nMate DE kaldırılıyor...")
        messagebox.showinfo("Bilgilendirme","Mate DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def xfcesil():
    try:
        print("\nXfce DE kaldırılıyor...")
        os.system("sudo apt autoremove -y")
        os.system("sudo apt -f install -y")
        os.system("sudo apt clean -y")
        os.system("sudo apt autoclean -y")
        os.system("sudo apt update -y")
        os.system("sudo apt purge xfce4* -y")
        os.system("sudo apt autoremove -y")
        messagebox.showinfo("Bilgilendirme","Xfce DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def openboxsil():
    try:
        print("\nOpenBox WM kaldırılıyor...")
        os.system("sudo apt purge openbox* -y")
        os.system("sudo apt autoremove -y")
        messagebox.showinfo("Bilgilendirme","OpenBox WM kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def i3sil():
    try:
        print("\İ3 WM kaldırılıyor...")
        os.system("sudo apt purge i3* -y")
        os.system("sudo apt autoremove -y")
        messagebox.showinfo("Bilgilendirme","İ3 WM kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def ddesil():
    try:
        print("\nDeepin DE kaldırılıyor...")
        os.system("sudo apt purge dde* -y")
        os.system("sudo apt autoremove -y")
        messagebox.showinfo("Bilgilendirme","Deepin DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def programkurucu():         
    yazi2.config(text="Hangi programı kurmak istiyorsunuz?")
    islemsecimbuton1.config(text="Firefox'u kur",command=firefoxkur)
    islemsecimbuton2.config(text="Chromium'u kur",command=chromiumkur)
    islemsecimbuton3.config(text="VLC oynatıcısını kur",command=vlckur)
    islemsecimbuton4.config(text="LibreOffice ofis programını kur",command=libreofficekur)
    islemsecimbuton5.config(text="OBS Studio ekran kaydedicisini kur",command=obskur)
    islemsecimbuton6.config(text="CUPS yazıcı yöneticisini kur",command=cupskur)
    islemsecimbuton7.config(text="Plank'ı kur",command=plankkur)
    islemsecimbuton8.config(text="GParted disk bölümü düzenleyicisini kur",command=gpartedkur)
    islemsecimbuton9.config(text="GIMP görüntü işleme programını  kur",command=gimpkur)
    islemsecimbuton10.config(text="Audacity'i kur",command=audacitykur)
    islemsecimbuton11.config(text="Wine'ı kur",command=winekur)
    islemsecimbuton12.config(text="PlayOnLinux'u kur",command=playonlinuxkur)
def libreofficekur():
    try:
        print("\nLibreOffice kurulumu başlatılıyor...")
        os.system("sudo add-apt-repository ppa:libreoffice/ppa -y")
        os.system("sudo apt update -y")
        os.system("sudo apt install libreoffice -y")
        os.system("sudo add-apt-repository --remove ppa:libreoffice/ppa -y")
        os.system("sudo apt update -y")
        messagebox.showinfo("Bilgilendirme","LibreOffice ofis programı başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def gimpkur():
    try:
        print("\nGIMP kurulumu başlatılıyor...")
        os.system("sudo apt install gimp -y")
        messagebox.showinfo("Bilgilendirme","GIMP görüntü işleme programı başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def plankkur():
    try:
        print("\nPlank kurulumu başlatılıyor...")
        os.system("sudo apt install plank -y")
        messagebox.showinfo("Bilgilendirme","Plank başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def cupskur():
    try:
        print("\nCups kurulumu başlatılıyor...")
        os.system("sudo apt install cups -y")
        messagebox.showinfo("Bilgilendirme","Cups yazıcı yöneticisi başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat() 
def obskur():
    try:
        print("\nOBS Studio kurulumu başlatılıyor...")
        os.system("sudo apt install obs-studio -y")
        messagebox.showinfo("Bilgilendirme","OBS Stuido ekran kaydedici başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()  
def vlckur():
    try:
        print("\nVLC kurulumu başlatılıyor...")
        os.system("sudo apt install vlc -y")
        messagebox.showinfo("Bilgilendirme","VLC video oynatıcısı başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def playonlinuxkur():
    try:
        print("\nPlayOnLinux kurulumu başlatılıyor...")
        os.system('sudo apt install playonlinux -y')
        messagebox.showinfo("Bilgilendirme","PlayOnLinux başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def winekur():
    try:
        print("\nWine kurulumu başlatılıyor...")
        os.system("sudo dpkg --add-architecture i386")
        os.system("sudo apt install wine-stable -y")
        messagebox.showinfo("Bilgilendirme","Wine başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def firefoxkur():
    try:
        print("\nMozilla Firefox kurulumu başlatılıyor...")
        os.system("sudo apt install firefox -y")
        messagebox.showinfo("Bilgilendirme","Mozilla Firefox internet tarayıcısı başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def chromiumkur():
    try:
        print("\nChromium kurulumu başlatılıyor...")
        os.system("sudo apt install chromium-browser -y")
        messagebox.showinfo("Bilgilendirme","Chromium internet tarayıcısı başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def audacitykur():
    try:
        print("\nAudacity kurulumu başlatılıyor...")
        os.system("sudo apt install audacity -y")
        messagebox.showinfo("Bilgilendirme","Audacity başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def kodikur():
    try:
        print("\nKODI kurulumu başlatılıyor...")
        os.system("sudo apt-get install software-properties-common -y")
        os.system("sudo add-apt-repository ppa:team-xbmc/ppa -y")
        os.system("sudo apt update -y")
        os.system("sudo apt install kodi -y")
        messagebox.showinfo("Bilgilendirme","KODI başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def gpartedkur():
    try:
        print("\nGParted kurulumu başlatılıyor...")
        os.system("sudo apt install gparted -y")
        messagebox.showinfo("Bilgilendirme","GParted disk bölümü düzenleyecisi başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def programsil():
    yazi2.config(text="Hangi programı kaldırmak istiyorsunuz?")
    islemsecimbuton1.config(text="Firefox'u kaldır",command=firefoxsil)
    islemsecimbuton2.config(text="Chromium'u kaldır",command=chromiumsil)
    islemsecimbuton3.config(text="VLC oynatıcısını kaldır",command=vlcsil)
    islemsecimbuton4.config(text="LibreOffice ofis programını kaldır",command=libreofficesil)
    islemsecimbuton5.config(text="OBS Studio ekran kaydedicisini kaldır",command=obssil)
    islemsecimbuton6.config(text="CUPS yazıcı yöneticisini kaldır",command=cupssil)
    islemsecimbuton7.config(text="Plank'ı kaldır",command=planksil)
    islemsecimbuton8.config(text="GParted disk bölümü düzenleyicisini kaldır",command=gpartedsil)
    islemsecimbuton9.config(text="GIMP görüntü işleme programını kaldır",command=gimpsil)
    islemsecimbuton10.config(text="Audacity'i kaldır",command=audacitysil)
    islemsecimbuton11.config(text="Wine'ı kaldır",command=winesil)
    islemsecimbuton12.config(text="PlayOnLinux'u kaldır",command=playonlinuxsil)
def libreofficesil():
    try:
        print("\nLibreOffice kaldırılıyor...")
        os.system("sudo apt purge libreoffice* -y")
        messagebox.showinfo("Bilgilendirme","LibreOffice ofis programı başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def gimpsil():
    try:
        print("\nGIMP kaldırılıyor...")
        os.system("sudo apt purge gimp* -y")
        messagebox.showinfo("Bilgilendirme","GIMP görüntü işleme programı başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def planksil():
    try:
        print("\nPlank kaldırılıyor...")
        os.system("sudo apt purge plank* -y")
        messagebox.showinfo("Bilgilendirme","Plank başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def cupssil():
    try:
        print("\nCups kaldırılıyor...")
        os.system("sudo apt purge cups* -y")
        messagebox.showinfo("Bilgilendirme","Cups yazıcı yöneticisi başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat() 
def obssil():
    try:
        print("\nOBS Studio kaldırılıyor...")
        os.system("sudo apt purge obs-studio* -y")
        messagebox.showinfo("Bilgilendirme","OBS Stuido ekran kaydedici başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()  
def vlcsil():
    try:
        print("\nVLC kaldırılıyor...")
        os.system("sudo apt purge vlc* -y")
        messagebox.showinfo("Bilgilendirme","VLC video oynatıcısı başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def playonlinuxsil():
    try:
        print("\nPlayOnLinux kaldırılıyor...")
        os.system('sudo apt purge playonlinux* -y')
        messagebox.showinfo("Bilgilendirme","PlayOnLinux başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def winesil():
    try:
        print("\nWine kaldırılıyor...")
        os.system("sudo apt purge wine* -y")
        messagebox.showinfo("Bilgilendirme","Wine başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def firefoxsil():
    try:
        print("\nMozilla Firefox kaldırılıyor...")
        os.system("sudo apt purge firefox* -y")
        messagebox.showinfo("Bilgilendirme","Mozilla Firefox internet tarayıcısı başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def chromiumsil():
    try:
        print("\nChromium kaldırılıyor...")
        os.system("sudo apt purge chromium-browser* -y")
        messagebox.showinfo("Bilgilendirme","Chromium internet tarayıcısı başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def audacitysil():
    try:
        print("\nAudacity kaldırılıyor...")
        os.system("sudo apt purge audacity* -y")
        messagebox.showinfo("Bilgilendirme","Audacity başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def kodisil():
    try:
        print("\nKODI kaldırılıyor...")
        os.system("sudo apt purge kodi* -y")
        messagebox.showinfo("Bilgilendirme","KODI başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def gpartedsil():
    try:
        print("\nGParted kaldırılıyor...")
        os.system("sudo apt install gparted -y")
        messagebox.showinfo("Bilgilendirme","GParted disk bölümü düzenleyecisi başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def systemup():
    try:
        print("\nSistem güncellemesi işlemi başlatılıyor...")
        os.system("sudo apt upgrade -y")
        messagebox.showinfo("Bilgilendirme","Sistem güncellemesi işlemi bitmiştir.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()   
def hatacoz():
    yazi2.config(text="Lütfen yapmak istediğiniz işlemi seçiniz.")
    islemsecimbuton1.config(text="Paket hatalarını düzelt\nNot: Bu işlem paket hatalarını düzeltmek amacıyla paket silebilir ya da kaldırabilir.",command=aptfix)
    islemsecimbuton2.config(text="DPKG'yi yapılandır",command=dpkgconfigure)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def dpkgconfigure():
    try:
        os.system("sudo dpkg --configure -a")
        messagebox.showinfo("Bilgilendirme","DPKG yapılandırma işlemi bitmiştir.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def aptfix():
    try:
        os.system("sudo apt-get install -f -y")
        messagebox.showinfo("Bilgilendirme","Paket hatalarını düzeltme işlemi bitmiştir.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()    
def gnulinuxhk():
    yazi2.config(text="Aşağıdaki listeden lütfen bir GNU/Linux dağıtımı seçiniz.")
    islemsecimbuton1.config(text="MX Linux",command=mx)
    islemsecimbuton2.config(text="Manjaro",command=manjaro)
    islemsecimbuton3.config(text="Linux Mint",command=mint)
    islemsecimbuton4.config(text="Ubuntu",command=ubuntu)
    islemsecimbuton5.config(text="Debian GNU/Linux",command=debian)
    islemsecimbuton6.config(text="Elementary OS",command=elementary)
    islemsecimbuton7.config(text="Solus",command=solus)
    islemsecimbuton8.config(text="Fedora Linux",command=fedora)
    islemsecimbuton9.config(text="Pop!_OS",command=pop)
    islemsecimbuton10.config(text="Zorin OS",command=zorin)
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def mx():
    yazi2.config(text="MX Linux, Debian GNU/Linux tabanlı ve varsayılan olarak Xfce DE'i kullanan hafif bir dağıtımdır.\nİnternet sitesi: https://mxlinux.org/")
    islemsecimbuton1.config(text="Bağlantıyı kopyala",command=mxcopy)
    islemsecimbuton2.destroy()
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def mxcopy():
    try:
        pencere.clipboard_append("https://mxlinux.org")
        pencere.update()
        messagebox.showinfo("Bilgilendirme","Bağlantı panoya kopyalandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def manjaro():
    yazi2.config(text="Manjaro, Arch Linux tabanlı ve son kullanıcı odaklı bir dağıtımdır. Manjaro'nun kendisine ait araçları vardır. Örneğin: Pamac\nİnternet sitesi: https://manjaro.org/")
    islemsecimbuton1.config(text="Bağlantıyı kopyala",command=manjarocopy)
    islemsecimbuton2.destroy()
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def manjarocopy():
    try:
        pencere.clipboard_append("https://manjaro.org")
        pencere.update()
        messagebox.showinfo("Bilgilendirme","Bağlantı panoya kopyalandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def mint():
    yazi2.config(text="Linux Mint, Ubuntu tabanlı, son kullanıcı odaklı bir dağıtımdır. Linux Mint, kendi DE'i olan Cinnamon DE'i varsayılan olarak kullanır.\nİnternet sitesi: https://linuxmint.com/")
    islemsecimbuton1.config(text="Bağlantıyı kopyala",command=mintcopy)
    islemsecimbuton2.destroy()
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def mintcopy():
    try:
        pencere.clipboard_append("https://linuxmint.com")
        pencere.update()
        messagebox.showinfo("Bilgilendirme","Bağlantı panoya kopyalandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def ubuntu():
    yazi2.config(text="Ubuntu, Debian GNU/Linux tabanlı en pöpüler GNU/Linux dağıtımlarından biridir.\nİnternet sitesi: https://ubuntu.com/")
    islemsecimbuton1.config(text="Bağlantıyı kopyala",command=ubuntucopy)
    islemsecimbuton2.destroy()
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def ubuntucopy():
    try:
        pencere.clipboard_append("https://ubuntu.com")
        pencere.update()
        messagebox.showinfo("Bilgilendirme","Bağlantı panoya kopyalandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def debian():
    yazi2.config(text="Debian GNU/Linux, ilk çıkan GNU/Linux dağıtımlarından birisidir ve bağımsızdır. Günümüzde desteklenmeye eski olmasına rağmen devam etmektedir.\nİnternet sitesi: https://www.debian.org/")
    islemsecimbuton1.config(text="Bağlantıyı kopyala",command=debiancopy)
    islemsecimbuton2.destroy()
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def debiancopy():
    try:
        pencere.clipboard_append("https://www.debian.org")
        pencere.update()
        messagebox.showinfo("Bilgilendirme","Bağlantı panoya kopyalandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def elementary():
    yazi2.config(text="ElementaryOS, Debian GNU/Linux tabanlı ve kendi DE'i olan Pantheon DE'i varsayılan olarak kullanır.\nİnternet sitesi: https://elementary.io/")
    islemsecimbuton1.config(text="Bağlantıyı kopyala",command=elementarycopy)
    islemsecimbuton2.destroy()
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def elementarycopy():
    try:
        pencere.clipboard_append("https://elementary.io")
        pencere.update()
        messagebox.showinfo("Bilgilendirme","Bağlantı panoya kopyalandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def solus():
    yazi2.config(text="Solus, PiSi tabanlı EOPKG adlı paket yöneticisini kullanan ve kendi DE'i olan Budgie DE'i varsayılan olarak kullanır. Solus, bağımsız bir dağıtımdır.\nİnternet sitesi: https://getsol.us/home/")
    islemsecimbuton1.config(text="Bağlantıyı kopyala",command=soluscopy)
    islemsecimbuton2.destroy()
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def soluscopy():
    try:
        pencere.clipboard_append("https://getsol.us")
        pencere.update()
        messagebox.showinfo("Bilgilendirme","Bağlantı panoya kopyalandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def fedora():
    yazi2.config(text="Fedora Linux, YUM'un geliştirilmiş hali olan DNF adlı paket yöneticisini kullanır. Fedora Linux, bağımsız bir dağıtımdır.\nİnternet sitesi: https://getfedora.org/tr/")
    islemsecimbuton1.config(text="Bağlantıyı kopyala",command=fedoracopy)
    islemsecimbuton2.destroy()
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def fedoracopy():
    try:
        pencere.clipboard_append("https://getfedora.org")
        pencere.update()
        messagebox.showinfo("Bilgilendirme","Bağlantı panoya kopyalandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def pop():
    yazi2.config(text="Pop!_OS, system76 tarafından üretilen Ubuntu tabanlı bir dağıtımdır. Pop!_OS'in NVIDIA sürücüleri olan ISO imajını indirme imkanı sunması dikkat çekmektedir.\nİnternet sitesi: https://pop.system76.com/")
    islemsecimbuton1.config(text="Bağlantıyı kopyala",command=popcopy)
    islemsecimbuton2.destroy()
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def popcopy():
    try:
        pencere.clipboard_append("https://pop.system76.com")
        pencere.update()
        messagebox.showinfo("Bilgilendirme","Bağlantı panoya kopyalandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def zorin():
    yazi2.config(text="Zorin OS, Ubuntu tabanlı kendi DE'i kullanan bir dağıtımdır. Zorin OS'in en üst sürümü para ödenerek edinilebilir.\nİnternet sitesi: https://zorin.com/os")
    islemsecimbuton1.config(text="Bağlantıyı kopyala",command=zorincopy)
    islemsecimbuton2.destroy()
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def zorincopy():
    try:
        pencere.clipboard_append("https://zorin.com/os")
        pencere.update()
        messagebox.showinfo("Bilgilendirme","Bağlantı panoya kopyalandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def rootuyg():
    yazi2.config(text="Lütfen açmak istediğiniz uygulamayı seçiniz.\nNot: Uygulamaları bu şekilde açıp, sistem ile uygulamalar için gerekli dosyaları silerseniz veya değiştirseniz sisteminiz ile uygulamalar hasar alabilir. Lütfen dikkatli olunuz!")
    islemsecimbuton1.config(text="Thunar'ı bu şekilde aç",command=thunaropen)
    islemsecimbuton2.config(text="Thunar'ı kur sonra bu şekilde aç",command=thunarstart)
    islemsecimbuton3.config(text="PCManFM'ı bu şekilde aç",command=pcmanfmopen)
    islemsecimbuton4.config(text="PCManFM'ı kur sonra bu şekilde aç",command=pcmanfmstart)
    islemsecimbuton5.config(text="Nautilus'u bu şekilde aç",command=nautilusopen)
    islemsecimbuton6.config(text="Nautilus'u kur sonra bu şekilde aç",command=nautilusstart)    
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def pcmanfmopen():
    try:
        print("\nPCmanFM açılıyor...")
        os.system("sudo pcmanfm")
        messagebox.showinfo("Bilgilendirme","İşlem tamamlandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def pcmanfmstart():
    try:
        print("\nPCmanFM kuruluyor...")
        os.system("sudo apt install pcmanfm -y")
        print("\nPCmanFM açılıyor...")
        os.system("sudo pcmanfm")
        messagebox.showinfo("Bilgilendirme","İşlem tamamlandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def thunaropen():
    try:
        print("\nThunar açılıyor...")
        os.system("sudo thunar")
        messagebox.showinfo("Bilgilendirme","İşlem tamamlandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def thunarstart():
    try:
        print("\nThunar kuruluyor...")
        os.system("sudo apt install thunar -y")
        print("\nThunar açılıyor...")
        os.system("sudo thunar")
        messagebox.showinfo("Bilgilendirme","İşlem tamamlandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def nautilusopen():
    try:
        print("\nNautilus açılıyor...")
        os.system("sudo nautilus")
        messagebox.showinfo("Bilgilendirme","İşlem tamamlandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def nautilusstart():
    try:
        print("\nNautilus kuruluyor...")
        os.system("sudo apt install nautilus -y")
        print("\nPCmanFM açılıyor...")
        os.system("sudo nautilus")
        messagebox.showinfo("Bilgilendirme","İşlem tamamlandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()       
def pakettoolmgr():
    yazi2.config(text="Hangi paket yöneticisini/aracı kurmak istersiniz?")
    islemsecimbuton1.config(text="Snap paket yönetcisini kur",command=snapkur)
    islemsecimbuton2.config(text="Flatpak paket yöneticisini kur",command=flatpakkur)
    islemsecimbuton3.config(text="Kali Linux araçlarını kur",command=kalitool)
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def flatpakkur():
    try:
        print("\nFlatpak kuruluyor...")
        try:
            os.system("sudo apt install flatpak -y")
        except:
            os.system("sudo add-apt-repository ppa:alexlarsson/flatpak -y && sudo apt update -y && sudo apt install flatpak -y")
        os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
        messagebox.showinfo("Hata","Bilgilendirme","Flatpak paket yöneticisi başarıyla kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def snapkur():
    try:
        print("\nSnap kuruluyor...")
        os.system("sudo apt install snapd -y")
        messagebox.showinfo("Bilgilendirme","Snap paket yöneticisi başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat() 
def kalitool():
    try:
        dosyailkhal=open("/etc/apt/sources.list", "r")
        dosyailkhaloku=dosyailkhal.read()
        dosyailkhal.close()
        with open("/etc/apt/sources.list", "r+") as dosyasonhal:
            veri = dosyasonhal.read()
            dosyasonhal.seek(0)
            dosyasonhal.write("#deb Index of /kali kali-rolling main non-free contrib\n"+veri)
            dosyasonhal.close()
        os.system('sudo apt-get -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali -y && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/") && sudo apt install aircrack-ng ')
        dosyafinal=open("/etc/apt/sources.list", "w")
        dosyafinal.write(dosyailkhaloku)
        dosyafinal.close()
        os.system("sudo apt update -y")
        messagebox.showinfo("Bilgilendirme","Kali araçlarının kurulumu bitmiştir.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()    
def info():
    yazi2.config(text="BetterXP, son kullanıcı için tasarlanmış, özgür bir yazılım ürünüdür.\nBetterXP, GNU General Public License, Version 3.0 (GPL 3) altında lisanslanmıştır.\nYapımcı: MuKonqi (Muhammed Abdurrahman)\nTemel: Terminalden kurtulun 2.0 (Kararlı Sürüm)\nSürüm: 2.0.2 (Kararlı Sürüm)")
    islemsecimbuton1.config(text="İletişim",command=contact)
    islemsecimbuton2.config(text="Yenilikler",command=yenilikler)
    islemsecimbuton3.config(text="Lisans",command=lisans)
    islemsecimbuton4.config(text="BetterXP'ın internet sitesi",command=bxpwebsite)
    islemsecimbuton5.config(text="BetterXP'ı güncelle\n(Bu işlem için internet bağlantınızın olması gereklidir.)",command=bxpup)
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def contact():
    yazi2.config(text="Bize ulaşabilmeniz için Matrix topluluğumuz:\nhttps://matrix.to/#/#betterxp-community:kde.org?via=kde.org")
    islemsecimbuton1.config(text="Matrix topluluğu davet bağlantısını kopyala",command=matrixcopy)
    islemsecimbuton2.destroy()
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def matrixcopy():
    try:
        pencere.clipboard_append("https://matrix.to/#/#betterxp-community:kde.org?via=kde.org")
        pencere.update()
        messagebox.showinfo("Bilgilendirme","Bağlantı panoya kopyalandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def yenilikler():
    def bilgi():
        messagebox.showinfo("Bilgilendirme","Bu bir örnek bilgilendirme mesajı!")
    def hata():
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.\n\nNot: Bu bir örnek hata mesajı!\nBu bir örnek olduğu için program kapatılmayacak.")
    yazi2.config(text="BetterXP 2.0 (Kararlı Sürüm) ile olan yenilikler:\nArayüzde köklü değişiklikler yapıldı:\nRenkler\nBilgi Mesajları\nHata Mesajları\nGitHub Repository düzeni değiştirildi.\nŞifre girme yeri değiştirildi ve artık BetterXP ile beraber terminal açılmıyor.\nBetterXP'ın sitesindeki 'Neler Yeni' kısmı aktif hale getirildi.\n'Bu bilgisayarı yeniden adlandır' işlevi geliştirildi.\n'BetterXP'ı Yapılandır' işlevi bazı sorunlardan dolayı kaldırıldı.\nBütün 'Terminali yapılandır' seçeneklerindeki 'Süper kullanıcı' ile 'Süper kullanıcı ile RAM kullanımı' özellikleri kaldırıldı.\n\nBetterXP 2.0.1 (Kararlı Sürüm) ile olan yenilikler:\n'BetterXP'ı yeniden aç' butonu eklendi.\n\nBetterXP 2.0.2 (Kararlı Sürüm) ile olan yenilikler:\nUfak iyileştirmeler yapıldı.\nKarşılama ekranı geliştirildi.")
    islemsecimbuton1.config(text="BetterXP'ın yeni bilgi mesajını göster",command=bilgi)
    islemsecimbuton2.config(text="BetterXP'ın yeni hata mesajını göster",command=hata)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def bxpup():
    os.system("sudo apt install git -y")
    os.system("cd /usr/local/bin/BetterXP ; sudo git clone https://github.com/MuKonqi/BetterXP.git")
    os.system("sudo rm /usr/local/bin/BetterXP/betterxp-update.py")
    os.system("sudo cp /usr/local/bin/BetterXP/BetterXP/BetterXP/betterxp-update.py /usr/local/bin/BetterXP")
    os.system("sudo python3 /usr/local/bin/BetterXP/betterxp-update.py")
    messagebox.showinfo("Bilgilendirme","BetterXP başarıyla güncellendi.\n'OK' tuşuna bastığınız an BetterXP kapatılacak.") 
    programkapat()
def lisans():
    yazi2.config(text="\nCopyright (C) 2021, Muhammed Abdurrahman\n\nBetterXP is free software: you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\n\nBetterXP is distributed in the hope that it will be useful\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License\nalong with BetterXP.  If not, see <https://www.gnu.org/licenses/>.\n")
    islemsecimbuton1.config(text="Lisansın tamamının olduğu bağlantıyı kopyala",command=lisanscopy)
    islemsecimbuton2.destroy()
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def lisanscopy():
    try:
        pencere.clipboard_append("https://www.gnu.org/licenses/gpl-3.0.txt")
        pencere.update()
        messagebox.showinfo("Bilgilendirme","Bağlantı panoya kopyalandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def bxpwebsite():
    yazi2.config(text="BetterXP'ın internet sitesi: https://betterxp.ml")
    islemsecimbuton1.config(text="BetterXP'ın internet sitesinin bağlantısını kopyala",command=bxpwebsitecopy)
    islemsecimbuton2.destroy()
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def bxpwebsitecopy():
    try:
        pencere.clipboard_append("https://betterxp.ml")
        pencere.update()
        messagebox.showinfo("Bilgilendirme","Bağlantı panoya kopyalandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def yazilimayar():
    yazi2.config(text="Lütfen aşağıdan bir seçenek seçiniz.")
    islemsecimbuton1.config(text="Terminali yapılandır",command=konsolayar)
    islemsecimbuton2.config(text="GRUB önyükleyiciyi yapılandır",command=grubc)
    islemsecimbuton3.config(text="Cups yazıcı yöneticisini yapılandır",command=cupsayar)
    islemsecimbuton4.config(text="Plank'ı yapılandır",command=plankayar)
    islemsecimbuton5.config(text="Wine'ı yapılandır",command=wineayar)
    islemsecimbuton6.config(text="Bu bilgisayarı yeniden adlandır",command=pcrename)
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def pcrename():
    try:
        islemsecimbuton1.destroy()
        islemsecimbuton2.destroy()
        islemsecimbuton3.destroy()
        islemsecimbuton4.destroy()
        islemsecimbuton5.destroy()
        islemsecimbuton6.destroy()
        islemsecimbuton7.destroy()
        islemsecimbuton8.destroy()
        islemsecimbuton9.destroy()
        islemsecimbuton10.destroy()
        islemsecimbuton11.destroy()
        islemsecimbuton12.destroy()
        buton1.destroy()
        buton2.destroy()
        b_metin1.destroy()
        def addpcname():
            get_new_pc_name=new_pc_name.get()
            add_new_pc_name=open('/etc/hostname', "w")
            add_new_pc_name.write(get_new_pc_name)
            add_new_pc_name.close()
            messagebox.showinfo("Bilgilendirme","Bilgisayarınızın yeni adını uygulamak için 'OK' tuşuna bastığınızda bilgisayarınız yeniden başlatılacak.")
            reboot()
        yazi2.config(text="Aşağıya bilgisayarınız için yeni bir ad giriniz.")
        new_pc_name=Entry(pencere)
        new_pc_name.pack()
        b_1_pcrename=Button(pencere,  cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Kaydet",command=addpcname)
        b_1_pcrename.pack()
        b_metin2=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n")
        buton_1=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="BetterXP'ı kapat", command=programkapat)
        buton_2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="BetterXP'ı yeniden aç", command=bxpreopen)
        b_metin2.pack()
        buton_1.pack()
        buton_2.pack()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def plankayar():
    try:
        messagebox.showwarning("Bu işlem için daha önceden Plank'ı kurmuş olmanız gerekmektedir.")
        os.system("plank --preferences")
        messagebox.showinfo("Bilgilendirme","Plank için yaptığınız yapılandırma işlemi bitmiştir.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def wineayar():
    try:
        messagebox.showwarning("Bu işlem için daha önceden Wine'ı kurmuş olmanız gerekmektedir.")
        os.system("sudo winecfg")
        messagebox.showinfo("Bilgilendirme","Wine için yaptığınız yapılandırma işlemi bitirilmiştir.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def grubc():
    try:
        print("\nGrub Customizer kuruluyor...")
        os.system("sudo apt install grub-customizer -y")
        print("\nGrub Customizer açılıyor...")
        os.system("sudo grub-customizer")
        messagebox.showinfo("Bilgilendirme","GRUB önyükleyiciyi için yaptığınız yapılandırma işlemi bitmiştir.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def cupsayar():
    try:
        os.system("x-www-browser localhost:631")
        messagebox.showinfo("Bilgilendirme","Cups yazıcı yöneticisi için yaptığınız yapılandırma için işlemi bitirilmiştir.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def konsolayar():
    yazi2.config(text="Lütfen aşağıdan bir seçenek seçiniz.\nNot: İşlemler yandaki kullanıcı adına göre yapılacaktır: "+ whoami)
    islemsecimbuton1.config(text="Arch Linux",command=archkonsol)
    islemsecimbuton2.config(text="Kali Linux",command=kalikonsol)
    islemsecimbuton3.config(text="Debian GNU/Linux",command=debiankonsol)
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def archkonsol():
    yazi2.config(text="Lütfen aşağıdan bir seçenek seçiniz.")
    islemsecimbuton1.config(text="Orijinal",command=archbash1)
    islemsecimbuton2.config(text="RAM Kullanımı",command=archbash2)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def archbash1():
    try:
        os.system("sudo apt install neofetch -y")
        os.system(cdmydir+bashdel)
        os.system("cd /usr/local/bin/BetterXP/ArchTerminal/Orijinal && "+bashcp)
        messagebox.showinfo("Bilgilendirme","İstediğiniz terminal yapılandırma teması uygulandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def archbash2():
    try:
        os.system("sudo apt install neofetch -y")
        os.system(cdmydir+bashdel)
        os.system("cd /usr/local/bin/BetterXP/ArchTerminal/Ram_Durumu && "+bashcp)
        messagebox.showinfo("Bilgilendirme","İstediğiniz terminal yapılandırma teması uygulandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def debiankonsol():
    yazi2.config(text="Lütfen aşağıdan bir seçenek seçiniz.")
    islemsecimbuton1.config(text="Orijinal",command=debianbash1)
    islemsecimbuton2.config(text="RAM Kullanımı",command=debianbash2)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def debianbash1():
    try:
        os.system("sudo apt install neofetch -y")
        os.system(cdmydir+bashdel)
        os.system("cd /usr/local/bin/BetterXP/DebianTerminal/Orijinal && "+bashcp)
        messagebox.showinfo("Bilgilendirme","İstediğiniz terminal yapılandırma teması uygulandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def debianbash2():
    try:
        os.system("sudo apt install neofetch -y")
        os.system(cdmydir+bashdel)
        os.system("cd /usr/local/bin/BetterXP/DebianTerminal/Ram_Durumu && "+bashcp)
        messagebox.showinfo("Bilgilendirme","İstediğiniz terminal yapılandırma teması uygulandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def kalikonsol():
    yazi2.config(text="Lütfen aşağıdan bir seçenek seçiniz.")
    islemsecimbuton1.config(text="Orijinal",command=archbash1)
    islemsecimbuton2.config(text="RAM Kullanımı",command=kalibash2)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
    islemsecimbuton12.destroy()
def kalibash1():
    try:
        os.system("sudo apt install neofetch -y")
        os.system(cdmydir+bashdel)
        os.system("cd /usr/local/bin/BetterXP/KaliTerminal/Orijinal && "+bashcp)
        messagebox.showinfo("Bilgilendirme","İstediğiniz terminal yapılandırma teması uygulandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def kalibash2():
    try:
        os.system("sudo apt install neofetch -y")
        os.system(cdmydir+bashdel)
        os.system("cd /usr/local/bin/BetterXP/KaliTerminal/Ram_Durumu && "+bashcp)
        messagebox.showinfo("Bilgilendirme","İstediğiniz terminal yapılandırma teması uygulandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def temizle():
    try:
        os.system("sudo apt clean -y")
        os.system("sudo apt autoremove -y")
        messagebox.showinfo("Bilgilendirme","Kullanılmayan eski paketler kaldırılmıştır.")
        programkapat()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def islemsecim():
    yazi2.config(text="Lütfen yapmak istediğiniz işlemi aşağıdaki listeden seçiniz.")
    global islemsecimbuton1
    global islemsecimbuton2
    global islemsecimbuton3
    global islemsecimbuton4
    global islemsecimbuton5
    global islemsecimbuton6
    global islemsecimbuton7
    global islemsecimbuton8
    global islemsecimbuton9
    global islemsecimbuton10
    global islemsecimbuton11
    global islemsecimbuton12
    global islemsecimbuton13
    global buton1
    global buton2
    islemsecimbuton1=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton1.config(text="Program kur",command=programkurucu)
    islemsecimbuton1.pack()
    islemsecimbuton2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton2.config(text="Program kaldır",command=programsil)
    islemsecimbuton2.pack()
    islemsecimbuton3=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton3.config(text="Masaüstü ortamı/pencere yöneticisi kur",command=dewmkurucu)
    islemsecimbuton3.pack()
    islemsecimbuton4=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton4.config(text="Masaüstü ortamı/pencere yöneticisi kaldır",command=dewmsilici)
    islemsecimbuton4.pack()
    islemsecimbuton5=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton5.config(text="Hata çözücü",command=hatacoz)
    islemsecimbuton5.pack()
    islemsecimbuton6=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton6.config(text="Sistem güncelleyici",command=systemup)
    islemsecimbuton6.pack()
    islemsecimbuton7=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton7.config(text="Yapılandırma",command=yazilimayar)
    islemsecimbuton7.pack()
    islemsecimbuton8=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton8.config(text="Paket yöneticisi/araç kurucusu",command=pakettoolmgr)
    islemsecimbuton8.pack()
    islemsecimbuton9=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton9.config(text="Dosya yöneticilerini süper kullanıcı haklarıyla açma",command=rootuyg)
    islemsecimbuton9.pack()
    islemsecimbuton10=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton10.config(text="Bazı GNU/Linux dağıtımları hakkında",command=gnulinuxhk)
    islemsecimbuton10.pack()
    islemsecimbuton11=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton11.config(text="Eski paket temizleyicisi",command=temizle)
    islemsecimbuton11.pack()
    islemsecimbuton12=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton12.config(text="BetterXP hakkında",command=info)
    islemsecimbuton12.pack()
    b_metin1.config(text="\n")
    b_metin1.pack()
    buton1=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    buton1.config(text="BetterXP'ı kapat",command=programkapat)
    buton1.pack()
    buton2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    buton2.config(text="BetterXP'ı yeniden aç",command=bxpreopen)
    buton2.pack()

myusername=open('/usr/local/bin/BetterXP/whoami.txt')
whoami=myusername.read()
myusername.close()
mydir="/home/"+whoami
bash=".bashrc"
cdmydir="cd /home/"+whoami
mybash=mydir+bash
rm="rm -rf "
bashdel=rm+bash
bashcp="cp .bashrc "+mydir

if os.path.isfile("/usr/local/bin/BetterXP/first_start_succesful"):
    pencere=Tk()
    pencere.title("BetterXP")
    pencere.config(background="#000000")
    pencere.resizable(0, 0) 

    menu1=Menu(pencere)
    pencere.config(menu=menu1)
    dosya=Menu(menu1, tearoff=0)
    menu1.add_cascade(label="Dosya",menu=dosya)
    dosya.add_command(label="Çıkış", command=programkapat)
    dosya.add_command(label="Yeniden aç", command=bxpreopen)

    metin1=Label(pencere, background="#000000", foreground="#FFFFFF", font="junkyard 12 bold")
    metin1.config(text="Merhabalar!\nSon kullanıcı için tasarlanan BetterXP'ı tercih ettiğiniz için teşekkürler.\nBaşınıza gelebilecek herhangi bir durumda sorumluluk almayacağımızı belirtiriz.\nİyi günler dileriz.")
    metin1.pack()

    yazi2=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 10")
    yazi2.pack()

    b_metin1=Label(pencere, background="#000000", foreground="#FFFFFF")

    islemsecim()
else:
    def exitfirststart():
        os.system("cd /usr/local/bin/BetterXP ; sudo touch first_start_succesful")
        pencere.title("BetterXP")
        metin2.destroy()
        w_buton.destroy()
        menu1=Menu(pencere)
        pencere.config(menu=menu1)
        dosya=Menu(menu1, tearoff=0)
        menu1.add_cascade(label="Dosya",menu=dosya)
        dosya.add_command(label="Çıkış", command=programkapat)
        dosya.add_command(label="Yeniden aç", command=bxpreopen)
        metin1.config(text="Merhabalar!\nSon kullanıcı için tasarlanan BetterXP'ı tercih ettiğiniz için teşekkürler.\nBaşınıza gelebilecek herhangi bir durumda sorumluluk almayacağımızı belirtiriz.\nİyi günler dileriz.")
        islemsecim()

    pencere=Tk()
    pencere.title("BetterXP'a Hoş Geldiniz")
    pencere.config(background="#000000")
    pencere.resizable(0, 0) 

    b_metin1=Label(pencere, background="#000000", foreground="#FFFFFF")

    metin1=Label(pencere, background="#000000", foreground="#FFFFFF", font="junkyard 12 bold")
    metin1.config(text="Merhabalar!\nSon kullanıcı için tasarlanan BetterXP'ı tercih ettiğiniz için teşekkürler.\nBaşınıza gelebilecek herhangi bir durumda sorumluluk almayacağımızı belirtiriz.\nİyi günler dileriz.")
    metin1.pack()

    metin2=Label(pencere, background="#000000", foreground="#FF0000", font="arial 11 bold")
    metin2.config(text="Görünüşe göre BetterXP'ı ilk defa çalıştırıyorsunuz.\nO zaman size BetterXP'ın sahip olduğu özelliklerin bazılarını anlatalım.\nİşte BetterXP'ın sahip olduğu özelliklerin bazıları:\nÖzgür ve açık kaynaklı\nProgram kurma/kaldırma özelliği\nMasaüstü ortamı kurma/kaldırma özelliği\nSistemi güncelleme özelliği\nÇeşitli yapılandırma özellikleri (GRUB, Terminal, Plank, Wine...)\nPaket yöneticisi kurma özelliği")
    metin2.pack()

    w_buton=Button(pencere, cursor="hand2", activebackground="#00FFFF", activeforeground="#000000", foreground="#000000", background="#FFFFFF", borderwidth="5")
    w_buton.config(font="arial 10 bold", text="Hadi, BetterXP'ı kullanmaya başlayalım!",command=exitfirststart)
    w_buton.pack()

    yazi2=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 10")
    yazi2.pack()

mainloop()
