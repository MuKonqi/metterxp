#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

# This file part of MetterXP.

from tkinter import *
from tkinter import messagebox
import os

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"

if not os.getuid() == 0:
    messagebox.showerror("Hata","Sadece kök kullanıcı bu modülü çalıştırabilir!")
    exit("\nSadece kök kullanıcı bu modülü çalıştırabilir!\nModül kapatılıyor...")

def kapat():
    print("\nModül kapatılıyor...")
    exit()
def reopen():
    print("\nModül yeniden başlatılıyor...")
    pencere.destroy()
    os.system(" python3 /usr/local/bin/metterxp/modules/yapilandir.py")
def reboot():
    print("\nBilgisayarınız yeniden başlatılıyor...")
    os.system(" reboot")

pencere=Tk()
pencere.title("Yazılımları yapılandır | MetterXP")
pencere.config(background="#000000")
pencere.resizable(0, 0)

def bash():
    try:
        def penkapat():
            pencere2.destroy()
        pencere2=Tk()
        pencere2.title(".bashrc dosyasını yapılandır | MetterXP")
        pencere2.config(background="#000000")
        pencere2.resizable(0, 0)
        def main():
            get_my_user_name=my_user_name.get()
            str_my_user_name=str(get_my_user_name)
            if os.path.isfile("/usr/local/bin/metterxp/.bashrc.bak"):
                pass
            else:
                cmd2=" touch /usr/local/bin/metterxp/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /usr/local/bin/MetterXP/.bashrc.bak"
                os.system(cmd2)                
            my_user_name.destroy()
            b_1_bash.destroy()
            b_metin3.destroy()
            buton_1.destroy()
            yazi2.config(text=".bashrc dosyasında nasıl yapılandırmalar yapmak istersiniz?\nNot: Yapılandırma seçeneklerinde, seçeneklere tıklanma sırası önemlidir.\nGeçerli kullanıcı adınız: "+str_my_user_name)
            def renksiz():
                cmd1=" touch /home/"+str_my_user_name+"/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /home/"+str_my_user_name+"/.bashrc.bak"
                os.system(cmd1)
                cmd_0=" echo '   ' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_0)
                cmd_2=" echo 'echo Merhabalar "+str_my_user_name+"!' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_2)
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
            def renkli():
                cmd1=" touch /home/"+str_my_user_name+"/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /home/"+str_my_user_name+"/.bashrc.bak"
                os.system(cmd1)
                cmd_0=" echo '   ' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_0)
                print("\nLolcat kuruluyor...")
                if os.path.isfile(debian):
                    os.system(" apt install lolcat -y")
                elif os.path.isfile(fedora):
                    os.system(" dnf install lolcat -y")
                elif os.path.isfile(solus):
                    os.system(" eopkg install lolcat -y")
                cmd_1=" echo 'echo Merhabalar "+str_my_user_name+"! | lolcat' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_1)
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
            def neofetch():
                cmd1=" touch /home/"+str_my_user_name+"/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /home/"+str_my_user_name+"/.bashrc.bak"
                os.system(cmd1)
                cmd_0=" echo '   ' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_0)
                print("\nNeofetch kuruluyor...")
                if os.path.isfile(debian):
                    os.system(" apt install neofetch -y")
                elif os.path.isfile(fedora):
                    os.system(" dnf install neofetch -y")
                elif os.path.isfile(solus):
                    os.system(" eopkg install neofetch -y")
                cmd_3=" echo 'neofetch' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_3)
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
            def neofetchrenkli():
                cmd1=" touch /home/"+str_my_user_name+"/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /home/"+str_my_user_name+"/.bashrc.bak"
                os.system(cmd1)
                cmd_0=" echo '   ' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_0)
                print("\nNeofetch ile lolcat kuruluyor...")
                if os.path.isfile(debian):
                    os.system(" apt install neofetch lolcat -y")
                elif os.path.isfile(fedora):
                    os.system(" dnf install neofetch lolcat -y")
                elif os.path.isfile(solus):
                    os.system(" eopkg install neofetch lolcat -y")
                cmd_4=" echo 'neofetch | lolcat' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_4)
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
            def ram():
                cmd1=" touch /home/"+str_my_user_name+"/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /home/"+str_my_user_name+"/.bashrc.bak"
                os.system(cmd1)
                cmd_0=" echo '   ' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_0)
                cmd_5=" echo 'free -m' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_5)
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
            def ramrenkli():
                cmd1=" touch /home/"+str_my_user_name+"/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /home/"+str_my_user_name+"/.bashrc.bak"
                os.system(cmd1)
                cmd_0=" echo '   ' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_0)
                cmd_5=" echo 'free -m | lolcat' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_5)
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")             
            def kok():
                cmd1=" touch /home/"+str_my_user_name+"/.bashrc.bak ;  cp /home/"+str_my_user_name+"/.bashrc /home/"+str_my_user_name+"/.bashrc.bak"
                os.system(cmd1)
                cmd_0=" echo '   ' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_0)
                cmd_6=" echo ' su' >> /home/"+str_my_user_name+"/.bashrc"
                os.system(cmd_6)
                messagebox.showinfo("Bilgilendirme","Yapılandırma başarıyla tamamlandı.")
            bashbuton1=Button(pencere2, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Kullanıcı adımı renksiz bir şekilde ekle", command=renksiz)
            bashbuton1.pack()
            bashbuton2=Button(pencere2, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Kullanıcı adımı renkli bir şekilde ekle\n(lolcat yardımıyla)", command=renkli)
            bashbuton2.pack()
            bashbuton3=Button(pencere2, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Sistem bilgisini az renkli bir şekilde ekle\n(neofetch yardımıyla)", command=neofetch)
            bashbuton3.pack()
            bashbuton4=Button(pencere2, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Sistem bilgisini rengarenk bir şekilde ekle\n(neofetch ve lolcat yardımıyla)", command=neofetchrenkli)
            bashbuton4.pack()
            bashbuton5=Button(pencere2, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Ram tüketimini renksiz bir şekilde ekle", command=ram)
            bashbuton5.pack()
            bashbuton6=Button(pencere2, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Ram tüketimini renkli bir şekilde ekle", command=ramrenkli)
            bashbuton6.pack()
            bashbuton7=Button(pencere2, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Bash (terminal diye düşünebilirsiniz)\nbaşlatıldığında kök şifresini sor", command=kok)
            bashbuton7.pack()
            def sifirlama():
                def pen_kapat():
                    pencere3.destroy()
                pencere3=Tk()
                pencere3.title("Sıfırlama seçenekleri | MetterXP")
                pencere3.config(background="#000000")
                pencere3.resizable(0, 0)
                yazi3=Label(pencere3, background="#000000", foreground="#FFFFFF", font="arial 10 bold", text="Aşağıdan bir sıfırlama seçeneği seçiniz.")
                yazi3.pack()
                bashb_metin3=Label(pencere3, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
                bashb_metin3.pack()
                def gerialbash():
                    _cmd1=" cp /home/"+str_my_user_name+"/.bashrc.bak /home/"+str_my_user_name+"/.bashrc"
                    os.system(_cmd1)
                    messagebox.showinfo("Bilgilendirme","Geri alma başarılı.")
                def ilkhalbash():
                    _cmd2=" cp /usr/local/bin/metterxp/.bashrc.bak /home/"+str_my_user_name+"/.bashrc"
                    os.system(_cmd2)
                    messagebox.showinfo("Bilgilendirme","Geri alma başarılı.")
                bashbuton1=Button(pencere3, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text=".bashrc dosyasındaki son değişikliği geri al", command=gerialbash)
                bashbuton1.pack()
                bashbuton2=Button(pencere3, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text=".bashrc dosyasındaki tüm değişiklikleri geri al", command=ilkhalbash)
                bashbuton2.pack()
                bashb_metin4=Label(pencere3, background="#000000", foreground="#FFFFFF", font="arial 3", text="\n")
                bashb_metin4.pack()
                bashbuton_2=Button(pencere3, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat\nMenüye dön", command=pen_kapat)
                bashbuton_2.pack()
            bashb_metin1=Label(pencere2, background="#000000", foreground="#FFFFFF", font="arial 2", text="\n")
            bashb_metin1.pack()
            bashbuton8=Button(pencere2, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Sıfırlama seçenekleri", command=sifirlama)
            bashbuton8.pack()
            bashb_metin2=Label(pencere2, background="#000000", foreground="#FFFFFF", font="arial 3", text="\n")
            bashb_metin2.pack()
            bashbuton_1=Button(pencere2, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat\nMenüye dön", command=penkapat)
            bashbuton_1.pack()

        yazi2=Label(pencere2, background="#000000", foreground="#FFFFFF", font="arial 10 bold", text="Aşağıya kullanıcı adınızı giriniz (bu bilgi kesinlikle kaydedilmeyecektir).")            
        yazi2.pack()
        b_metin2=Label(pencere2, background="#000000", foreground="#FFFFFF", font="arial 2", text="\n")
        b_metin2.pack()
        my_user_name=Entry(pencere2)
        my_user_name.pack()
        b_1_bash=Button(pencere2,  cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Onayla",command=main)
        b_1_bash.pack()
        b_metin3=Label(pencere2, background="#000000", foreground="#FFFFFF", font="arial 3", text="\n")
        b_metin3.pack()
        buton_1=Button(pencere2, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat\nMenüye dön", command=penkapat)
        buton_1.pack()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def grub():
    try:
        print("\nGrub Customizer kuruluyor...")
        if os.path.isfile(debian):
            os.system(" apt install grub-customizer -y")
        elif os.path.isfile(fedora):
            os.system(" dnf install grub-customizer -y")
        elif os.path.isfile(solus):
            os.system(" eopkg install grub-customizer -y")
        print("\nGrub Customizer açılıyor...")
        os.system(" grub-customizer")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def cups():
    try:
        messagebox.showwarning("Uyarı","Bu işlem için daha önceden Cups'ı kurmuş olmanız gerekmektedir.")
        os.system("x-www-browser localhost:631")
        messagebox.showinfo("Bilgilendirme","Cups yazıcı yöneticisi için yaptığınız yapılandırma için işlemi bitirilmiştir.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def plank():
    try:
        messagebox.showwarning("Uyarı","Bu işlem için daha önceden Plank'ı kurmuş olmanız gerekmektedir.")
        os.system("plank --preferences")
        messagebox.showinfo("Bilgilendirme","Plank için yaptığınız yapılandırma işlemi bitmiştir.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def wine():
    try:
        messagebox.showwarning("Uyarı","Bu işlem için daha önceden Wine'ı kurmuş olmanız gerekmektedir.")
        os.system(" winecfg")
        messagebox.showinfo("Bilgilendirme","Wine için yaptığınız yapılandırma işlemi bitirilmiştir.")
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()
def pcrename():
    try:
        def penkapat():
            pencere2.destroy()
        pencere2=Tk()
        pencere2.title("Bu bilgisayarın adını yapılandır | MetterXP")
        pencere2.config(background="#000000")
        pencere2.resizable(0, 0)
        def addpcname():
            get_new_pc_name=new_pc_name.get()
            add_new_pc_name=open('/etc/hostname', "w")
            add_new_pc_name.write(get_new_pc_name)
            add_new_pc_name.close()
            messagebox.showinfo("Bilgilendirme","Bilgisayarınızın yeni adını uygulamak için 'OK' tuşuna bastığınızda bilgisayarınız yeniden başlatılacak.")
            reboot()
        yazi2=Label(pencere2, background="#000000", foreground="#FFFFFF", font="arial 10 bold", text="Aşağıya bilgisayarınız için yeni bir ad giriniz.")
        yazi2.pack()
        b_metin2=Label(pencere2, background="#000000", foreground="#FFFFFF", font="arial 2", text="\n")
        b_metin2.pack()
        new_pc_name=Entry(pencere2)
        new_pc_name.pack()
        b_1_pcrename=Button(pencere2,  cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Kaydet",command=addpcname)
        b_1_pcrename.pack()
        b_metin3=Label(pencere2, background="#000000", foreground="#FFFFFF", font="arial 3", text="\n")
        b_metin3.pack()
        buton_1=Button(pencere2, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Pencereyi kapat\nMenüye dön", command=penkapat)
        buton_1.pack()
    except:
        messagebox.showerror("Hata","Bazı hata(lar) oluştu!\n'OK' tuşuna basınca tekrar denemeniz için modül kapatılacak.")
        kapat()

yazi1=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 10 bold", text="Hangi dosya yöneticisini kök haklarıyla açmak istersiniz?")
yazi1.pack()
b_metin1=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
b_metin1.pack()
islemsecimbuton1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text=".bashrc dosyasını [Bash (terminal olarak düşünebilirsiniz)\n Yapılandırma Dosyası] yapılandır", command=bash)
islemsecimbuton1.pack()
islemsecimbuton2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="GRUB önyükleyiciyi yapılandır\n(Grub Customizer yardımıyla)", command=grub)
islemsecimbuton2.pack()
islemsecimbuton3=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Cups yazıcı yöneticisini yapılandır", command=cups)
islemsecimbuton3.pack()
islemsecimbuton4=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Plank dockunu yapılandır", command=plank)
islemsecimbuton4.pack()
islemsecimbuton5=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Wine'ı yapılandır", command=wine)
islemsecimbuton5.pack()
islemsecimbuton6=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Bu bilgisayarın adını yapılandır", command=pcrename)
islemsecimbuton6.pack()
b_metin2=Label(pencere, background="#000000", foreground="#FFFFFF", text="\n", font="arial 3")
b_metin2.pack()
buton_1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", background="#FFFFFF", foreground="#000000", borderwidth="3", text="Ana menüye dön\nModülü kapat", command=kapat)
buton_1.pack()

mainloop()
