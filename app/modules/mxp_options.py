#!/usr/bin/env python3

# Copyright (C) 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os
import getpass
import subprocess
from subprocess import *
from tkinter.colorchooser import askcolor
username=getpass.getuser()
t="/home/"+username+"/.by-mukonqi/metterxp/theme/"

en="/home/"+username+"/.by-mukonqi/metterxp/language/en.txt"
tr="/home/"+username+"/.by-mukonqi/metterxp/language/tr.txt"

global gfs
gfs=0

if os.getuid() == 0:
    if os.path.isfile(en):
        messagebox.showerror("Error","Root can't run this module!")
    elif os.path.isfile(tr):
        messagebox.showerror("Hata","Kök kullanıcı bu modülü çalıştıramaz!")
    exit()

def main():
    global bg, fg, button_bg, button_fg, a_button_bg, a_button_fg
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
    swindow=Tk(className="MetterXP")
    swindow.config(background=bg)
    swindow.resizable(0, 0)
    sparent = Frame(swindow)
    sparent.pack(expand=1)
    swindow.geometry("483x483")
    icon = PhotoImage(file="/usr/local/bin/metterxp/icon.png")
    swindow.iconphoto(True, icon)


    def mukonqi():
        def eleven():
            subprocess.Popen("metterxp 2011 p", shell=True)
        def one():
            subprocess.Popen("metterxp 2021 p", shell=True)
        def two():
            subprocess.Popen("metterxp 2022 p", shell=True)
        def threeq2():
            subprocess.Popen("metterxp 23Q2 p", shell=True)
        def threeh2():
            subprocess.Popen("metterxp 23H2 p", shell=True)
        
        mwindow=Tk(className="MetterXP")
        mwindow.config(background=bg)
        mwindow.resizable(0, 0)
        mparent = Frame(mwindow)
        mparent.pack(expand=1)
        mwindow.geometry("483x483")
        if os.path.isfile(en):
            mwindow.title("Themes From Developer - Settings | MetterXP")
            mtext1=Label(mparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Please select a theme.")
            mspace1=Label(mparent, background=bg, foreground=fg, font="arial 3", text="\n")
            mbutton1=Button(mparent, text="Veteran [old computer (2011)]", command=eleven, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")
            mbutton2=Button(mparent, text="Classic [from latest BetterXP (2021)]", command=one, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")
            mbutton3=Button(mparent, text="Modern [from old MetterXP's but revised (2022)]", command=two, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")
            mbutton4=Button(mparent, text="Machine [my new computer (23Q2)]", command=threeq2, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")
            mbutton5=Button(mparent, text="Default [from this MetterXP's (23H2)]", command=threeh2, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")        
        elif os.path.isfile(tr):
            mwindow.title("Geliştiriciden Temalar - Ayarlar | MetterXP")
            mtext1=Label(mparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Lütfen bir tema seçin.")
            mspace1=Label(mparent, background=bg, foreground=fg, font="arial 3", text="\n")
            mbutton1=Button(mparent, text="Emektar [eski bilgisayar (2011)]", command=eleven, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")
            mbutton2=Button(mparent, text="Klasik [sonuncu BetterXP'dan (2021)]", command=one, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")
            mbutton3=Button(mparent, text="Modern [eski MetterXP'lerden ama revizeli (2022)]", command=two, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")
            mbutton4=Button(mparent, text="Makine [yeni bilgisayarım (23Q2)]", command=threeq2, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")            
            mbutton5=Button(mparent, text="Varsayılan [bu MetterXP'lerden (23H2)]", command=threeh2, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")
        mtext1.pack(fill="x")
        mspace1.pack(fill="x")
        mbutton1.pack(fill="x")
        mbutton2.pack(fill="x")
        mbutton3.pack(fill="x")
        mbutton4.pack(fill="x")
        mbutton5.pack(fill="x")
    
    
    def colors():
        def black():
            subprocess.Popen("metterxp black p", shell=True)
        def white():
            subprocess.Popen("metterxp white p", shell=True)
        def gray():
            subprocess.Popen("metterxp gray p", shell=True)
        def red():
            subprocess.Popen("metterxp red p", shell=True)
        def yellow():
            subprocess.Popen("metterxp yellow p", shell=True)
        def green():
            subprocess.Popen("metterxp green p", shell=True)
        def blue():
            subprocess.Popen("metterxp blue p", shell=True)
        def navy():
            subprocess.Popen("metterxp navy-blue p", shell=True)
        def purple():
            subprocess.Popen("metterxp purple p", shell=True)
        def lilac():
            subprocess.Popen("metterxp lilac p", shell=True)
        def pink():
            subprocess.Popen("metterxp pink p", shell=True)
            
        cwindow=Tk(className="MetterXP")
        cwindow.config(background=bg)
        cwindow.resizable(0, 0)
        cparent = Frame(cwindow)
        cparent.pack(expand=1)
        cwindow.geometry("483x483")
        if os.path.isfile(en):
            cwindow.title("Simple Color Themes - Settings | MetterXP")
            ctext1=Label(cparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Please select a theme.")
            cspace1=Label(cparent, background=bg, foreground=fg, font="arial 3", text="\n")
            cbutton1=Button(cparent, text="Black (Dark)", command=black, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton2=Button(cparent, text="White (White)", command=white, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton3=Button(cparent, text="Gray", command=gray, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton4=Button(cparent, text="Red", command=red, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton5=Button(cparent, text="Yellow", command=yellow, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton6=Button(cparent, text="Green", command=green, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton7=Button(cparent, text="Blue", command=blue, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton8=Button(cparent, text="Navy Blue", command=navy, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton9=Button(cparent, text="Purple", command=purple, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton10=Button(cparent, text="Lilac", command=lilac, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton11=Button(cparent, text="Pink", command=pink, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
        elif os.path.isfile(tr):
            cwindow.title("Basit Renk Temaları - Ayarlar | MetterXP")
            ctext1=Label(cparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Lütfen bir tema seçin.")
            cspace1=Label(cparent, background=bg, foreground=fg, font="arial 3", text="\n")
            cbutton1=Button(cparent, text="Siyah (Koyu)", command=black, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton2=Button(cparent, text="Beyaz (Açık)", command=white, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
            cbutton3=Button(cparent, text="Gri", command=gray, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="3")
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
        def complex_atno():
            subprocess.Popen("metterxp complex_atno p", shell=True)
        
        pwindow=Tk(className="MetterXP")
        pwindow.config(background=bg)
        pwindow.resizable(0, 0)
        pparent = Frame(pwindow)
        pparent.pack(expand=1)
        pwindow.geometry("400x600")
        if os.path.isfile(en):
            pwindow.title("Themes From People - Settings | MetterXP")
            ptext1=Label(pparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Please select a theme.")
            pspace1=Label(pparent, background=bg, foreground=fg, font="arial 3", text="\n")
            pbutton1=Button(pparent, text="atno's complex theme", command=complex_atno, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")
        elif os.path.isfile(tr):
            pwindow.title("İnsanlardan Temalar - Ayarlar | MetterXP")
            ptext1=Label(pparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Lütfen bir tema seçin.")
            pspace1=Label(pparent, background=bg, foreground=fg, font="arial 3", text="\n")
            pbutton1=Button(pparent, text="atno'nun karmaşık teması", command=complex_atno, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")
        ptext1.pack(fill="x")
        pspace1.pack(fill="x")
        pbutton1.pack(fill="x")
    
    
    def ct():
        def ue():
            if os.path.isfile(en):
                messagebox.showerror("User Error","You didn't select color.")
            elif os.path.isfile(tr):
                messagebox.showerror("Kullanıcı Hatası","Renk seçmediniz.")
        def run():
            if e1.get() != None and e2.get() != None and e3.get() != None and e4.get() != None and e5.get() != None and e6.get() != None:
                r1=e1.get().replace('#','')
                r2=e2.get().replace('#','')
                r3=e3.get().replace('#','')
                r4=e4.get().replace('#','')
                r5=e5.get().replace('#','')
                r6=e6.get().replace('#','')
                subprocess.Popen("metterxp ct p "+r1+" "+r2+" "+r3+" "+r4+" "+r5+" "+r6, shell=True)
            else:
                ue()
        def s1():
            global v1
            v1 = askcolor(title="")
            if v1 != None:
                b1.config(background=v1[1])
                e1.delete(0, END)
                e1.insert(0, v1[1])
            elif v1 == None:
                ue()
                return
        def s2():
            global v2
            v2 = askcolor(title="")
            if v2 != None:
                b2.config(background=v2[1])
                e2.delete(0, END)
                e2.insert(0, v2[1])
            elif v2 == None:
                ue()
                return
        def s3():
            global v3
            v3 = askcolor(title="")
            if v3 != None:
                b3.config(background=v3[1])
                e3.delete(0, END)
                e3.insert(0, v3[1])
            elif v3 == None:
                ue()
                return
        def s4():
            global v4
            v4 = askcolor(title="")
            if v4 != None:
                b4.config(background=v4[1])
                e4.delete(0, END)
                e4.insert(0, v4[1])
            elif v4 == None:
                ue()
                return
        def s5():
            global v5
            v5 = askcolor(title="")
            if v5 != None:
                b5.config(background=v5[1])
                e5.delete(0, END)
                e5.insert(0, v5[1])
            elif v5 == None:
                ue()
                return
        def s6():
            global v6
            v6 = askcolor(title="")
            if v6 != None:
                b6.config(background=v6[1])
                e6.delete(0, END)
                e6.insert(0, v6[1])
            elif v6 == None:
                ue()
                return 
        ctwindow=Tk(className="MetterXP")
        ctwindow.config(background=bg)
        ctwindow.resizable(0, 0)
        ctparent = Frame(ctwindow, background=bg)
        ctparent.pack(expand=1)
        ctwindow.geometry("512x512")
        e1=Entry(ctparent)
        e2=Entry(ctparent)
        e3=Entry(ctparent)
        e4=Entry(ctparent)
        e5=Entry(ctparent)
        e6=Entry(ctparent)
        if os.path.isfile(en):
            ctwindow.title("Customizing theme - Settings | MetterXP")
            b1=Button(ctparent, text="Choose color of\nwindow", command=s1, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="2")
            b2=Button(ctparent, text="Choose color of\ntext in window", command=s2, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="2")
            b3=Button(ctparent, text="Choose color of\nbuttons", command=s3, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="2")
            b4=Button(ctparent, text="Choose color of\ntext on buttons", command=s4, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="2")
            b5=Button(ctparent, text="Choose color of\nbutton when cursor is on the button", command=s5, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="2")
            b6=Button(ctparent, text="Choose color of\ntext on button when bursor is on button", command=s6, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="2")
            b7=Button(ctparent, text="Run", command=run, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="2")
        elif os.path.isfile(tr):
            ctwindow.title("Tema özelleştirme - Ayarlar | MetterXP")
            b1=Button(ctparent, text="Pencerenin\nrengini reçin", command=s1, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="2")
            b2=Button(ctparent, text="Penceredeki yazıların\nrengini seçin", command=s2, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="2")
            b3=Button(ctparent, text="Butonların\nrengini seçin", command=s3, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="2")
            b4=Button(ctparent, text="Butonlardaki yazıların\nrengini seçin", command=s4, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="2")
            b5=Button(ctparent, text="İmleç butonda olduğundaki\nrengini seçin", command=s5, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="2")
            b6=Button(ctparent, text="İmleç butonda olduğundaki yazı\nrengini seçin", command=s6, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="2")
            b7=Button(ctparent, text="Çalıştır", command=run, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="8")            
        b1.grid(row=0, column=0)
        e1.grid(row=0, column=1)
        b2.grid(row=1, column=0)
        e2.grid(row=1, column=1)
        b3.grid(row=2, column=0)
        e3.grid(row=2, column=1)
        b4.grid(row=3, column=0)
        e4.grid(row=3, column=1)
        b5.grid(row=4, column=0)
        e5.grid(row=4, column=1)
        b6.grid(row=5, column=0)
        e6.grid(row=5, column=1)
        b7.grid(row=6, columnspan=2)        
        
    if os.path.isfile(en):
        swindow.title("Settings | MetterXP")
        stext1=Label(sparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Please select a theme category.")
        sspace1=Label(sparent, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton1=Button(sparent, text="From developer [MuKonqi (Muhammed Abdurrahman)]", command=mukonqi, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="7")
        sbutton2=Button(sparent, text="Simple color themes", command=colors, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="7")
        sbutton3=Button(sparent, text="From people", command=people, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="7")
        sbutton4=Button(sparent, text="Customize", command=ct, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="7")
        sspace2=Label(sparent, background=bg, foreground=fg, font="arial 3", text="\n\n")
        stext2=Label(sparent, background=bg, foreground=fg, font="arial 11 bold italic", text="You can change your language preferences below.")
        sspace3=Label(sparent, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton5=Button(sparent, text="English (English)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="7")
        sbutton6=Button(sparent, text="Turkish (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="7")
    elif os.path.isfile(tr):
        swindow.title("Ayarlar | MetterXP")
        stext1=Label(sparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Lütfen bir tema kategorisi seçiniz.")
        sspace1=Label(sparent, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton1=Button(sparent, text="Geliştiriciden [MuKonqi (Muhammed Abdurrahman)]", command=mukonqi, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font="arial 11 bold", cursor="hand2", borderwidth="7")
        sbutton2=Button(sparent, text="Basit renk temaları", command=colors, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="7")
        sbutton3=Button(sparent, text="İnsanlardan", command=people, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font="arial 11 bold", cursor="hand2", borderwidth="7")
        sbutton4=Button(sparent, text="Özelleştir", command=ct, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="7")
        sspace2=Label(sparent, background=bg, foreground=fg, font="arial 3", text="\n\n")
        stext2=Label(sparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Aşağıdan dil tercihlerinizi değiştirebilirsiniz.")
        sspace3=Label(sparent, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton5=Button(sparent, text="English (İngilizce)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font="arial 11 bold", cursor="hand2", borderwidth="7")
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
        if not os.path.isdir("/home/"+username+"/.by-mukonqi/"):
            os.system("cd /home/"+username+"/ ; mkdir .by-mukonqi ; cd .by-mukonqi ; mkdir metterxp ; mkdir metterxp/language")
        elif not os.path.isdir("/home/"+username+"/.by-mukonqi/metterxp"):
            os.system("cd /home/"+username+"/.by-mukonqi ; mkdir metterxp ; mkdir metterxp/language")
        elif not os.path.isdir("/home/"+username+"/.by-mukonqi/metterxp/language/"):
            os.system("cd /home/"+username+"/.by-mukonqi/metterxp ; mkdir language")
        messagebox.showinfo("Information","English language applied! When you click 'OK', MetterXP settings will open.")
        lwindow.destroy()
        main()
    def llangtr():
        if not os.path.isdir("/home/"+username+"/.by-mukonqi/"):
            os.system("cd /home/"+username+"/ ; mkdir .by-mukonqi ; cd .by-mukonqi ; mkdir metterxp ; mkdir metterxp/language")
        elif not os.path.isdir("/home/"+username+"/.by-mukonqi/metterxp"):
            os.system("cd /home/"+username+"/.by-mukonqi ; mkdir metterxp ; mkdir metterxp/language")
        elif not os.path.isdir("/home/"+username+"/.by-mukonqi/metterxp/language/"):
            os.system("cd /home/"+username+"/.by-mukonqi/metterxp ; mkdir language")
        os.system("cd /home/"+username+"/.by-mukonqi/metterxp/language ; touch tr.txt")
        messagebox.showinfo("Bilgilendirme","İstenilen dil uygulandı! 'OK' tuşuna bastığınızda MetterXP ayarları açılacak.")
        lwindow.destroy()
        main()
    lwindow=Tk(className="MetterXP")
    lwindow.title("First Start of MetterXP")
    lwindow.config(background=bg)
    lparent = Frame(lwindow)
    lparent.pack(expand=1)
    lwindow.geometry("322x161")
    icon = PhotoImage(file="/usr/local/bin/metterxp/icon.png")
    lwindow.iconphoto(True, icon)
    ltext1=Label(lparent, background=bg, foreground=fg, font="arial 11 bold italic", text="Please choose a language for MetterXP.\nMetterXP için lütfen bir dil seçin.")
    ltext1.pack(fill="x")
    lspace1=Label(lparent, background=bg, foreground=fg, font="arial 3", text="\n")
    lspace1.pack(fill="x")
    lbutton1=Button(lparent, text="English (İngilizce)", command=llangen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font="arial 11 bold", cursor="hand2", borderwidth="4")
    lbutton1.pack(fill="x")
    lbutton2=Button(lparent, text="Türkçe (Turkish)", command=llangtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11 bold", cursor="hand2", borderwidth="4")
    lbutton2.pack(fill="x")
    mainloop()

if not os.path.isdir("/home/"+username+"/.by-mukonqi/"):
    first_start()
    exit()
elif not os.path.isdir("/home/"+username+"/.by-mukonqi/metterxp"):
    first_start()
    exit()
elif not os.path.isdir("/home/"+username+"/.by-mukonqi/metterxp/language/"):
    os.system("cd /home/"+username+"/.by-mukonqi/metterxp ; mkdir language")
    first_start()
    exit()
elif not os.path.isfile("/home/"+username+"/.by-mukonqi/metterxp/language/en.txt") and not os.path.isfile("/home/"+username+"/.by-mukonqi/metterxp/language/tr.txt"):
    first_start()
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
    gfs=1
    if os.path.isfile(en):
        messagebox.showwarning("Warning","Can't found theme configuration. When you click 'OK' settings will open.")
    elif os.path.isfile(tr):
        messagebox.showwarning("Uyarı","Tema yapılandırması bulunamadı. Ayarlar 'OK' tuşuna bastığınızda açılacaktır.")
    main()
    exit()

main()