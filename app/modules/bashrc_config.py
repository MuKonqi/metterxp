#!/usr/bin/env python3

# Copyright (C) 2022, 2023 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os
import getpass
username=getpass.getuser()
t="/home/"+username+"/.by-mukonqi/metterxp/theme/"
en="/home/"+username+"/.by-mukonqi/metterxp/language/en.txt"
tr="/home/"+username+"/.by-mukonqi/metterxp/language/tr.txt"
debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if not os.path.isdir("/home/"+username+"/.by-mukonqi/metterxp/"):
    os.system("python3 /usr/local/bin/metterxp/modules/mxp_options.py")
    exit()

if os.getuid() == 0:
    if os.path.isfile(en):
        messagebox.showerror("Error","Root can't run this module!")
    elif os.path.isfile(tr):
        messagebox.showerror("Hata","Kök kullanıcı bu modülü çalıştıramaz!")
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
    os.system("python3 /usr/local/bin/metterxp/modules/mxp_options.py")
    exit()
        

window=Tk(className="MetterXP")
if os.path.isfile(en):
    window.title("Configure .bashrc file | MetterXP")
elif os.path.isfile(tr):
    window.title(".bashrc dosyasını yapılandır | MetterXP")
window.config(background=bg)
window.resizable(0, 0)
window.geometry("571x571")
icon = PhotoImage(file="/usr/local/bin/metterxp/icon.png")
window.iconphoto(True, icon)
parent = Frame(window)
parent.pack(expand=1)

