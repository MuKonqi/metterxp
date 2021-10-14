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
def dekurucu():
    yazi2.config(text="Lütfen kurmak istediğiniz masaüstü ortamını seçiniz.")
    islemsecimbuton1.config(text="KDE Plasma DE'i kur",command=kdekur)
    islemsecimbuton2.config(text="GNOME DE'i kur",command=gnomekur)
    islemsecimbuton3.config(text="Xfce DE'i kur",command=xfcekur)
    islemsecimbuton4.config(text="Cinnamon DE'i kur",command=cinnamonkur)
    islemsecimbuton5.config(text="Pantheon DE'i kur",command=pantheonkur)    
    islemsecimbuton6.config(text="Mate DE'i kur",command=matekur)
    islemsecimbuton7.config(text="Deepin DE'i kur",command=ddekur)
    islemsecimbuton8.config(text="LXDE'i kur",command=lxdekur)
    islemsecimbuton9.config(text="LXQt DE'i kur",command=lxqtkur)
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
def gnomekur():
    try:
        print("\nGNOME DE kurulumu başlatılıyor...")
        os.system("sudo dnf install @gnome-desktop")
        messagebox.showinfo("Bilgilendirme","GNOME DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def kdekur():
    try:
        print("\nKDE Plasma DE kurulumu başlatılıyor...")
        os.system("sudo dnf install @kde-desktop")
        messagebox.showinfo("Bilgilendirme","KDE Plasma DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def cinnamonkur():
    try:
        print("\nCinnamon DE kurulumu başlatılıyor...")
        os.system("sudo dnf install @cinnamon-desktop")
        messagebox.showinfo("Bilgilendirme","Cinnamon DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def xfcekur():
    try:
        print("\nXfce DE kurulumu başlatılıyor...")
        os.system("sudo dnf install @xfce-desktop")
        messagebox.showinfo("Bilgilendirme","Xfce DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def matekur():
    try:
        print("\nMate DE kurulumu başlatılıyor...")
        os.system("sudo dnf install @mate-desktop")
        messagebox.showinfo("Bilgilendirme","Mate DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def ddekur():
    try:
        print("\nDeepin DE kurulumu başlatılıyor...")
        os.system("sudo dnf install @deepin-desktop")
        messagebox.showinfo("Bilgilendirme","Deepin DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def pantheonkur():
    try:
        print("\nPantheon DE kurulumu başlatılıyor...")
        os.system("sudo dnf install @pantheon-desktop")
        messagebox.showinfo("Bilgilendirme","Pantheon DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def lxdekur():
    try:
        print("\nLXDE kurulumu başlatılıyor...")
        os.system("sudo dnf install @lxde-desktop")
        messagebox.showinfo("Bilgilendirme","LXDE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def lxqtkur():
    try:
        print("\nLXQt DE kurulumu başlatılıyor...")
        os.system("sudo dnf install @lxqt-desktop")
        messagebox.showinfo("Bilgilendirme","LXQt DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def desilici():
    yazi2.config(text="Lütfen kaldırmak istediğiniz masaüstü ortamını seçiniz.")
    islemsecimbuton1.config(text="KDE Plasma DE'i kaldır",command=kdesil)
    islemsecimbuton2.config(text="GNOME DE'i kaldır",command=gnomesil)
    islemsecimbuton3.config(text="Xfce DE'i kaldır",command=xfcesil)
    islemsecimbuton4.config(text="Cinnamon DE'i kaldır",command=cinnamonsil)
    islemsecimbuton5.config(text="Pantheon DE'i kaldır",command=pantheonsil)    
    islemsecimbuton6.config(text="Mate DE'i kaldır",command=matesil)
    islemsecimbuton7.config(text="Deepin DE'i kaldır",command=ddesil)
    islemsecimbuton8.config(text="LXDE'i kaldır",command=lxdesil)
    islemsecimbuton9.config(text="LXQt DE'i kaldır",command=lxqtsil)
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
def gnomesil():
    try:
        print("\nGNOME DE kaldırılıyor...")
        os.system("sudo dnf remove @gnome-desktop")
        messagebox.showinfo("Bilgilendirme","GNOME DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def kdesil():
    try:
        print("\nKDE Plasma DE kaldırılıyor...")
        os.system("sudo dnf remove @kde-desktop")
        messagebox.showinfo("Bilgilendirme","KDE Plasma DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def cinnamonsil():
    try:
        print("\nCinnamon DE kaldırılıyor...")
        os.system("sudo dnf remove @cinnamon-desktop")
        messagebox.showinfo("Bilgilendirme","Cinnamon DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def xfcesil():
    try:
        print("\nXfce DE kaldırılıyor...")
        os.system("sudo dnf install @xfce-desktop")
        messagebox.showinfo("Bilgilendirme","Xfce DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def matesil():
    try:
        print("\nMate DE kaldırılıyor...")
        os.system("sudo dnf remove @mate-desktop")
        messagebox.showinfo("Bilgilendirme","Mate DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def ddesil():
    try:
        print("\nDeepin DE kaldırılıyor...")
        os.system("sudo dnf install @deepin-desktop")
        messagebox.showinfo("Bilgilendirme","Deepin DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def pantheonsil():
    try:
        print("\nPantheon DE kaldırılıyor...")
        os.system("sudo dnf remove @pantheon-desktop")
        messagebox.showinfo("Bilgilendirme","Pantheon DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def lxdesil():
    try:
        print("\nLXDE kaldırılıyor...")
        os.system("sudo dnf remove @lxde-desktop")
        messagebox.showinfo("Bilgilendirme","LXDE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def lxqtsil():
    try:
        print("\nLXQt DE kaldırılıyor...")
        os.system("sudo dnf remove @lxqt-desktop")
        messagebox.showinfo("Bilgilendirme","LXQt DE kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def programkurucu():          
    yazi2.config(text="Hangi programı kurmak istiyorsunuz?")
    islemsecimbuton1.config(text="Firefox'u kur",command=firefoxkur)
    islemsecimbuton2.config(text="Chromium'u kur",command=chromiumkur)
    islemsecimbuton3.config(text="Plank'ı kur",command=plankkur)
    islemsecimbuton4.config(text="GParted'i kur",command=gpartedkur)
    islemsecimbuton5.config(text="GIMP'i kur",command=gimpkur)
    islemsecimbuton6.config(text="Cups'ı kur",command=cupskur)
    islemsecimbuton7.config(text="Terminator'u kur",command=terminatorkur)
    islemsecimbuton8.config(text="Code::Blocks'u kur",command=codeblockskur)
    islemsecimbuton9.config(text="PlayOnLinux'u kur",command=playonlinuxkur)
    islemsecimbuton10.config(text="Wine'ı kur",command=winekur)
    islemsecimbuton11.destroy()
def firefoxkur():
    try:
        print("\nMozilla Firefox kurulumu başlatılıyor...")
        os.system("sudo dnf install firefox -y")
        messagebox.showinfo("Bilgilendirme","Mozilla Firefox internet tarayıcısı başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def chromiumkur():
    try:
        print("\nChromium kurulumu başlatılıyor...")
        os.system("sudo dnf install chromium -y")
        messagebox.showinfo("Bilgilendirme","Chromium internet tarayıcısı başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def plankkur():
    try:
        print("\nPlank kurulumu başlatılıyor...")
        os.system("sudo dnf install plank -y")
        messagebox.showinfo("Bilgilendirme","Plank başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def gpartedkur():
    try:
        print("\nGParted kurulumu başlatılıyor...")
        os.system("sudo dnf install gparted -y")
        messagebox.showinfo("Bilgilendirme","GParted disk bölümü düzenleyicisi başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def gimpkur():
    try:
        print("\nGIMP kurulumu başlatılıyor...")
        os.system("sudo dnf install gimp -y")
        messagebox.showinfo("Bilgilendirme","GIMP görüntü işleme programı başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def cupskur():
    try:
        print("\nCups kurulumu başlatılıyor...")
        os.system("sudo dnf install cups -y")
        messagebox.showinfo("Bilgilendirme","Cups yazıcı yöneticisi başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def terminatorkur():
    try:
        print("\nTerminator kurulumu başlatılıyor...")
        os.system("sudo dnf install terminator -y")
        messagebox.showinfo("Bilgilendirme","Terminator uçbirim emulatörü başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def codeblockskur():
    try:
        print("\nCode::Blocks kurulumu başlatılıyor...")
        os.system("sudo dnf install codeblocks -y")
        messagebox.showinfo("Bilgilendirme","Code::Blocks başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def playonlinuxkur():
    try:
        print("\nPlayOnLinux kurulumu başlatılıyor...")
        os.system("sudo dnf install playonlinux -y")
        messagebox.showinfo("Bilgilendirme","PlayOnLinux başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def winekur():
    try:
        print("\nWine kurulumu başlatılıyor...")
        os.system("sudo dnf install wine -y")
        messagebox.showinfo("Bilgilendirme","Wine başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def programsil():         
    yazi2.config(text="Hangi programı kaldırmak istiyorsunuz?")
    islemsecimbuton1.config(text="Firefox'u kaldır",command=firefoxsil)
    islemsecimbuton2.config(text="Chromium'u kaldır",command=chromiumsil)
    islemsecimbuton3.config(text="Plank'ı kaldır",command=planksil)
    islemsecimbuton4.config(text="GParted'i kaldır",command=gpartedsil)
    islemsecimbuton5.config(text="GIMP'i kaldır",command=gimpsil)
    islemsecimbuton6.config(text="Cups'ı kaldır",command=cupssil)
    islemsecimbuton7.config(text="Terminator'u kaldır",command=terminatorsil)
    islemsecimbuton8.config(text="Code::Blocks'u kaldır",command=codeblockssil)
    islemsecimbuton9.config(text="PlayOnLinux'u kaldır",command=playonlinuxsil)
    islemsecimbuton10.config(text="Wine'ı kaldır",command=winesil)
    islemsecimbuton11.destroy()
def firefoxsil():
    try:
        print("\nMozilla Firefox kaldırılıyor...")
        os.system("sudo dnf remove firefox -y")
        messagebox.showinfo("Bilgilendirme","Mozilla Firefox internet tarayıcısı başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()    
def chromiumsil():
    try:
        print("\nChromium kaldırılıyor...")
        os.system("sudo dnf remove chromium -y")
        messagebox.showinfo("Bilgilendirme","Chromium internet tarayıcısı başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def planksil():
    try:
        print("\nPlank kaldırılıyor...")
        os.system("sudo dnf remove plank -y")
        messagebox.showinfo("Bilgilendirme","Plank başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat() 
def gpartedsil():
    try:
        print("\nGParted kaldırılıyor...")
        os.system("sudo dnf remove gparted -y")
        messagebox.showinfo("Bilgilendirme","GParted disk bölümü düzenleyicisi başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat() 
def gimpsil():
    try:
        print("\nGIMP kaldırılıyor...")
        os.system("sudo dnf remove gimp -y")
        messagebox.showinfo("Bilgilendirme","GIMP başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat() 
def cupssil():
    try:
        print("\nCups kaldırılıyor...")
        os.system("sudo dnf remove cups -y")
        messagebox.showinfo("Bilgilendirme","Cups yazıcı yöneticisi başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat() 
def terminatorsil():
    try:
        print("\nTerminator kaldırılıyor...")
        os.system("sudo dnf remove terminator -y")
        messagebox.showinfo("Bilgilendirme","Terminator uçbirim emulatörü başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat() 
def codeblockssil():
    try:
        print("\nCode::Blocks kaldırılıyor...")
        os.system("sudo dnf remove codeblocks -y")
        messagebox.showinfo("Bilgilendirme","Code::Blocks başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat() 
def playonlinuxsil():
    try:
        print("\nPlanOnLinux kaldırılıyor...")
        os.system("sudo dnf remove playonlinux -y")
        messagebox.showinfo("Bilgilendirme","PlanOnLinux başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat() 
def winesil():
    try:
        print("\nWine kaldırılıyor...")
        os.system("sudo dnf remove wine -y")
        messagebox.showinfo("Bilgilendirme","Wine başarıyla kaldırıldı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat() 
def systemup():
    try:
        print("\nSistem güncellemesi işlemi başlatılıyor...")
        os.system("sudo dnf update -y")
        messagebox.showinfo("Bilgilendirme","Sistem güncellemesi işlemi bitmiştir.")
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
        os.system("sudo dnf install pcmanfm")
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
        os.system("sudo dnf install thunar")
        print("\nThunar açılıyor...")
        os.system("sudo thunnar")
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
        os.system("sudo dnf install nautilus")
        print("\nNautilus açılıyor...")
        os.system("sudo nautilus")
        messagebox.showinfo("Bilgilendirme","İşlem tamamlandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()  
def paketmgr():
    yazi2.config(text="Hangi paket yöneticisini kurmak istersiniz?")
    islemsecimbuton1.config(text="Snap paket yöneticisini kur",command=snapkur)
    islemsecimbuton2.config(text="Flatpak paket yöneticisini kur",command=flatpakkur)
    islemsecimbuton3.destroy()
    islemsecimbuton4.destroy()
    islemsecimbuton5.destroy()
    islemsecimbuton6.destroy()
    islemsecimbuton7.destroy()
    islemsecimbuton8.destroy()
    islemsecimbuton9.destroy()
    islemsecimbuton10.destroy()
    islemsecimbuton11.destroy()
def flatpakkur():
    try:
        print("\nFlatpak kuruluyor...")
        os.system("sudo dnf install flatpak -y")
        os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
        messagebox.showinfo("Bilgilendirme","Flatpak paket yöneticisi başarıyla kuruldu.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
        reboot()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def snapkur():
    try:
        print("\nSnap kuruluyor...")
        os.system("sudo dnf install snapd -y")
        messagebox.showinfo("Bilgilendirme","Snap paket yöneticisi başarıyla kuruldu.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()       
def info():
    yazi2.config(text="BetterXP, son kullanıcı için tasarlanmış, özgür bir yazılım ürünüdür.\nBetterXP, GNU General Public License, Version 3.0 (GPL 3) altında lisanslanmıştır.\nYapımcı: MuKonqi (Muhammed Abdurrahman)\nTemel: Terminalden kurtulun 2.0 (Kararlı Sürüm)\nSürüm: 2.0 (Kararlı Sürüm)")
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
    yazi2.config(text="\nİlk önce BetterXP'ı tercih ettiğiniz için size teşekkür ederiz.\n\n\nBetterXP 2.0 (Kararlı Sürüm) ile olan yenilikler:\nArayüzde köklü değişiklikler yapıldı:\nRenkler\nBilgi Mesajları\nHata Mesajları\nGitHub Repository düzeni değiştirildi.\nŞifre girme yeri değiştirildi ve artık BetterXP ile beraber terminal açılmıyor.\nBetterXP'ın sitesindeki 'Neler Yeni' kısmı aktif hale getirildi.\n'Bu bilgisayarı yeniden adlandır' işlevi geliştirildi.\n'BetterXP'ı Yapılandır' işlevi bazı sorunlardan dolayı kaldırıldı.\nBütün 'Terminali yapılandır' seçeneklerindeki 'Süper kullanıcı' ile 'Süper kullanıcı ile RAM kullanımı' özellikleri kaldırıldı.\n")
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
def bxpup():
    os.system("sudo dnf install git -y")
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
        buton.destroy()
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
        b_1_pcrename=Button(pencere,  cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Kaydet",command=addpcname)
        b_1_pcrename.pack()
        b_metin2=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n")
        buton1=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="BetterXP'ı kapat", command=programkapat)
        b_metin2.pack()
        buton1.pack()
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
        os.system("sudo dnf install grub-customizer -y")
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
def archbash1():
    try:
        os.system("sudo dnf install neofetch -y")
        os.system(cdmydir+bashdel)
        os.system("cd /usr/local/bin/BetterXP/ArchTerminal/Orijinal && "+bashcp)
        messagebox.showinfo("Bilgilendirme","İstediğiniz terminal yapılandırma teması uygulandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def archbash2():
    try:
        os.system("sudo dnf install neofetch -y")
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
def debianbash1():
    try:
        os.system("sudo dnf install neofetch -y")
        os.system(cdmydir+bashdel)
        os.system("cd /usr/local/bin/BetterXP/DebianTerminal/Orijinal && "+bashcp)
        messagebox.showinfo("Bilgilendirme","İstediğiniz terminal yapılandırma teması uygulandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def debianbash2():
    try:
        os.system("sudo dnf install neofetch -y")
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
def kalibash1():
    try:
        os.system("sudo dnf install neofetch -y")
        os.system(cdmydir+bashdel)
        os.system("cd /usr/local/bin/BetterXP/KaliTerminal/Orijinal && "+bashcp)
        messagebox.showinfo("Bilgilendirme","İstediğiniz terminal yapılandırma teması uygulandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def kalibash2():
    try:
        os.system("sudo dnf install neofetch -y")
        os.system(cdmydir+bashdel)
        os.system("cd /usr/local/bin/BetterXP/KaliTerminal/Ram_Durumu && "+bashcp)
        messagebox.showinfo("Bilgilendirme","İstediğiniz terminal yapılandırma teması uygulandı.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def temizle():
    try:
        os.system("sudo dnf autoremove")
        messagebox.showinfo("Bilgilendirme","Kullanılmayan eski paketler kaldırılmıştır.")
        programkapat()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için program kapatılacak.")
        programkapat()
def islemsecim():
    metin2.destroy() 
    devam_buton.destroy()
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
    global buton
    islemsecimbuton1=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton1.config(text="Program kur",command=programkurucu)
    islemsecimbuton1.pack()
    islemsecimbuton2=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton2.config(text="Program kaldır",command=programsil)
    islemsecimbuton2.pack()
    islemsecimbuton3=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton3.config(text="Masaüstü ortamı kur",command=dekurucu)
    islemsecimbuton3.pack()
    islemsecimbuton4=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton4.config(text="Masaüstü ortamı kaldır",command=desilici)
    islemsecimbuton4.pack()
    islemsecimbuton5=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton5.config(text="Sistem güncelleyici",command=systemup)
    islemsecimbuton5.pack()
    islemsecimbuton6=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton6.config(text="Yapılandırma",command=yazilimayar)
    islemsecimbuton6.pack()
    islemsecimbuton7=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton7.config(text="Paket yöneticisi kurucusu",command=paketmgr)
    islemsecimbuton7.pack()
    islemsecimbuton8=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton8.config(text="Dosya yöneticilerini süper kullanıcı haklarıyla açma",command=rootuyg)
    islemsecimbuton8.pack()
    islemsecimbuton9=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton9.config(text="Bazı GNU/Linux dağıtımları hakkında",command=gnulinuxhk)
    islemsecimbuton9.pack()
    islemsecimbuton10=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton10.config(text="Eski paket temizleyecisi",command=temizle)
    islemsecimbuton10.pack()
    islemsecimbuton11=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    islemsecimbuton11.config(text="BetterXP hakkında",command=info)
    islemsecimbuton11.pack()
    b_metin1.config(text="\n")
    b_metin1.pack()
    buton=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3")
    buton.config(text="BetterXP'ı kapat",command=programkapat)
    buton.pack()

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

pencere=Tk()
pencere.title("BetterXP")
pencere.config(background="#000000")
pencere.resizable(0, 0)

menu1=Menu(pencere)
pencere.config(menu=menu1)
dosya=Menu(menu1, tearoff=0)
menu1.add_cascade(label="Dosya",menu=dosya)
dosya.add_command(label="Çıkış", command=programkapat)

metin1=Label(pencere, background="#000000", foreground="#FFFFFF", font="junkyard 12 bold")
metin1.config(text="Merhabalar!\nBetterXP'ı tercih ettiğiniz için teşekkürler.\nBaşınıza gelebilecek herhangi bir durumda sorumluluk almayacağımızı belirtiriz.\nİyi günler dileriz.")
metin1.pack()

metin2=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 11 bold")
metin2.config(text="Son kullanıcıya daha iyi bir deneyim sağlamak için tasarlanan BetterXP'a hoş geldiniz!\nLütfen programı kullanmak için devam ediniz.")
metin2.pack()

devam_buton=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="5")
devam_buton.config(font="arial 10 bold", text="Devam et!",command=islemsecim)
devam_buton.pack()

yazi2=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 10")
yazi2.pack() 

b_metin1=Label(pencere, background="#000000", foreground="#FFFFFF")

mainloop()
