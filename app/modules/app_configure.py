#!/usr/bin/env python3

# Copyright (C) 2021, 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os
import sys

t="/home/"+str(sys.argv[1])+"/.by-mukonqi/metterxp/theme/"
en="/home/"+str(sys.argv[1])+"/.by-mukonqi/metterxp/language/en.txt"
tr="/home/"+str(sys.argv[1])+"/.by-mukonqi/metterxp/language/tr.txt"
debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if not os.path.isdir("/home/"+str(sys.argv[1])+"/.by-mukonqi/metterxp/"):
    messagebox.showerror("User Error - Fatal | MetterXP","Please start only MetterXP (just select MetterXP in the applications section or type metterxp) to set up language and theme preferences.")
    exit()

if not os.getuid() == 0:
    if os.path.isfile(en):
        messagebox.showerror("Error","Only root can run this module!")
        exit()
    elif os.path.isfile(tr):
        messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
        exit()
    

bg=""
fg=""
button_bg=""
button_fg=""
a_button_bg=""
a_button_fg=""
if os.path.isfile(t+"2011.txt"):
    bg="#9e9c9d"
    fg="#e3af79"
    button_bg="#d2d1d2"
    button_fg="#3a1212"
    a_button_bg="#0b75aa"
    a_button_fg="#FFFFFF"    