def bash():
    def main():
        cmd2=" touch /home/"+username+"/.bashrc-boot.bak ;  cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc-boot.bak"             
        os.system(cmd2)
        if not os.path.isfile("/home/"+username+"/.bashrc-first.bak"):
            cmd3=" touch /home/"+username+"/.bashrc-first.bak ;  cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc-first.bak"
            os.system(cmd3)   
        
        def nocolor():
            cmd1=" touch /home/"+username+"/.bashrc.bak ;  cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+username+"/.bashrc"
            os.system(cmd_0)
            if os.path.isfile(en):
                cmd_1=" echo 'echo Hello "+username+"!' >> /home/"+username+"/.bashrc"
                os.system(cmd_1)
                messagebox.showinfo("Information","Successful! Configuration completed.")
            elif os.path.isfile(tr):
                cmd_1=" echo 'echo Merhabalar "+username+"!' >> /home/"+username+"/.bashrc"
                os.system(cmd_1)
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
        def withcolor():
            cmd1=" touch /home/"+username+"/.bashrc.bak ;  cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+username+"/.bashrc"
            os.system(cmd_0)
            if os.path.isfile("/usr/bin/lolcat") or os.path.isfile("/bin/lolcat"):
                pass
            else:
                if os.path.isfile(debian):
                    os.system(" apt install lolcat -y")
                elif os.path.isfile(fedora):
                    os.system(" dnf install lolcat -y")
                elif os.path.isfile(solus):
                    os.system(" eopkg install lolcat -y")
            if os.path.isfile(en):
                cmd_1=" echo 'echo Hello "+username+"! | lolcat' >> /home/"+username+"/.bashrc"
                os.system(cmd_1)
                messagebox.showinfo("Information","Successful! Configuration completed.")
            elif os.path.isfile(tr):
                cmd_1=" echo 'echo Merhabalar "+username+"! | lolcat' >> /home/"+username+"/.bashrc"
                os.system(cmd_1)
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
        def yasfetch():
            cmd1=" touch /home/"+username+"/.bashrc.bak ;  cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+username+"/.bashrc"
            os.system(cmd_0)
            if not os.path.isfile("/usr/bin/yasfetch"):
                os.system("pkexec /usr/bin/metterxp install_yasfetch")
            cmd_3=" echo 'yasfetch' >> /home/"+username+"/.bashrc"
            os.system(cmd_3)
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Configuration completed.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
        def yasfetchwithcolor():
            cmd1=" touch /home/"+username+"/.bashrc.bak ;  cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+username+"/.bashrc"
            os.system(cmd_0)
            if os.path.isfile("/usr/bin/lolcat") or os.path.isfile("/bin/lolcat"):
                pass
            else:
                if os.path.isfile(debian):
                    os.system(" apt install lolcat -y")
                elif os.path.isfile(fedora):
                    os.system(" dnf install lolcat -y")
                elif os.path.isfile(solus):
                    os.system(" eopkg install lolcat -y")
            if not os.path.isfile("/usr/bin/yasfetch"):
                os.system("pkexec /usr/bin/metterxp install_yasfetch")
            cmd_4=" echo 'yasfetch | lolcat' >> /home/"+username+"/.bashrc"
            os.system(cmd_4)
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Configuration completed.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
        def memory():
            cmd1=" touch /home/"+username+"/.bashrc.bak ;  cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+username+"/.bashrc"
            os.system(cmd_0)
            cmd_5=" echo 'free -m' >> /home/"+username+"/.bashrc"
            os.system(cmd_5)
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Configuration completed.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
        def memorywithcolor():
            cmd1=" touch /home/"+username+"/.bashrc.bak ;  cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+username+"/.bashrc"
            os.system(cmd_0)
            cmd_5=" echo 'free -m | lolcat' >> /home/"+username+"/.bashrc"
            os.system(cmd_5)
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Configuration completed.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")          
        def root():
            cmd1=" touch /home/"+username+"/.bashrc.bak ;  cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+username+"/.bashrc"
            os.system(cmd_0)
            cmd_6=" echo ' su' >> /home/"+username+"/.bashrc"
            os.system(cmd_6)
            if os.path.isfile(en):
                messagebox.showinfo("Information","Successful! Configuration completed.")
            elif os.path.isfile(tr):
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")

        def reset():
            window2=Tk(className="MetterXP")
            window2.config(background=bg)
            window2.resizable(0, 0)
            parent2 = Frame(window2)
            window2.geometry("365x210")
            parent2.pack(expand=1)
            if os.path.isfile(en):
                window2.title("Reset options for .bashrc file | MetterXP")
                text3=Label(parent2, background=bg, foreground=fg, font="arial 11 bold italic", text="Choose a reset option below.")                
            elif os.path.isfile(tr):
                window2.title(".bashrc dosyası için sıfırlama seçenekleri | MetterXP")
                text3=Label(parent2, background=bg, foreground=fg, font="arial 11 bold italic", text="Aşağıdan bir sıfırlama seçeneği seçiniz.")
            bashspace3=Label(parent2, background=bg, foreground=fg, text="\n", font="arial 3")
            text3.pack(fill="x")
            bashspace3.pack(fill="x")
            def takeitbackbash():
                _cmd1=" cp /home/"+username+"/.bashrc.bak /home/"+username+"/.bashrc"
                os.system(_cmd1)
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Successful! Last change is undone.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Son değişiklik başarıyla geri alındı.")
            def initialstatebash():
                _cmd2=" cp /usr/local/bin/metterxp/.bashrc.bak /home/"+username+"/.bashrc"
                os.system(_cmd2)
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Successful! All changes are undone.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Tüm değişiklikler başarıyla geri alındı.")
            def firststatebash():
                _cmd3=" cp /usr/local/bin/metterxp/.bashrc-first.bak /home/"+username+"/.bashrc"
                os.system(_cmd3)
                if os.path.isfile(en):
                    messagebox.showinfo("Information","Successful! All changes are undone.")
                elif os.path.isfile(tr):
                    messagebox.showinfo("Bilgilendirme","Tüm değişiklikler başarıyla geri alındı.")
            if os.path.isfile(en):
                bashbutton1=Button(parent2, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Undo last change in .bashrc file", command=takeitbackbash)
                bashbutton2=Button(parent2, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Undo all changes to the .bashrc file made\nat the current startup of MetterXP", command=initialstatebash)
                bashbutton3=Button(parent2, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Undo all changes to the bashrc file made\nat the first startup of MetterXP", command=firststatebash)
            elif os.path.isfile(tr):
                bashbutton1=Button(parent2, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text=".bashrc dosyasındaki son değişikliği geri al", command=takeitbackbash)
                bashbutton2=Button(parent2, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Şuanki MetterXP açılışında yapılan\n.bashrc dosyasındaki tüm değişiklikleri geri al", command=initialstatebash)
                bashbutton3=Button(parent2, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="İlk MetterXP açılışında yapılan\n.bashrc dosyasındaki tüm değişiklikleri geri al", command=firststatebash)                
            bashspace1=Label(parent, background=bg, foreground=fg, font="arial 2", text="\n")
            bashbutton1.pack(fill="x")
            bashbutton2.pack(fill="x")
            bashbutton3.pack(fill="x")
            bashspace1.pack(fill="x")

        if os.path.isfile(en):
            text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text="How would you like to configure the .bashrc file?\nNote: In the configuration options, the order of clicking the options is important.\nYour current username: "+username)
            bashbutton1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Add my username without color", command=nocolor)
            bashbutton2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Add my username with color\n(with the help of lolcat)", command=withcolor)
            bashbutton3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Add system info with low color\n(with the help of yasfetch)", command=yasfetch)
            bashbutton4=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Add system info with colorful\n(with the help of yasfetch and lolcat)", command=yasfetchwithcolor)
            bashbutton5=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Add memory consumption without color", command=memory)
            bashbutton6=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Add memory consumption with color", command=memorywithcolor)
            bashbutton7=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Bash (you can think of it as terminal)\nask for root password on start", command=root)
            bashbutton8=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Reset options for .bashrc file", command=reset)
        elif os.path.isfile(tr):
            text1=Label(parent, background=bg, foreground=fg, font="arial 11 bold italic", text=".bashrc dosyasını nasıl yapılandırmak istersiniz?\nNot: Yapılandırma seçeneklerinde, seçeneklerin tıklanma sırası önemlidir.\nMevcut kullanıcı adınız: "+username)
            bashbutton1=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Kullanıcı adımı renksiz bir şekilde ekle", command=nocolor)
            bashbutton2=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Kullanıcı adımı renkli bir şekilde ekle\n(lolcat yardımıyla)", command=withcolor)
            bashbutton3=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Sistem bilgisini az renkli bir şekilde ekle\n(yasfetch yardımıyla)", command=yasfetch)
            bashbutton4=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Sistem bilgisini rengarenk bir şekilde ekle\n(yasfetch ve lolcat yardımıyla)", command=yasfetchwithcolor)
            bashbutton5=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Ram tüketimini renksiz bir şekilde ekle", command=memory)
            bashbutton6=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Ram tüketimini renkli bir şekilde ekle", command=memorywithcolor)
            bashbutton7=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text="Bash (terminal diye düşünebilirsiniz)\nbaşlatıldığında kök şifresini sor", command=root)
            bashbutton8=Button(parent, font="arial 11 bold", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="10", text=".bashrc dosyası için sıfırlama seçenekleri", command=reset)
        text1.pack(fill="x")
        bashbutton1.pack(fill="x")
        bashbutton2.pack(fill="x")
        bashbutton3.pack(fill="x")
        bashbutton4.pack(fill="x")
        bashbutton5.pack(fill="x")
        bashbutton6.pack(fill="x")
        bashbutton7.pack(fill="x")
        bashbutton8.pack(fill="x")
    main()
bash()
mainloop()