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
    print("\nModül yeniden başlatılıyor...\nRestarting this module")
    window.destroy()
    os.system("pkexec python3 /usr/local/bin/metterxp/modules/app_configre.py")
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
    window.title("Configre softwares | MetterXP")
elif os.path.isfile(lang_tr):
    window.title("Yazılımları yapılandır | MetterXP")
window.config(background=bg)
window.resizable(0, 0)

def bash():
    def windowclose():
        window2.destroy()
    window2=Tk()
    if os.path.isfile(lang_en):
        window2.title("Configre .bashrc file | MetterXP")
    elif os.path.isfile(lang_tr):
        window2.title(".bashrc dosyasını yapılandır | MetterXP")
    window2.config(background=bg)
    window2.resizable(0, 0)
    def main():
        get_my_user_name=my_user_name.get()
        str_my_user_name=str(get_my_user_name)
        cmd2=" touch /usr/local/bin/metterxp/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /usr/local/bin/metterxp/.bashrc.bak"             
        os.system(cmd2)
        if os.path.isfile("/usr/local/bin/metterxp/.bashrc-first.bak"):
            pass
        else:
            cmd3=" touch /usr/local/bin/metterxp/.bashrc-first.bak ;  cp /home/"+str_my_user_name+"/.bashrc /usr/local/bin/metterxp/.bashrc-first.bak"
            os.system(cmd3)   
        my_user_name.destroy()
        b_1_bash.destroy()
        space4.destroy()
        button_1.destroy()
        if os.path.isfile(lang_en):
            text2.config(text="How would you like to configure the .bashrc file?\nNote: In the configuration options, the order of clicking the options is important.\nYour current username: "+str_my_user_name)
        elif os.path.isfile(lang_tr):
            text2.config(text=".bashrc dosyasını nasıl yapılandırmak istersiniz?\nNot: Yapılandırma seçeneklerinde, seçeneklerin tıklanma sırası önemlidir.\nMevcut kullanıcı adınız: "+str_my_user_name)
        def nocolor():
            cmd1=" touch /home/"+str_my_user_name+"/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /home/"+str_my_user_name+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+str_my_user_name+"/.bashrc"
            os.system(cmd_0)
            if os.path.isfile(lang_en):
                cmd_1=" echo 'echo Hello "+str_my_user_name+"!' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_1)
                messagebox.showinfo("Information","Succesful! Configuration completed.")
            elif os.path.isfile(lang_tr):
                cmd_1=" echo 'echo Merhabalar "+str_my_user_name+"!' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_1)
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
        def withcolor():
            cmd1=" touch /home/"+str_my_user_name+"/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /home/"+str_my_user_name+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+str_my_user_name+"/.bashrc"
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
                cmd_1=" echo 'echo Hello "+str_my_user_name+"! | lolcat' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_1)
                messagebox.showinfo("Information","Succesful! Configuration completed.")
            elif os.path.isfile(lang_tr):
                cmd_1=" echo 'echo Merhabalar "+str_my_user_name+"! | lolcat' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_1)
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
        def neofetch():
            cmd1=" touch /home/"+str_my_user_name+"/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /home/"+str_my_user_name+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+str_my_user_name+"/.bashrc"
            os.system(cmd_0)
            if os.path.isfile("/usr/bin/neofetch") or os.path.isfile("/bin/neofetch"):
                pass
            else:
                if os.path.isfile(debian):
                    os.system(" apt install neofetch -y")
                elif os.path.isfile(fedora):
                    os.system(" dnf install neofetch -y")
                elif os.path.isfile(solus):
                    os.system(" eopkg install neofetch -y")
            cmd_3=" echo 'neofetch' >> /home/"+str_my_user_name+"/.bashrc"
            os.system(cmd_3)
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succesful! Configuration completed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
        def neofetchwithcolor():
            cmd1=" touch /home/"+str_my_user_name+"/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /home/"+str_my_user_name+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+str_my_user_name+"/.bashrc"
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
            if os.path.isfile("/usr/bin/neofetch") or os.path.isfile("/bin/neofetch"):
                pass
            else:
                if os.path.isfile(debian):
                    os.system(" apt install neofetch -y")
                elif os.path.isfile(fedora):
                    os.system(" dnf install neofetch -y")
                elif os.path.isfile(solus):
                    os.system(" eopkg install neofetch -y")
            cmd_4=" echo 'neofetch | lolcat' >> /home/"+str_my_user_name+"/.bashrc"
            os.system(cmd_4)
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succesful! Configuration completed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
        def memory():
            cmd1=" touch /home/"+str_my_user_name+"/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /home/"+str_my_user_name+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+str_my_user_name+"/.bashrc"
            os.system(cmd_0)
            cmd_5=" echo 'free -m' >> /home/"+str_my_user_name+"/.bashrc"
            os.system(cmd_5)
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succesful! Configuration completed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
        def memorywithcolor():
            cmd1=" touch /home/"+str_my_user_name+"/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /home/"+str_my_user_name+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+str_my_user_name+"/.bashrc"
            os.system(cmd_0)
            cmd_5=" echo 'free -m | lolcat' >> /home/"+str_my_user_name+"/.bashrc"
            os.system(cmd_5)
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succesful! Configuration completed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")          
        def kok():
            cmd1=" touch /home/"+str_my_user_name+"/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /home/"+str_my_user_name+"/.bashrc.bak"
            os.system(cmd1)
            cmd_0=" echo '   ' >> /home/"+str_my_user_name+"/.bashrc"
            os.system(cmd_0)
            cmd_6=" echo ' su' >> /home/"+str_my_user_name+"/.bashrc"
            os.system(cmd_6)
            if os.path.isfile(lang_en):
                messagebox.showinfo("Information","Succesful! Configuration completed.")
            elif os.path.isfile(lang_tr):
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
        def reset():
            def window_close():
                window3.destroy()
            window3=Tk()
            window3.config(background=bg)
            window3.resizable(0, 0)
            if os.path.isfile(lang_en):
                window3.title("Reset options for .bashrc file | MetterXP")
                text3=Label(window3, background=bg, foreground=fg, font="arial 10 bold", text="Choose a reset option below.")                
            elif os.path.isfile(lang_tr):
                window3.title(".bashrc dosyası için sıfırlama seçenekleri | MetterXP")
                text3=Label(window3, background=bg, foreground=fg, font="arial 10 bold", text="Aşağıdan bir sıfırlama seçeneği seçiniz.")
            bashspace3=Label(window3, background=bg, foreground=fg, text="\n", font="arial 3")
            text3.pack()
            bashspace3.pack()
            def takeitbackbash():
                _cmd1=" cp /home/"+str_my_user_name+"/.bashrc.bak /home/"+str_my_user_name+"/.bashrc"
                os.system(_cmd1)
                if os.path.isfile(lang_en):
                    messagebox.showinfo("Information","Succesful! Last change is undone.")
                elif os.path.isfile(lang_tr):
                    messagebox.showinfo("Bilgilendirme","Son değişiklik başarıyla geri alındı.")
            def initialstatebash():
                _cmd2=" cp /usr/local/bin/metterxp/.bashrc.bak /home/"+str_my_user_name+"/.bashrc"
                os.system(_cmd2)
                if os.path.isfile(lang_en):
                    messagebox.showinfo("Information","Succesful! All changes are undone.")
                elif os.path.isfile(lang_tr):
                    messagebox.showinfo("Bilgilendirme","Tüm değişiklikler başarıyla geri alındı.")
            def firststatebash():
                _cmd3=" cp /usr/local/bin/metterxp/.bashrc-first.bak /home/"+str_my_user_name+"/.bashrc"
                os.system(_cmd3)
                if os.path.isfile(lang_en):
                    messagebox.showinfo("Information","Succesful! All changes are undone.")
                elif os.path.isfile(lang_tr):
                    messagebox.showinfo("Bilgilendirme","Tüm değişiklikler başarıyla geri alındı.")
            if os.path.isfile(lang_en):
                bashbutton1=Button(window3, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Undo last change in .bashrc file", command=takeitbackbash)
                bashbutton2=Button(window3, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Undo all changes to the .bashrc file made\nat the current startup of MetterXP", command=initialstatebash)
                bashbutton3=Button(window3, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Undo all changes to the bashrc file made\nat the first startup of MetterXP", command=firststatebash)
                bashspace4=Label(window3, background=bg, foreground=fg, font="arial 3", text="\n")
                bashbutton_2=Button(window3, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close window\nBack to menu", command=window_close)
            elif os.path.isfile(lang_tr):
                bashbutton1=Button(window3, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text=".bashrc dosyasındaki son değişikliği geri al", command=takeitbackbash)
                bashbutton2=Button(window3, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Şuanki MetterXP açılışında yapılan\n.bashrc dosyasındaki tüm değişiklikleri geri al", command=initialstatebash)
                bashbutton3=Button(window3, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="İlk MetterXP açılışında yapılan\n.bashrc dosyasındaki tüm değişiklikleri geri al", command=firststatebash)                
                bashspace4=Label(window3, background=bg, foreground=fg, font="arial 3", text="\n")
                bashbutton_2=Button(window3, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Pencereyi kapat\nMenüye dön", command=window_close)
            bashspace1=Label(window2, background=bg, foreground=fg, font="arial 2", text="\n")
            bashbutton1.pack()
            bashbutton2.pack()
            bashbutton3.pack()
            bashspace4.pack()
            bashbutton_2.pack()
            bashspace1.pack()
        if os.path.isfile(lang_en):
            bashbutton1=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Add my username without color", command=nocolor)
            bashbutton2=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Add my username with color\n(with the help of lolcat)", command=withcolor)
            bashbutton3=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Add system info with low color\n(with the help of neofetch)", command=neofetch)
            bashbutton4=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Add system info with colorful\n(with the help of neofetch and lolcat)", command=neofetchwithcolor)
            bashbutton5=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Add memory consumption without color", command=memory)
            bashbutton6=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Add memory consumption with color", command=memorywithcolor)
            bashbutton7=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Bash (you can think of it as terminal)\nask for root password on start", command=kok)
            bashbutton8=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Reset options for .bashrc file", command=reset)
            bashspace2=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
            bashbutton_1=Button(window2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close window\nBack to menu", command=windowclose)
        elif os.path.isfile(lang_tr):
            bashbutton1=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Kullanıcı adımı renksiz bir şekilde ekle", command=nocolor)
            bashbutton2=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Kullanıcı adımı renkli bir şekilde ekle\n(lolcat yardımıyla)", command=withcolor)
            bashbutton3=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Sistem bilgisini az renkli bir şekilde ekle\n(neofetch yardımıyla)", command=neofetch)
            bashbutton4=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Sistem bilgisini rengarenk bir şekilde ekle\n(neofetch ve lolcat yardımıyla)", command=neofetchwithcolor)
            bashbutton5=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Ram tüketimini renksiz bir şekilde ekle", command=memory)
            bashbutton6=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Ram tüketimini renkli bir şekilde ekle", command=memorywithcolor)
            bashbutton7=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Bash (terminal diye düşünebilirsiniz)\nbaşlatıldığında kök şifresini sor", command=kok)
            bashbutton8=Button(window2, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text=".bashrc dosyası için sıfırlama seçenekleri", command=reset)
            bashspace2=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
            bashbutton_1=Button(window2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Pencereyi kapat\nMenüye dön", command=windowclose)
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
    if os.path.isfile(lang_en):
        text2=Label(window2, background=bg, foreground=fg, font="arial 10 bold", text="Enter your username below (this information will never be collected).")            
        space3=Label(window2, background=bg, foreground=fg, font="arial 2", text="\n")
        my_user_name=Entry(window2)
        b_1_bash=Button(window2,  cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Approve",command=main)
        space4=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
        button_1=Button(window2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close window\nBack to menu", command=windowclose)
    elif os.path.isfile(lang_tr):
        text2=Label(window2, background=bg, foreground=fg, font="arial 10 bold", text="Aşağıya kullanıcı adınızı giriniz (bu bilgi kesinlikle toplanmamaktadır).")            
        space3=Label(window2, background=bg, foreground=fg, font="arial 2", text="\n")
        my_user_name=Entry(window2)
        b_1_bash=Button(window2,  cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Onayla",command=main)
        space4=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
        button_1=Button(window2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Pencereyi kapat\nMenüye dön", command=windowclose)
    text2.pack()
    space3.pack()
    my_user_name.pack()
    b_1_bash.pack()
    space4.pack()
    button_1.pack()
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
        os.system(" x-www-browser localhost:631")
def cups():
    if os.path.isfile("/usr/bin/cups") or os.path.isfile("/bin/cups"):
        os.system(" x-www-browser localhost:631")
    else:
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
        os.system(" x-www-browser localhost:631")
    if os.path.isfile(lang_en):
        messagebox.showinfo("Information","Succesful! Cups configuration completed.")
    elif os.path.isfile(lang_tr):
        messagebox.showinfo("Bilgilendirme","Cups yapılandırması başarıyla tamamlandı.")
def wine():
    if os.path.isfile("/usr/bin/wine") or os.path.isfile("/bin/wine"):
        os.system(" winecfg")
    else:
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
        messagebox.showinfo("Information","Succesful! Wine configuration completed.")
    elif os.path.isfile(lang_tr):
        messagebox.showinfo("Bilgilendirme","Wine yapılandırması başarıyla tamamlandı.")
def pcrename():
    def windowclose():
        window2.destroy()
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
    window2=Tk()
    window2.config(background=bg)
    window2.resizable(0, 0)
    if os.path.isfile(lang_en):
        window2.title("Change this PC's name | MetterXP")
        text2=Label(window2, background=bg, foreground=fg, font="arial 10 bold", text="Enter a new name for your computer below.")
        space3=Label(window2, background=bg, foreground=fg, font="arial 2", text="\n")
        new_pc_name=Entry(window2)
        b_1_pcrename=Button(window2,  cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Save",command=addpcname)
        space4=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
        button_1=Button(window2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close window\nBack to menu", command=windowclose)
    elif os.path.isfile(lang_tr):
        window2.title("Bu bilgisayarın adını değiştir | MetterXP")
        text2=Label(window2, background=bg, foreground=fg, font="arial 10 bold", text="Aşağıya bilgisayarınız için yeni bir ad giriniz.")
        space3=Label(window2, background=bg, foreground=fg, font="arial 2", text="\n")
        new_pc_name=Entry(window2)
        b_1_pcrename=Button(window2,  cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Kaydet",command=addpcname)
        space4=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
        button_1=Button(window2, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Pencereyi kapat\nMenüye dön", command=windowclose)
    text2.pack()
    space3.pack()
    new_pc_name.pack()
    b_1_pcrename.pack()
    space4.pack()
    button_1.pack()
if os.path.isfile(lang_en):
    text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Please choose something.")
    space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    button1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Configure .bashrc file [Bash (you can think\nof it as a terminal) Configuration File]", command=bash)
    button2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Configure GRUB bootloader\n(with the help of Grub Customizer)", command=grub)
    button3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Configure Cups printer manager", command=cups)
    button4=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Configure Wine", command=wine)
    button5=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Change this PC's name", command=pcrename)
    space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    button_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close this module\nBack to main menu", command=module_exit)
elif os.path.isfile(lang_tr):
    text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Lütfen bir şey seçin.")
    space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    button1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text=".bashrc dosyasını [Bash (terminal olarak düşünebilirsiniz)\n Yapılandırma Dosyası] yapılandır", command=bash)
    button2=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="GRUB önyükleyiciyi yapılandır\n(Grub Customizer yardımıyla)", command=grub)
    button3=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Cups yazıcı yöneticisini yapılandır", command=cups)
    button4=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Wine'ı yapılandır", command=wine)
    button5=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Bu bilgisayarın adını değiştir", command=pcrename)
    space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    button_1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Modülü kapat\nAna menüye dön", command=module_exit)
text1.pack()
space1.pack()
button1.pack()
button2.pack()
button3.pack()
button5.pack()
space2.pack()
button_1.pack()

mainloop()