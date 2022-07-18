#!/usr/bin/env python3

# Copyright (C) 2021, 2022 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
from subprocess import *
import subprocess
import os

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp/settings/lang/en.txt"


def module_exit():
    print("\nModül kapatılıyor...\nClosing this module...")
    exit()

if os.getuid() == 0:
    if os.path.isfile(lang_en):
        messagebox.showerror("Error","Only normal user can run this module!")
        exit("Only normal user can run this module!\nClosing this module...")
    elif os.path.isfile(lang_tr):
        messagebox.showerror("Hata","Sadece normal kullanıcı bu modülü çalıştırabilir!")
        exit("\nSadece normal kullanıcı bu modülü çalıştırabilir!\nModül kapatılıyor...")
    

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
    window.title("Search application/package | MetterXP")
elif os.path.isfile(lang_tr):
    window.title("Program/paket ara | MetterXP")
window.config(background=bg)
window.resizable(0, 0)

def packagesearch():
    if os.path.isfile(debian):
        c1_package=" apt search "
        get_packagename=packagename.get()
        cf_package=c1_package+get_packagename
        run_cf_package = subprocess.Popen(cf_package, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
    elif os.path.isfile(fedora):
        c1_package=" dnf search "
        get_packagename=packagename.get()
        cf_package=c1_package+get_packagename
        run_cf_package = subprocess.Popen(cf_package, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
    elif os.path.isfile(solus):
        c1_package=" eopkg search "
        get_packagename=packagename.get()
        cf_package=c1_package+get_packagename
        run_cf_package = subprocess.Popen(cf_package, shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
        (out, err) = run_cf_package.communicate()
    if os.path.isfile(lang_en):
        window_2=Toplevel()
        window_2.title("Output | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Label(window_2, background=bg, foreground=fg, font="arial 12", text="\nInformation: When the package name you entered is correct, the process has been completed successfully!\n\nNote: Changing the output of the command below will not change anything.\n")
        text4=Text(window_2, yscrollcommand=scroll.set)
        text4.insert(END, out)
        scroll.config(command=text4.yview)
        space4=Label(window_2, background=bg, foreground=fg, text="\n", font="arial 3")
        button_2=Button(window_2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close window", command=window_2.destroy)
    elif os.path.isfile(lang_tr):
        window_2=Toplevel()
        window_2.title("Çıktı | MetterXP")
        window_2.config(background=bg)
        window_2.resizable(0, 0)
        scroll=Scrollbar(window_2)
        text3=Label(window_2, background=fg, foreground=bg, font="arial 12", text="\nBilgilendirme: Eğer girdiğiniz paket adı hatalı değilse işlem başarıyla tamamlandı!\n\nNot: Aşağıdaki komut çıktısını değiştirmeniz herhangi bir şey değiştirmez.\n")
        text4=Text(window_2, yscrollcommand=scroll.set)
        text4.insert(END, out)
        scroll.config(command=text4.yview)
        space4=Label(window_2, background=bg, foreground=fg, text="\n", font="arial 3")
        button_2=Button(window_2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Pencereyi kapat", command=window_2.destroy)
    scroll.pack(side=RIGHT,fill=Y)
    text3.pack()
    text4.pack()
    space4.pack()
    button_2.pack()
if os.path.isfile(lang_en):
    text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Please enter the name of the program/package you want to search.\nNote: You must enter the package name correctly!")
    space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    packagename=Entry(window)
    b_packagesearch=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Search",command=packagesearch)
    space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
    text2=Label(window, background=bg, foreground=fg, font="arial 9 bold", text="Information: There may be some errors (meaningless letters, numbers, etc.) in the command output to be opened.\nPlease ignore this.")
    space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    exit_button_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
elif os.path.isfile(lang_tr):
    text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Lütfen aratmak istediğiniz programın/paketin adını giriniz.\nNot: Paket adını doğru girmeniz gerekmektedir!")
    space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    packagename=Entry(window)
    b_packagesearch=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Ara",command=packagesearch)
    space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
    text2=Label(window, background=bg, foreground=fg, font="arial 9 bold", text="Bilgilendirme: Açılacak komut çıktısında bazı hatalar (anlamsız harfler, sayılar vb.) olabilir.\nLütfen bunu dikkate almayınız.")
    space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    exit_button_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
text1.pack()
space1.pack()
packagename.pack()
b_packagesearch.pack()
space2.pack()
text2.pack()
space3.pack()
exit_button_1.pack()

mainloop()