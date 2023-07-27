#!/usr/bin/env python3

# Copyright (C) 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os
import getpass
import subprocess
from subprocess import *
username=getpass.getuser()
t="/home/"+username+"/.by-mukonqi/metterxp/theme/"

en="/home/"+username+"/.by-mukonqi/metterxp/language/en.txt"
tr="/home/"+username+"/.by-mukonqi/metterxp/language/tr.txt"

global gfs
gfs=0

def main():
    if not os.path.isdir("/home/"+username+"/.by-mukonqi/metterxp/theme") or gfs == 1:
        if not os.path.isdir("/home/"+username+"/.by-mukonqi/metterxp/theme"):
            os.system("cd /home/"+username+"/.by-mukonqi ; mkdir metterxp/theme")
        bg="#2f2f2f"
        fg="#376296"
        button_bg="#a9a9a9"
        button_fg="#000000"
        a_button_bg="#376296"
        a_button_fg="#FFFFFF"

    def langen():
        os.system("cd /home/"+username+"/.by-mukonqi/metterxp/language/ ; rm * ; touch en.txt")
        messagebox.showinfo("Information","Successful! English language applied.")
        swindow.destroy()
        os.system("python3 /usr/bin/metterxp")
    def langtr():
        os.system("cd /home/"+username+"/.by-mukonqi/metterxp/language/ ; rm * ; touch tr.txt")
        messagebox.showinfo("Bilgilendirme","Başarılı! Türkçe dili uygulandı.") 
        swindow.destroy()
        os.system("python3 /usr/bin/metterxp")
    swindow=Tk()
    swindow.config(background=bg)
    swindow.resizable(0, 0)
    sparent = Frame(swindow)
    sparent.pack(expand=1)
    swindow.geometry("483x483")


    def mukonqi():
        def one():
            subprocess.Popen("metterxp 2021 p", shell=TRUE)
        def two():
            subprocess.Popen("metterxp 2022 p", shell=TRUE)
        def modern():
            subprocess.Popen("metterxp modern p", shell=TRUE)
        def machine():
            subprocess.Popen("metterxp machine p", shell=TRUE)
        
        mwindow=Tk()
        mwindow.config(background=bg)
        mwindow.resizable(0, 0)
        mparent = Frame(mwindow)
        mparent.pack(expand=1)
        mwindow.geometry("412x412")
        if os.path.isfile(en):
            mwindow.title("Themes from developer - Settings | MetterXP")
            mtext1=Label(mparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Please select a theme.")
            mspace1=Label(mparent, background=bg, foreground=fg, font="arial 3", text="\n")
            mbutton1=Button(mparent, text="Classic [From BetterXP (2021)]", command=one, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 11 bold", cursor="hand2", borderwidth="8")
            mbutton2=Button(mparent, text="Modern [From MetterXP but revised (2022)]", command=two, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")
            mbutton3=Button(mparent, text="Modern", command=modern, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 11 bold", cursor="hand2", borderwidth="8")
            mbutton4=Button(mparent, text="Machine", command=machine, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")
        elif os.path.isfile(tr):
            mwindow.title("Geliştiriciden temalar - Ayarlar | MetterXP")
            mtext1=Label(mparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Lütfen bir tema seçin.")
            mspace1=Label(mparent, background=bg, foreground=fg, font="arial 3", text="\n")
            mbutton1=Button(mparent, text="Klasik [BetterXP'dan (2021)]", command=one, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 11 bold", cursor="hand2", borderwidth="8")
            mbutton2=Button(mparent, text="Modern [MetterXP'dan ama revizeli (2022)]", command=two, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")
            mbutton3=Button(mparent, text="Modern", command=modern, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 11 bold", cursor="hand2", borderwidth="8")
            mbutton4=Button(mparent, text="Makine", command=machine, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")
        mtext1.pack(fill="x")
        mspace1.pack(fill="x")
        mbutton1.pack(fill="x")
        mbutton2.pack(fill="x")
        mbutton3.pack(fill="x")
        mbutton4.pack(fill="x")
    
    
    def colors():
        def black():
            subprocess.Popen("metterxp black p", shell=TRUE)
        def white():
            subprocess.Popen("metterxp white p", shell=TRUE)
        def gray():
            subprocess.Popen("metterxp gray p", shell=TRUE)
        def red():
            subprocess.Popen("metterxp red p", shell=TRUE)
        def yellow():
            subprocess.Popen("metterxp yellow p", shell=TRUE)
        def green():
            subprocess.Popen("metterxp green p", shell=TRUE)
        def blue():
            subprocess.Popen("metterxp blue p", shell=TRUE)
        def navy():
            subprocess.Popen("metterxp navy-blue p", shell=TRUE)
        def purple():
            subprocess.Popen("metterxp purple p", shell=TRUE)
        def lilac():
            subprocess.Popen("metterxp lilac p", shell=TRUE)
        def pink():
            subprocess.Popen("metterxp pink p", shell=TRUE)
            
        cwindow=Tk()
        cwindow.config(background=bg)
        cwindow.resizable(0, 0)
        cparent = Frame(cwindow)
        cparent.pack(expand=1)
        cwindow.geometry("600x600")
        if os.path.isfile(en):
            cwindow.title("Themes from developer - Settings | MetterXP")
            ctext1=Label(cparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Please select a theme.")
            cspace1=Label(cparent, background=bg, foreground=fg, font="arial 3", text="\n")
            cbutton1=Button(cparent, text="Black (Dark)", command=black, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton2=Button(cparent, text="White (White)", command=white, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton3=Button(cparent, text="Gray", command=gray, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton4=Button(cparent, text="Red", command=red, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton5=Button(cparent, text="Yellow", command=yellow, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton6=Button(cparent, text="Green", command=green, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton7=Button(cparent, text="Blue", command=blue, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton8=Button(cparent, text="Navy Blue", command=navy, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton9=Button(cparent, text="Purple", command=purple, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton10=Button(cparent, text="Lilac", command=lilac, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton11=Button(cparent, text="Pink", command=pink, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
        elif os.path.isfile(tr):
            cwindow.title("Geliştiriciden temalar - Ayarlar | MetterXP")
            ctext1=Label(cparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Lütfen bir tema seçin.")
            cspace1=Label(cparent, background=bg, foreground=fg, font="arial 3", text="\n")
            cbutton1=Button(cparent, text="Siyah (Koyu)", command=black, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton2=Button(cparent, text="Beyaz (Açık)", command=white, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton3=Button(cparent, text="Gri", command=gray, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton4=Button(cparent, text="Kırmızı", command=red, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton5=Button(cparent, text="Sarı", command=yellow, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton6=Button(cparent, text="Yeşil", command=green, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton7=Button(cparent, text="Mavi", command=blue, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton8=Button(cparent, text="Lacivert", command=navy, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton9=Button(cparent, text="Mor", command=purple, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton10=Button(cparent, text="Lila", command=lilac, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton11=Button(cparent, text="Pembe", command=pink, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
        ctext1.pack(fill="x")
        cspace1.pack(fill="x")
        cbutton1.pack(fill="x")
        cbutton2.pack(fill="x")
        cbutton3.pack(fill="x")
        cbutton4.pack(fill="x")
        cbutton5.pack(fill="x")
        cbutton6.pack(fill="x")
        cbutton7.pack(fill="x")
        cbutton8.pack(fill="x")
        cbutton9.pack(fill="x")
        cbutton10.pack(fill="x")
        cbutton11.pack(fill="x")
    
    
    def people():
        pass
    
    
    def custom():
        pass
        
        
    if os.path.isfile(en):
        swindow.title("Settings | MetterXP")
        stext1=Label(sparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Please select a theme category.")
        sspace1=Label(sparent, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton1=Button(sparent, text="From developer [MuKonqi (Muhammed Abdurrahman)]", command=mukonqi, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 11 bold", cursor="hand2", borderwidth="7")
        sbutton2=Button(sparent, text="Simple color themes", command=colors, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="7")
        sbutton3=Button(sparent, text="From people", command=people, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 11 bold", cursor="hand2", borderwidth="7")
        sbutton4=Button(sparent, text="Custom", command=custom, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="7")
        sspace2=Label(sparent, background=bg, foreground=fg, font="arial 3", text="\n\n")
        stext2=Label(sparent, background=bg, foreground=fg, font="arial 11 bold italic", text="You can change your language preferences below.")
        sspace3=Label(sparent, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton5=Button(sparent, text="English (English)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 11 bold", cursor="hand2", borderwidth="7")
        sbutton6=Button(sparent, text="Turkish (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="7")
    elif os.path.isfile(tr):
        swindow.title("Ayarlar | MetterXP")
        stext1=Label(sparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Lütfen bir tema kategorisi seçiniz.")
        sspace1=Label(sparent, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton1=Button(sparent, text="Geliştiriciden [MuKonqi (Muhammed Abdurrahman)]", command=mukonqi, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 11 bold", cursor="hand2", borderwidth="7")
        sbutton2=Button(sparent, text="Basit renk temaları", command=colors, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="7")
        sbutton3=Button(sparent, text="İnsanlardan", command=people, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 11 bold", cursor="hand2", borderwidth="7")
        sbutton4=Button(sparent, text="Özel", command=custom, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="7")
        sspace2=Label(sparent, background=bg, foreground=fg, font="arial 3", text="\n\n")
        stext2=Label(sparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Aşağıdan dil tercihlerinizi değiştirebilirsiniz.")
        sspace3=Label(sparent, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton5=Button(sparent, text="English (İngilizce)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 11 bold", cursor="hand2", borderwidth="7")
        sbutton6=Button(sparent, text="Türkçe (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="7")
    stext1.pack(fill="x")
    sspace1.pack(fill="x")
    sbutton1.pack(fill="x")
    sbutton2.pack(fill="x")
    sbutton3.pack(fill="x")
    sbutton4.pack(fill="x")
    sspace2.pack(fill="x")
    stext2.pack(fill="x")
    sspace3.pack(fill="x")
    sbutton5.pack(fill="x")
    sbutton6.pack(fill="x")
    mainloop()
    exit()
    
def first_start():
    global gfs
    gfs=1
    bg="#2f2f2f"
    fg="#376296"
    button_bg="#a9a9a9"
    button_fg="#000000"
    a_button_bg="#376296"
    a_button_fg="#FFFFFF"
    def llangen():
        os.system("cd /home/"+username+"/.by-mukonqi/metterxp/language/ ; touch en.txt")
        messagebox.showinfo("Information","English language applied! When you click 'OK', MetterXP settings will open.")
        lwindow.destroy()
        main()
    def llangtr():
        os.system("cd /home/"+username+"/.by-mukonqi/metterxp/language ; touch tr.txt")
        messagebox.showinfo("Bilgilendirme","İstenilen dil uygulandı! 'OK' tuşuna bastığınızda MetterXP ayarları açılacak.")
        lwindow.destroy()
        main()
    lwindow=Tk()
    lwindow.title("First Start of MetterXP")
    lwindow.config(background=bg)
    lparent = Frame(lwindow)
    lparent.pack(expand=1)
    lwindow.geometry("322x161")
    ltext1=Label(lparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Please choose a language for MetterXP.\nMetterXP için lütfen bir dil seçin.")
    ltext1.pack(fill="x")
    lspace1=Label(lparent, background=bg, foreground=fg, font="arial 3", text="\n")
    lspace1.pack(fill="x")
    lbutton1=Button(lparent, text="English (İngilizce)", command=llangen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 11 bold", cursor="hand2", borderwidth="4")
    lbutton1.pack(fill="x")
    lbutton2=Button(lparent, text="Türkçe (Turkish)", command=llangtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="4")
    lbutton2.pack(fill="x")
    mainloop()

if not os.path.isdir("/home/"+username+"/.by-mukonqi/"):
    os.system("cd /home/"+username+" ; mkdir .by-mukonqi")
    os.system("cd /home/"+username+"/.by-mukonqi ; mkdir metterxp ; mkdir metterxp/language")
    first_start()
if not os.path.isdir("/home/"+username+"/.by-mukonqi/metterxp"):
    os.system("cd /home/"+username+"/.by-mukonqi ; mkdir metterxp ; mkdir metterxp/language")
    first_start()

bg=""
fg=""
button_bg=""
button_fg=""
a_button_bg=""
a_button_fg=""
if os.path.isfile(t+"2021.txt"):
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
elif os.path.isfile(t+"modern.txt"):
    bg="#2f2f2f"
    fg="#376296"
    button_bg="#a9a9a9"
    button_fg="#000000"
    a_button_bg="#376296"
    a_button_fg="#FFFFFF"
elif os.path.isfile(t+"machine.txt"):
    bg="#2f2f2f"
    fg="#FFFFFF"
    button_bg="#bf2422"
    button_fg="#2f2f2f"
    a_button_bg="#5dc305"
    a_button_fg="#376296"
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
else:
    gfs=1
    if os.path.isfile(en):
        messagebox.showwarning("Warning","Can't found theme configuration. When you click 'OK' settings will open.")
    elif os.path.isfile(tr):
        messagebox.showwarning("Uyarı","Tema yapılandırması bulunamadı. Ayarlar 'OK' tuşuna bastığınızda açılacaktır.")
    main()
    exit()

main()