#!/usr/bin/env python3

# Copyright (C) 2021, 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os


debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp/settings/lang/en.txt"

def reboot():
    print()
    os.system("reboot now")

if not os.getuid() == 0:
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Only root can run this module!")
        exit()
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit()
    

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


window=Tk(className="MetterXP")
if os.path.isfile(lang_en):
    window.title("Configre softwares | MetterXP")
elif os.path.isfile(lang_tr):
    window.title("Yazılımları yapılandır | MetterXP")
window.config(background=bg)
window.resizable(0, 0)
window.geometry("322x322")
icon = PhotoImage(file="/usr/local/bin/metterxp/icon.png")
window.iconphoto(True, icon)
parent = Frame(window)

def grub():
    if os.path.isfile("/usr/bin/grub-customizer") or os.path.isfile("/bin/grub-customizer"):
        os.system(" grub-customizer")
    else:
        if os.path.isfile(lang_en):
            messagebox.showwarning("Warning","Grub Customizer can't found on your system. When you click 'OK', the installation will start.")
        elif os.path.isfile(lang_tr):
            messagebox.showwarning("Uyarı","Grub Customizer sisteminizde bulunamadı, 'OK' tuşuna bastığınızda kurulum başlatılacak.")
        if os.path.isfile(debian):
            os.system(" apt install grub-customizer -y")
        elif os.path.isfile(fedora):
            os.system(" dnf install grub-customizer -y")
        elif os.path.isfile(solus):
            os.system(" eopkg install grub-customizer -y")
        os.system("grub-customizer")
def cups():
    if not os.path.isfile("/usr/bin/cups") or not os.path.isfile("/bin/cups"):
        if os.path.isfile(lang_en):
            messagebox.showwarning("Warning","Cups can't found on your system. When you click 'OK', the installation will start.")
        elif os.path.isfile(lang_tr):
            messagebox.showwarning("Uyarı","Cups sisteminizde bulunamadı, 'OK' tuşuna bastığınızda kurulum başlatılacak.")
        if os.path.isfile(debian):
            os.system(" apt install cups -y")
        elif os.path.isfile(fedora):
            os.system(" dnf install cups -y")
        elif os.path.isfile(solus):
            os.system(" eopkg install cups -y")
    os.system("x-www-browser localhost:631")
    if os.path.isfile(lang_en):
        messagebox.showinfo("Information","Successful! Cups configuration completed.")
    elif os.path.isfile(lang_tr):
        messagebox.showinfo("Bilgilendirme","Cups yapılandırması başarıyla tamamlandı.")
def wine():
    if not os.path.isfile("/usr/bin/wine") or not os.path.isfile("/bin/wine"):
        if os.path.isfile(lang_en):
            messagebox.showwarning("Warning","Wine can't found on your system. When you click 'OK', the installation will start.")
        elif os.path.isfile(lang_tr):
            messagebox.showwarning("Uyarı","Wine sisteminizde bulunamadı, 'OK' tuşuna bastığınızda kurulum başlatılacak.")
        if os.path.isfile(debian):
            os.system(" dpkg --add-architecture i386")
            os.system(" apt install wine-stable -y")      
        elif os.path.isfile(fedora):
            os.system(" dnf install wine -y")
        elif os.path.isfile(solus):
            os.system(" eopkg install wine -y")
    os.system("winecfg")
    if os.path.isfile(lang_en):
        messagebox.showinfo("Information","Successful! Wine configuration completed.")
    elif os.path.isfile(lang_tr):
        messagebox.showinfo("Bilgilendirme","Wine yapılandırması başarıyla tamamlandı.")
def pcrename():
    def addpcname():
        get_new_pc_name=new_pc_name.get()
        add_new_pc_name=open('/etc/hostname', "w")
        add_new_pc_name.write(get_new_pc_name)
        add_new_pc_name.close()
        if os.path.isfile(lang_en):
            messagebox.showinfo("Information","When you press 'OK' button and your computer will restart to apply the new name of your computer.")
        elif os.path.isfile(lang_tr):
            messagebox.showinfo("Bilgilendirme"," 'OK' tuşuna bastığınızda bilgisayarınızın yeni adını uygulamak için bilgisayarınız yeniden başlatılacak.")
        reboot()
    window2=Tk(className="MetterXP")
    window2.config(background=bg)
    window2.resizable(0, 0)
    window2.geometry("400x150")
    parent2 = Frame(window2)
    if os.path.isfile(lang_en):
        window2.title("Change this PC's name | MetterXP")
        text2=Label(parent2, background=bg, foreground=fg, font="arial 11 bold italic", text="Enter a new name for your computer below.")
        space3=Label(parent2, background=bg, foreground=fg, font="arial 2", text="\n")
        new_pc_name=Entry(parent2)
        b_1_pcrename=Button(parent2,  cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Save",command=addpcname)
    elif os.path.isfile(lang_tr):
        window2.title("Bu bilgisayarın adını değiştir | MetterXP")
        text2=Label(parent2, background=bg, foreground=fg, font="arial 11 bold italic", text="Aşağıya bilgisayarınız için yeni bir ad giriniz.")
        space3=Label(parent2, background=bg, foreground=fg, font="arial 2", text="\n")
        new_pc_name=Entry(parent2)
        b_1_pcrename=Button(parent2,  cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Kaydet",command=addpcname)
    parent2.pack(expand=1)
    text2.pack(fill="x")   
    space3.pack(fill="x")
    new_pc_name.pack(fill="x")
    b_1_pcrename.pack(fill="x")
if os.path.isfile(lang_en):
    text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Please choose something.")
    space1=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
    button1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Configure GRUB bootloader\n(with the help of Grub Customizer)", command=grub)
    button2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Configure Cups printer manager", command=cups)
    button3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Configure Wine", command=wine)
    button4=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Change this PC's name", command=pcrename)
elif os.path.isfile(lang_tr):
    text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Lütfen bir şey seçin.")
    space1=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
    button1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="GRUB önyükleyiciyi yapılandır\n(Grub Customizer yardımıyla)", command=grub)
    button2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Cups yazıcı yöneticisini yapılandır", command=cups)
    button3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Wine'ı yapılandır", command=wine)
    button4=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Bu bilgisayarın adını değiştir", command=pcrename)
parent.pack(expand=1)
text1.pack(fill="x")
space1.pack(fill="x")
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")

mainloop()