elif os.path.isfile(t+"2021.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#03035B"
    a_button_fg="#FFFFFF"
elif os.path.isfile(t+"2022.txt"):
    bg="#a9a9a9"
    fg="#376296"
    button_bg="#FFFFFF"
    button_fg="#376296"
    a_button_bg="#376296"
    a_button_fg="#FFFFFF"
elif os.path.isfile(t+"23Q2.txt"):
    bg="#2f2f2f"
    fg="#FFFFFF"
    button_bg="#bf2422"
    button_fg="#2f2f2f"
    a_button_bg="#5dc305"
    a_button_fg="#376296"
elif os.path.isfile(t+"23H2.txt"):
    bg="#2f2f2f"
    fg="#376296"
    button_bg="#a9a9a9"
    button_fg="#000000"
    a_button_bg="#376296"
    a_button_fg="#FFFFFF"
elif os.path.isfile(t+"black.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
elif os.path.isfile(t+"white.txt"):
    bg="#FFFFFF"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFFFF"
    a_button_bg="#FFFFFF"
    a_button_fg="#000000"
elif os.path.isfile(t+"gray.txt"):
    bg="#a9a9a9"
    fg="#000000"
    button_bg="#000000"
    button_fg="#a9a9a9"
    a_button_bg="#a9a9a9"
    a_button_fg="#000000"  
elif os.path.isfile(t+"red.txt"):
    bg="#FF0000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#FF0000"
    a_button_bg="#FF0000"
    a_button_fg="#FFFFFF"
elif os.path.isfile(t+"yellow.txt"):
    bg="#FFFF00"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFF00"
    a_button_bg="#FFFF00"
    a_button_fg="#000000"    
elif os.path.isfile(t+"green.txt"):
    bg="#008000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#008000"
    a_button_bg="#008000"
    a_button_fg="#FFFFFF"
elif os.path.isfile(t+"blue.txt"):
    bg="#0000FF"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#0000FF"
    a_button_bg="#0000FF"
    a_button_fg="#FFFFFF"    
elif os.path.isfile(t+"navy-blue.txt"):
    bg="#000080"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000080"
    a_button_bg="#000080"
    a_button_fg="#FFFFFF"      
elif os.path.isfile(t+"purple.txt"):
    bg="#800080"
    fg="#000000"
    button_bg="#000000"
    button_fg="#800080"
    a_button_bg="#800080"
    a_button_fg="#000000"
elif os.path.isfile(t+"lilac.txt"):
    bg="#C8A2C8"
    fg="#000000"
    button_bg="#000000"
    button_fg="#C8A2C8"
    a_button_bg="#C8A2C8"
    a_button_fg="#000000"
elif os.path.isfile(t+"pink.txt"):
    bg="#FFC0CB"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFC0CB"
    a_button_bg="#FFC0CB"
    a_button_fg="#000000"  
elif os.path.isfile(t+"complex_atno.txt"):
    bg="#474747"
    fg="#00252e"
    button_bg="#012547"
    button_fg="#8c0606"
    a_button_bg="#034d96"
    a_button_fg="#a4d46a"  
elif os.path.isfile(t+"theme.txt"):
    bgo=open(t+"bg.txt", "r")
    bgr="#"+bgo.read()
    bgo.close()
    bg=bgr.replace("\n","") 
    fgo=open(t+"fg.txt", "r")
    fgr="#"+fgo.read()
    fgo.close()
    fg=fgr.replace("\n","")
    bbgo=open(t+"button_bg.txt", "r")
    button_bgr="#"+bbgo.read()
    bbgo.close()
    button_bg=button_bgr.replace("\n","")
    bfgo=open(t+"button_fg.txt", "r")
    button_fgr="#"+bfgo.read()
    bfgo.close()
    button_fg=button_fgr.replace("\n","")
    abbgo=open(t+"a_button_bg.txt", "r")
    a_button_bgr="#"+abbgo.read()
    abbgo.close()
    a_button_bg=a_button_bgr.replace("\n","")
    abfgo=open(t+"a_button_fg.txt", "r")
    a_button_fgr="#"+abfgo.read()
    abfgo.close()
    a_button_fg=a_button_fgr.replace("\n","")
else:
    if os.path.isfile(en):
        messagebox.showerror("User Error - Fatal | MetterXP","Please start only MetterXP (just select MetterXP in the applications section or type metterxp) to set up theme preferences.")
    elif os.path.isfile(tr):
        messagebox.showerror("Kullanıcı Hatası - Ölümcül | MetterXP", "Tema tercihlerini ayarlamak için lütfen yalnızca MetterXP'yi başlatın (uygulamalar bölümünde MetterXP'yi seçin veya metterxp yazın.")
    exit()

def reboot():
    os.system("reboot now")

window=Tk(className="MetterXP")
if os.path.isfile(en):
    window.title("Configure softwares | MetterXP")
elif os.path.isfile(tr):
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
        if os.path.isfile(en):
            messagebox.showwarning("Warning","Grub Customizer can't found on your system. When you click 'OK', the installation will start.")
        elif os.path.isfile(tr):
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
        if os.path.isfile(en):
            messagebox.showwarning("Warning","Cups can't found on your system. When you click 'OK', the installation will start.")
        elif os.path.isfile(tr):
            messagebox.showwarning("Uyarı","Cups sisteminizde bulunamadı, 'OK' tuşuna bastığınızda kurulum başlatılacak.")
        if os.path.isfile(debian):
            os.system(" apt install cups -y")
        elif os.path.isfile(fedora):
            os.system(" dnf install cups -y")
        elif os.path.isfile(solus):
            os.system(" eopkg install cups -y")
    os.system("x-www-browser localhost:631")
    if os.path.isfile(en):
        messagebox.showinfo("Information","Successful! Cups configuration completed.")
    elif os.path.isfile(tr):
        messagebox.showinfo("Bilgilendirme","Cups yapılandırması başarıyla tamamlandı.")
def wine():
    if not os.path.isfile("/usr/bin/wine") or not os.path.isfile("/bin/wine"):
        if os.path.isfile(en):
            messagebox.showwarning("Warning","Wine can't found on your system. When you click 'OK', the installation will start.")
        elif os.path.isfile(tr):
            messagebox.showwarning("Uyarı","Wine sisteminizde bulunamadı, 'OK' tuşuna bastığınızda kurulum başlatılacak.")
        if os.path.isfile(debian):
            os.system(" dpkg --add-architecture i386")
            os.system(" apt install wine-stable -y")      
        elif os.path.isfile(fedora):
            os.system(" dnf install wine -y")
        elif os.path.isfile(solus):
            os.system(" eopkg install wine -y")
    os.system("winecfg")
    if os.path.isfile(en):
        messagebox.showinfo("Information","Successful! Wine configuration completed.")
    elif os.path.isfile(tr):
        messagebox.showinfo("Bilgilendirme","Wine yapılandırması başarıyla tamamlandı.")
def pcrename():
    def addpcname():
        get_new_pc_name=new_pc_name.get()
        add_new_pc_name=open('/etc/hostname', "w")
        add_new_pc_name.write(get_new_pc_name)
        add_new_pc_name.close()
        if os.path.isfile(en):
            messagebox.showinfo("Information","When you press 'OK' button and your computer will restart to apply the new name of your computer.")
        elif os.path.isfile(tr):
            messagebox.showinfo("Bilgilendirme"," 'OK' tuşuna bastığınızda bilgisayarınızın yeni adını uygulamak için bilgisayarınız yeniden başlatılacak.")
        reboot()
    window2=Tk(className="MetterXP")
    window2.config(background=bg)
    window2.resizable(0, 0)
    window2.geometry("400x150")
    parent2 = Frame(window2)
    if os.path.isfile(en):
        window2.title("Change this PC's name | MetterXP")
        text2=Label(parent2, background=bg, foreground=fg, font="arial 11 bold italic", text="Enter a new name for your computer below.")
        space3=Label(parent2, background=bg, foreground=fg, font="arial 2", text="\n")
        new_pc_name=Entry(parent2)
        b_1_pcrename=Button(parent2,  cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Save",command=addpcname)
    elif os.path.isfile(tr):
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
if os.path.isfile(en):
    text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="Please choose something.")
    space1=Label(parent, background=bg, foreground=fg, text="\n", font="arial 3")
    button1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Configure GRUB bootloader\n(with the help of Grub Customizer)", command=grub)
    button2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Configure Cups printer manager", command=cups)
    button3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Configure Wine", command=wine)
    button4=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Change this PC's name", command=pcrename)
elif os.path.isfile(tr):
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