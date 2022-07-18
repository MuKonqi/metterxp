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
    print("\nModül kapatılıyor...\nClosing this module...")
    exit()
def reopen():
    print("\nModül yeniden başlatılıyor...\nRestarting this module...")
    window.destroy()
    os.system("pkexec python3 /usr/local/bin/metterxp/modules/pm_it.py")
def reboot():
    print("Bilgisayarınız yeniden başlatılıyor...\nRestarting your PC...")
    os.system("reboot now")

if not os.getuid() == 0:
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Only root can run this module!")
        exit("Only root can run this module!\nClosing this module...")
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
    window.title("Install/reinstall package manager | MetterXP")
elif os.path.isfile(lang_tr):
    window.title("Paket yöneticisi kur/yeniden kur | MetterXP")
window.config(background=bg)
window.resizable(0, 0)

def flatpak():
    def install():
        if os.path.isfile(debian):
            print("\nFlatpak kuruluyor...")
            os.system(" apt install flatpak -y")
        elif os.path.isfile(fedora):
            print("\nFlatpak kuruluyor...")
            os.system(" dnf install flatpak -y")
        elif os.path.isfile(solus):
            print("\nFlatpak kuruluyor...")
            os.system(" eopkg install flatpak -y")
        os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
        if os.path.isfile(lang_en):
            messagebox.showinfo("Information","Process completed. Press the 'OK' button and your computer will restart.")
        elif os.path.isfile(lang_tr):
            messagebox.showinfo("Bilgilendirme","İşlem tamamlandı. 'OK' tuşuna bastığınızda bilgisayarınız yeniden başlatılacak.")
        reboot()
    def reinstall():
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
        if os.path.isfile(lang_en):
            messagebox.showinfo("Information","Process completed. Press the 'OK' button and your computer will restart.")
        elif os.path.isfile(lang_tr):
            messagebox.showinfo("Bilgilendirme","İşlem tamamlandı. 'OK' tuşuna bastığınızda bilgisayarınız yeniden başlatılacak.")
        reboot()
    button1.destroy()
    button2.destroy()
    space2.destroy()
    button_1.destroy()
    if os.path.isfile(debian):
        def oldubuntuinstall():
            os.system(" add-apt-repository ppa:flatpak/stable")
            os.system(" apt update")
            os.system(" apt install flatpak")
            os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Process completed. Press the 'OK' button and your computer will restart.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","İşlem tamamlandı. 'OK' tuşuna bastığınızda bilgisayarınız yeniden başlatılacak.")
            reboot()
        if os.path.isfile(lang_en):
            flatpakbutton1_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Install\n(Ubuntu 18.04) and later or based on Debian GNU/Linux)", command=install)
            flatpakbutton1_2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Install\n(Ubuntu 17.10) and before)", command=oldubuntuinstall)
        elif os.path.isfile(lang_tr):
            flatpakbutton1_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Kur\n(Ubuntu 18.04 ve sonrası ya da Debian GNU/Linux'u taban alanlar)", command=install)
            flatpakbutton1_2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Kur\n(Ubuntu 17.10 ve öncesini taban alanlar)", command=oldubuntuinstall)
        flatpakbutton1_1.pack()
        flatpakbutton1_2.pack()
    else:
        if os.path.isfile(lang_en):
            flatpakbutton1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Install", command=install)
        elif os.path.isfile(lang_tr):
            flatpakbutton1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Kur", command=install)
        flatpakbutton1.pack()        
    if os.path.isfile(lang_en):
        text1.config(text="What do you want to do for Flatpak?")
        flatpakbutton2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Reinstall",command=reinstall)
        button_2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
        button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to menu", command=reopen)
        space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")        
        # flatpakbutton2.pack()
        # button_2.pack()
        # button_3.pack()
    elif os.path.isfile(lang_tr):
        text1.config(text="Flatpak için ne yapmak istiyorsunuz?")
        flatpakbutton2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Yeniden kur",command=reinstall)
        space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")        
        button_2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna sayfaya dön", command=module_exit)
        button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü yeniden başlat\nMenüye dön", command=reopen)
        # flatpakbutton2.pack()
        # button_3.pack()
        # button_2.pack()
    flatpakbutton2.pack()
    space3.pack()
    button_3.pack()
    button_2.pack()
def snap():
    button1.destroy()
    button2.destroy()
    space2.destroy()
    button_1.destroy()
    def install():
        if os.path.isfile(debian):
            os.system(" apt install snapd -y")
        elif os.path.isfile(fedora):
            os.system(" dnf install snapd -y")
        elif os.path.isfile(solus):
            os.system(" eopkg install snapd -y")
        if os.path.isfile(lang_en):
            messagebox.showinfo("Information","Process completed. Press the 'OK' button and your computer will restart.")
        elif os.path.isfile(lang_tr):
            messagebox.showinfo("Bilgilendirme","İşlem tamamlandı. 'OK' tuşuna bastığınızda bilgisayarınız yeniden başlatılacak.")
        reboot()
    def reinstall():
        if os.path.isfile(debian):
            print("\nSnap yeniden kuruluyor...")
            os.system(" apt reinstall snapd -y")
        elif os.path.isfile(fedora):
            print("\nSnap yeniden kuruluyor...")
            os.system(" dnf reinstall snapd -y")
        elif os.path.isfile(solus):
            print("\nSnap yeniden kuruluyor...")
            os.system(" eopkg install snapd --rei -y")
        if os.path.isfile(lang_en):
            messagebox.showinfo("Information","Process completed. Press the 'OK' button and your computer will restart.")
        elif os.path.isfile(lang_tr):
            messagebox.showinfo("Bilgilendirme","İşlem tamamlandı. 'OK' tuşuna bastığınızda bilgisayarınız yeniden başlatılacak.")
        reboot()
    if os.path.isfile(lang_en):
        text1.config(text="What do you want to do for Snap?")
        snapbutton1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Install",command=install)
        snapbutton2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Reinstall",command=reinstall)
        space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")        
        button_2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
        button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Restart this module\nBack to menu", command=reopen)
    elif os.path.isfile(lang_tr):
        text1.config(text="Snap için ne yapmak istiyorsunuz?")
        snapbutton1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Kur",command=install)
        snapbutton2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Yeniden kur",command=reinstall)
        space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
        button_2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Bu modülü kapat\nAna menüye dön", command=module_exit)
        button_3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Bu modülü yeniden başlat\nMenüye dön", command=reopen)
    snapbutton1.pack()
    snapbutton2.pack()
    space3.pack()
    button_3.pack()
    button_2.pack()

if os.path.isfile(lang_en):
    text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="PLease, select a package manager.")
    space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    button1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Flatpak", command=flatpak)
    button2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Snap", command=snap)
    space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    button_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
elif os.path.isfile(lang_tr):
    text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Lütfen bir paket yöneticisi seçiniz.")
    space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    button1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Flatpak", command=flatpak)
    button2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Snap", command=snap)
    space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    button_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna sayfaya dön", command=module_exit)
text1.pack()
space1.pack()
button1.pack()
button2.pack()
space2.pack()
button_1.pack()

mainloop()