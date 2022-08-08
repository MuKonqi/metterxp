#!/usr/bin/env python3

# Copyright (C) 2022 MuKonqi (Muhammed Abdurrahman)

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os
import getpass


debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
lang_tr="/usr/local/bin/metterxp/settings/lang/tr.txt"
lang_en="/usr/local/bin/metterxp/settings/lang/en.txt"
username=getpass.getuser()


def module_exit():
    exit("\nThis module is shutting down...\nModül kapatılıyor...")
def reopen():
    print("\nModül yeniden başlatılıyor...\nRestarting this module")
    window.destroy()
    os.system("pkexec /usr/bin/metterxp bashrc_config")

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
    window.title("Configre .bashrc file | MetterXP")
elif os.path.isfile(lang_tr):
    window.title(".bashrc dosyasını yapılandır | MetterXP")
window.config(background=bg)
window.resizable(0, 0)

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
            if os.path.isfile(lang_en):
                cmd_1=" echo 'echo Hello "+username+"!' >> /home/"+username+"/.bashrc"
                os.system(cmd_1)
                messagebox.showinfo("Information","Successful! Configuration completed.")
            elif os.path.isfile(lang_tr):
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
            if os.path.isfile(lang_en):
                cmd_1=" echo 'echo Hello "+username+"! | lolcat' >> /home/"+username+"/.bashrc"
                os.system(cmd_1)
                messagebox.showinfo("Information","Successful! Configuration completed.")
            elif os.path.isfile(lang_tr):
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
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Configuration completed.")
            elif os.path.isfile(lang_tr):
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
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Configuration completed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
        def memory():
            cmd1=" touch /home/"+username+"/.bashrc.bak ;  cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+username+"/.bashrc"
            os.system(cmd_0)
            cmd_5=" echo 'free -m' >> /home/"+username+"/.bashrc"
            os.system(cmd_5)
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Configuration completed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
        def memorywithcolor():
            cmd1=" touch /home/"+username+"/.bashrc.bak ;  cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+username+"/.bashrc"
            os.system(cmd_0)
            cmd_5=" echo 'free -m | lolcat' >> /home/"+username+"/.bashrc"
            os.system(cmd_5)
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Configuration completed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")          
        def root():
            cmd1=" touch /home/"+username+"/.bashrc.bak ;  cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+username+"/.bashrc"
            os.system(cmd_0)
            cmd_6=" echo ' su' >> /home/"+username+"/.bashrc"
            os.system(cmd_6)
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Successful! Configuration completed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")

        def reset():
            def window_close():
                window2.destroy()
            window2=Tk()
            window2.config(background=bg)
            window2.resizable(0, 0)
            if os.path.isfile(lang_en):
                window2.title("Reset options for .bashrc file | MetterXP")
                text3=Label(window2, background=bg, foreground=fg, font="arial 10 bold", text="Choose a reset option below.")                
            elif os.path.isfile(lang_tr):
                window2.title(".bashrc dosyası için sıfırlama seçenekleri | MetterXP")
                text3=Label(window2, background=bg, foreground=fg, font="arial 10 bold", text="Aşağıdan bir sıfırlama seçeneği seçiniz.")
            bashspace3=Label(window2, background=bg, foreground=fg, text="\n", font="arial 3")
            text3.pack()
            bashspace3.pack()
            def takeitbackbash():
                _cmd1=" cp /home/"+username+"/.bashrc.bak /home/"+username+"/.bashrc"
                os.system(_cmd1)
                if os.path.isfile(lang_en):
                    messagebox.showinfo("Information","Successful! Last change is undone.")
                elif os.path.isfile(lang_tr):
                    messagebox.showinfo("Bilgilendirme","Son değişiklik başarıyla geri alındı.")
            def initialstatebash():
                _cmd2=" cp /usr/local/bin/metterxp/.bashrc.bak /home/"+username+"/.bashrc"
                os.system(_cmd2)
                if os.path.isfile(lang_en):
                    messagebox.showinfo("Information","Successful! All changes are undone.")
                elif os.path.isfile(lang_tr):
                    messagebox.showinfo("Bilgilendirme","Tüm değişiklikler başarıyla geri alındı.")
            def firststatebash():
                _cmd3=" cp /usr/local/bin/metterxp/.bashrc-first.bak /home/"+username+"/.bashrc"
                os.system(_cmd3)
                if os.path.isfile(lang_en):
                    messagebox.showinfo("Information","Successful! All changes are undone.")
                elif os.path.isfile(lang_tr):
                    messagebox.showinfo("Bilgilendirme","Tüm değişiklikler başarıyla geri alındı.")
            if os.path.isfile(lang_en):
                text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="How would you like to configure the .bashrc file?\nNote: In the configuration options, the order of clicking the options is important.\nYour current username: "+username)
                bashbutton1=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Undo last change in .bashrc file", command=takeitbackbash)
                bashbutton2=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Undo all changes to the .bashrc file made\nat the current startup of MetterXP", command=initialstatebash)
                bashbutton3=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Undo all changes to the bashrc file made\nat the first startup of MetterXP", command=firststatebash)
                bashspace4=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
                bashbutton_2=Button(window2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close window\nBack to menu", command=window_close)
            elif os.path.isfile(lang_tr):
                text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text=".bashrc dosyasını nasıl yapılandırmak istersiniz?\nNot: Yapılandırma seçeneklerinde, seçeneklerin tıklanma sırası önemlidir.\nMevcut kullanıcı adınız: "+username)
                bashbutton1=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text=".bashrc dosyasındaki son değişikliği geri al", command=takeitbackbash)
                bashbutton2=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Şuanki MetterXP açılışında yapılan\n.bashrc dosyasındaki tüm değişiklikleri geri al", command=initialstatebash)
                bashbutton3=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="İlk MetterXP açılışında yapılan\n.bashrc dosyasındaki tüm değişiklikleri geri al", command=firststatebash)                
                bashspace4=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
                bashbutton_2=Button(window2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Pencereyi kapat\nMenüye dön", command=window_close)
            bashspace1=Label(window, background=bg, foreground=fg, font="arial 2", text="\n")
            text1.pack()
            bashbutton1.pack()
            bashbutton2.pack()
            bashbutton3.pack()
            bashspace4.pack()
            bashbutton_2.pack()
            bashspace1.pack()

        if os.path.isfile(lang_en):
            bashbutton1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Add my username without color", command=nocolor)
            bashbutton2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Add my username with color\n(with the help of lolcat)", command=withcolor)
            bashbutton3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Add system info with low color\n(with the help of yasfetch)", command=yasfetch)
            bashbutton4=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Add system info with colorful\n(with the help of yasfetch and lolcat)", command=yasfetchwithcolor)
            bashbutton5=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Add memory consumption without color", command=memory)
            bashbutton6=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Add memory consumption with color", command=memorywithcolor)
            bashbutton7=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Bash (you can think of it as terminal)\nask for root password on start", command=root)
            bashbutton8=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Reset options for .bashrc file", command=reset)
            bashspace2=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
            bashbutton_1=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close window\nBack to menu", command=module_exit)
        elif os.path.isfile(lang_tr):
            bashbutton1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Kullanıcı adımı renksiz bir şekilde ekle", command=nocolor)
            bashbutton2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Kullanıcı adımı renkli bir şekilde ekle\n(lolcat yardımıyla)", command=withcolor)
            bashbutton3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Sistem bilgisini az renkli bir şekilde ekle\n(yasfetch yardımıyla)", command=yasfetch)
            bashbutton4=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Sistem bilgisini rengarenk bir şekilde ekle\n(yasfetch ve lolcat yardımıyla)", command=yasfetchwithcolor)
            bashbutton5=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Ram tüketimini renksiz bir şekilde ekle", command=memory)
            bashbutton6=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Ram tüketimini renkli bir şekilde ekle", command=memorywithcolor)
            bashbutton7=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Bash (terminal diye düşünebilirsiniz)\nbaşlatıldığında kök şifresini sor", command=root)
            bashbutton8=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text=".bashrc dosyası için sıfırlama seçenekleri", command=reset)
            bashspace2=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
            bashbutton_1=Button(window, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Pencereyi kapat\nMenüye dön", command=module_exit)
        bashbutton1.pack()
        bashbutton2.pack()
        bashbutton3.pack()
        bashbutton4.pack()
        bashbutton5.pack()
        bashbutton6.pack()
        bashbutton7.pack()
        bashbutton8.pack()
        bashspace2.pack()
        bashbutton_1.pack()
    main()
bash()
mainloop()