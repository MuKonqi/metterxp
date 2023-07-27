#!/usr/bin/env python3

# Copyright (C) 2021, 2022 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os


debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp/settings/lang/en.txt"


def module_exit():
    exit("\nThis module is shutting down...\nModül kapatılıyor...")
def reopen():
    print("\nRestarting this module...\nModül yeniden başlatılıyor...")
    window.destroy()
    os.system("pkexec /usr/bin/metterxp de_wm_it_rm")
def reboot():
    print("Bilgisayarınız yeniden başlatılıyor...\nRestarting your PC...")
    os.system("reboot now")

if not os.getuid() == 0:
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Only root can run this module!")
        exit("Only root can run this module!\nThis module is shutting down...")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit("\nSadece kök kullanıcı bu modülü çalıştırabilir!\nModül kapatılıyor...")
    

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


window=Tk()
if os.path.isfile(lang_en):
    window.title("Instal/reinstall/uninstall desktop environment/window manager | MetterXP")
elif os.path.isfile(lang_tr):
    window.title("Masaüstü ortamı/pencere yöneticisi kur/yeniden kur/kaldır | MetterXP")
window.config(background=bg)
window.resizable(0, 0)


if os.path.isfile(debian) or os.path.isfile(fedora):
    def kde():
        button_1.destroy()
        def install():
            if os.path.isfile(debian):
                os.system(" apt install kde-plasma-desktop -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @kde-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","KDE Plasma DE installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall kde-plasma-desktop -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @kde-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","KDE Plasma DE reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge kde-plasma-desktop* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove @kde-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","KDE Plasma DE uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for KDE Plasma DE?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="KDE Plasma DE için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    def gnome():
        button_1.destroy()
        def install():
            if os.path.isfile(debian):
                os.system(" apt install gnome gnome-shell -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @gnome-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","GNOME DE installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GNOME DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall gnome gnome-shell -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @gnome-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","GNOME DE reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GNOME DE yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge gnome* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove @gnome-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","GNOME DE uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GNOME DE kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for GNOME DE?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="GNOME DE için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    def cinnamon():
        button_1.destroy()
        def install():
            if os.path.isfile(debian):
                os.system(" apt install cinnamon -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @cinnamon-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Cinnamon DE installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Cinnamon DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall cinnamon -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @cinnamon-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Cinnamon DE reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Cinnamon DE yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge cinnamon* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove @cinnamon-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Cinnamon DE uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Cinnamon DE kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Cinnamon DE?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="Cinnamon DE için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    def mate():
        button_1.destroy()
        def install():
            if os.path.isfile(debian):
                os.system(" apt install mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @mate-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Mate DE installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Mate DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @mate-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Mate DE reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Mate DE yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge mate-plasma-desktop* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove @mate-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Mate DE uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Mate DE kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Mate DE?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="Mate DE için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    def xfce():
        button_1.destroy()
        def install():
            if os.path.isfile(debian):
                os.system(" apt install xfce4 -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @xfce-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Xfce DE installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Xfce DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall xfce4 -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @xfce4-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Xfce DE reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Xfce DE yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge xfce4* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove @xfce-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Xfce DE uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Xfce DE kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Xfce DE?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="Xfce DE için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    def deepin():
        button_1.destroy()
        def install():
            if os.path.isfile(debian):
                os.system(" apt install software-properties-common -y")
                os.system(" add-apt-repository ppa:ubuntudde-dev/stable -y")
                os.system(" apt update -y")
                os.system(" apt install dde -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @deepin-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Deepin DE installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Deepin DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall dde -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @deepin-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Deepin DE reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Deepin DE yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge dde* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove @deepin-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Deepin DE uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Deepin DE kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Deepin DE?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="Deepin DE için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(lang_en):
            if os.path.isfile(debian):
                text2.config(text="Note: The process of installing Deepin DE is not completely stable.\n\nDE = Desktop Enviroment = Desktop Environment\nWM = Window Manager = Window Manager")
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            if os.path.isfile(debian):
                text2.config(text="Not: Deepin DE'i kurma işlemi tamamen stabil değildir.\n\nDE = Desktop Enviroment = Masaüstü Ortamı\nWM = Window Manager = Pencere Yöneticisi")
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    def lxde():
        button_1.destroy()
        def install():
            if os.path.isfile(debian):
                os.system(" apt install lxde -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @lxde-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","LXDE installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","LXDE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall lxde -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @lxde-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","LXDE reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","LXDE yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge lxde* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove @lxde-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","LXDE uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","LXDE kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for LXDE?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="LXDE için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    def lxqt():
        button_1.destroy()
        def install():
            if os.path.isfile(debian):
                os.system(" apt install openbox pcmanfm-qt lxqt-admin lxqt-common lxqt-config lxqt-globalkeys lxqt-notificationd lxqt-panel lxqt-policykit lxqt-powermanagement lxqt-qtplugin lxqt-runner lxqt-session -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install @kde-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","KDE Plasma DE installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall openbox pcmanfm-qt lxqt-admin lxqt-common lxqt-config lxqt-globalkeys lxqt-notificationd lxqt-panel lxqt-policykit lxqt-powermanagement lxqt-qtplugin lxqt-runner lxqt-session -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall @kde-desktop -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","KDE Plasma DE reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(fedora):
                def openboxuninstall():
                    os.system(" apt purge openbox* -y")
                    if os.path.isfile(lang_en):
                        messagebox.showinfo("Information","The OpenBox WM used by LXQt DE has been uninstalled.\nYour computer will reboot as soon as you click the 'OK' button to apply the changes.")
                    elif os.path.isfile(lang_tr):
                        messagebox.showinfo("Bilgilendirme","LXQt DE'in kullandığı OpenBox WM kaldırıldı.\nDeğişiklikleri uygulamak için 'OK' butonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                    reboot()
                os.system(" apt purge pcmanfm-qt lxqt-admin lxqt-common lxqt-config lxqt-globalkeys lxqt-notificationd lxqt-panel lxqt-policykit lxqt-powermanagement lxqt-qtplugin lxqt-runner lxqt-session lxqt- -y")
                if os.path.isfile(lang_en):
                    text1.config(text="Everything has been removed except the OpenBox WM that LXQt DE uses.")
                    button1.config(text="Not uninstall OpenBox WM used by LXQt DE\nRestart computer immediately", command=reboot)
                    button2.config(text="Uninstall OpenBox WM used by LXQt DE\nRestart computer when OpenBox WM is uninstalled", command=openboxuninstall)
                elif os.path.isfile(lang_tr):
                    text1.config(text="LXQt DE'in kullandığı OpenBox WM hariç her şey kaldırıldı.")
                    button1.config(text="LXQt DE'in kullandığı OpenBox WM'ı kaldırma\nHemen bilgisayarı yeniden başlat", command=reboot)
                    button2.config(text="LXQt DE'in kullandığı OpenBox WM'i kaldır\nOpenBox WM'i kaldırılınca bilgisayarı yeniden başlat", command=openboxuninstall)
                button3.destroy()
            elif os.path.isfile(fedora):
                os.system(" dnf remove @lxqt-desktop -y")
                if os.path.isfile(lang_en):
                    messagebox.showinfo("Information","LXQt DE uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
                elif os.path.isfile(lang_tr):
                    messagebox.showinfo("Bilgilendirme","LXQt kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
                reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for LXQt DE?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="LXQt DE için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    def openbox():
        button_1.destroy()
        def install():
            if os.path.isfile(debian):
                os.system(" apt install openbox -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install openbox obconf -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","OpenBox WM installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","OpenBox WM kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall openbox -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall openbox obconf -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","OpenBox WM reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","OpenBox WM yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge openbox -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove openbox obconf -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","OpenBox WM uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","OpenBox WM kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for OpenBox WM?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="OpenBox WM için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    def i3():
        button_1.destroy()
        def install():
            if os.path.isfile(debian):
                os.system(" apt install i3 -y")
            elif os.path.isfile(fedora):
                os.system(" dnf install i3 i3status i3lock dmenu -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","i3 WM installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","i3 WM kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            if os.path.isfile(debian):
                os.system(" apt reinstall i3 -y")
            elif os.path.isfile(fedora):
                os.system(" dnf reinstall i3 i3status i3lock dmenu -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","i3 WM reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","i3 WM yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            if os.path.isfile(debian):
                os.system(" apt purge i3* -y")
            elif os.path.isfile(fedora):
                os.system(" dnf remove i3 i3status i3lock dmenu -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","i3 WM uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","i3 WM kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for i3 WM?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="i3 WM için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    def pantheon():
        button_1.destroy()
        def install():
            os.system(" dnf group install 'pantheon desktop' -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Pantheon DE installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Pantheon DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            os.system(" dnf group reinstall 'pantheon desktop' -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Pantheon DE reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Pantheon DE yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            os.system(" dnf group remove 'pantheon desktop' -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Pantheon DE uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Pantheon DE kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Pantheon DE?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="Pantheon DE için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        if os.path.isfile(fedora):
            button11.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    if os.path.isfile(lang_en):
        text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Which desktop environment/window manager do you want to install or reinstall or uninstall?")
    elif os.path.isfile(lang_tr):    
        text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Hangi masaüstü ortamını/pencere yöneticisi kurmak ya da yeniden kurmak ya da kaldırmak istiyorsunuz?")
    text1.pack()
    space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    space1.pack()
    button1=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="KDE Plasma DE",command=kde)
    button1.pack()
    button2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="GNOME DE",command=gnome)
    button2.pack()
    button3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Cinnamon DE",command=cinnamon)
    button3.pack()
    button4=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Mate DE",command=mate)
    button4.pack()
    button5=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Xfce DE",command=xfce)
    button5.pack()
    button6=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Deepin DE",command=deepin)
    button6.pack()
    button7=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="LXDE",command=lxde)
    button7.pack()
    button8=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="LXQt DE",command=lxqt)
    button8.pack()
    button9=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="OpenBox WM",command=openbox)
    button9.pack()
    button10=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="i3 WM",command=i3)
    button10.pack()
    if os.path.isfile(fedora):
        button11=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Pantheon DE",command=pantheon)
        button11.pack()
    space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
    space2.pack()
    text2=Label(window, background=bg, foreground=fg, font="arial 9 bold", text="DE = Desktop Enviroment = Masaüstü Ortamı\nWM = Window Manager = Pencere Yöneticisi")
    text2.pack()
    space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    space3.pack()
    if os.path.isfile(lang_en):
        button_1=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
    elif os.path.isfile(lang_tr):
        button_1=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
    button_1.pack()
    
    
if os.path.isfile(solus):
    def kde():
        button_1.destroy()
        def install():
            os.system(" eopkg it -c desktop.kde -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","KDE Plasma DE installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            os.system(" eopkg it -c desktop.kde --rei -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","KDE Plasma DE reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            os.system(" eopkg rm -c desktop.kde --purge -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","KDE Plasma DE uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","KDE Plasma DE kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for KDE Plasma DE?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="KDE Plasma DE için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    def gnome():
        button_1.destroy()
        def install():
            os.system(" eopkg it -c desktop.gnome -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","GNOME DE installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GNOME DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            os.system(" eopkg it -c desktop.gnome --rei -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","GNOME DE reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GNOME DE yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            os.system(" eopkg rm -c desktop.gnome --purge -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","GNOME DE uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","GNOME DE kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for GNOME DE?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="GNOME DE için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    def budgie():
        button_1.destroy()
        def install():
            os.system(" eopkg it -c desktop.budgie -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Budgie DE installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Budgie DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            os.system(" eopkg it -c desktop.budgie --rei -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Budgie DE reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Budgie DE yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            os.system(" eopkg rm -c desktop.budgie --purge -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Budgie DE uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Budgie DE kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Budgie DE?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="Budgie DE için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    def mate():
        button_1.destroy()
        def install():
            os.system(" eopkg it -c desktop.mate -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Mate DE installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Mate DE kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            os.system(" eopkg it -c desktop.mate --rei -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Mate DE reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Mate DE yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            os.system(" eopkg rm -c desktop.mate --purge -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Mate DE uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Mate DE kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for Mate DE?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="Mate DE için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()   
    def openbox():
        button_1.destroy()
        def install():
            os.system(" eopkg it openbox obconf -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","OpenBox WM installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","OpenBox WM kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            os.system(" eopkg it openbox obconf --rei -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","OpenBox WM reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","OpenBox WM yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            os.system(" eopkg rm openbox obconf --purge -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","OpenBox WM uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","OpenBox WM kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for OpenBox WM?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="OpenBox WM için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    def i3():
        button_1.destroy()
        def install():
            os.system(" eopkg it i3 -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","i3 WM installation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","i3 WM kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def reinstall():
            os.system(" eopkg it i3 --rei -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","i3 WM reinstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","i3 WM yeniden kurulumu tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        def uninstall():
            os.system(" eopkg rm -c i3 --purge -y")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","i3 WM uninstallation is complete.\nYour computer will restart as soon as you click the 'OK' button to apply the changes.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","i3 WM kaldırılması tamamlandı.\nDeğişiklikleri uygulamak için 'OK' buttonuna bastığınız an bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            text1.config(text="What do you want to do for i3 WM?")
            button1.config(text="Install", command=install)
            button2.config(text="Reinstall", command=reinstall)
            button3.config(text="Uninstall", command=uninstall)
        elif os.path.isfile(lang_tr):
            text1.config(text="i3 WM için ne yapmak istiyorsunuz?")
            button1.config(text="Kur", command=install)
            button2.config(text="Yeniden kur", command=reinstall)
            button3.config(text="Kaldır", command=uninstall)
        button4.destroy()
        button5.destroy()
        button6.destroy()
        if os.path.isfile(lang_en):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to to menu", command=reopen)
        elif os.path.isfile(lang_tr):
            button_2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
            button_3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        button_2.pack()
        button_3.pack()
    if os.path.isfile(lang_en):
        text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Which desktop environment/window manager do you want to install or reinstall or uninstall?")
    elif os.path.isfile(lang_tr):    
        text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Hangi masaüstü ortamını/pencere yöneticisi kurmak ya da yeniden kurmak ya da kaldırmak istiyorsunuz?")
    text1.pack()
    space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    space1.pack()
    button1=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="KDE Plasma DE",command=kde)
    button1.pack()
    button2=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="GNOME DE",command=gnome)
    button2.pack()
    button3=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Budgie DE",command=budgie)
    button3.pack()
    button4=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Mate DE",command=mate)
    button4.pack()
    button5=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="İ3 WM",command=i3)
    button5.pack()
    button6=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="OpenBox WM",command=openbox)
    button6.pack()
    space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
    space2.pack()
    text2=Label(window, background=bg, foreground=fg, font="arial 9 bold", text="DE = Desktop Enviroment = Masaüstü Ortamı\nWM = Window Manager = Pencere Yöneticisi")
    text2.pack()
    space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    space3.pack()
    if os.path.isfile(lang_en):
        button_1=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
    elif os.path.isfile(lang_tr):
        button_1=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
    button_1.pack()

mainloop()