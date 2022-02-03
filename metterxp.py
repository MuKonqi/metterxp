#!/usr/bin/env python3

# Copyright (C) 2021, 2022 Muhammed Abdurrahman

# MetterXP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# MetterXP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with MetterXP.  If not, see <https://www.gnu.org/licenses/>.

from tkinter import *
from tkinter import messagebox
import os
import sys

debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
args=sys.argv[1:]

def main_gui():
    def mxpkapat():
        print("\nMetterXP kapatılıyor...")
        exit()
        
    def prkurkaldır():
        print("\nProgram kur/yeniden kur/kaldır modülü açılıyor...")
        os.system("pkexec python3 /usr/local/bin/metterxp/modules/prkurkaldır.py")
    def prara():
        print("\nProgram/paket arama modülü açılıyor...")
        os.system("python3 /usr/local/bin/metterxp/modules/prara.py")       
    def dewmkurkaldır():
        print("\nMasaüstü ortamı/pencere yöneticisi kur/yeniden kur/kaldır modülü açılıyor...")
        os.system("pkexec python3 /usr/local/bin/metterxp/modules/dewmkurkaldır.py")
    def sistemiguncelle():
        print("\nSistem güncelle modülü açılıyor...")
        os.system("pkexec python3 /usr/local/bin/metterxp/modules/sistemiguncelle.py")
        messagebox.showinfo("Bilgilendirme","Sistem güncellemesi varsa başarıyla tamamlandı.")
    def yapilandir():
        print("\nYazılımları yapılandır modülü açılıyor...")
        os.system("pkexec python3 /usr/local/bin/metterxp/yapilandir.py")
    def fmkok():
        print("\nDosya yöneticilerini kök haklarıyla açma modülğ açılıyor...")
        os.system("pkexec python3 /usr/local/bin/metterxp/modules/fmkok.py")
    def distro():
        print("\nBazı GNU/Linux dağıtımları hakkında modülü açılıyor...")
        os.system("python3 /usr/local/bin/metterxp/modules/distro.py")
    def pmkur():
        print("\nPaket yöneticisi kur/yeniden kur modülü açılıyor...")
        os.system("pkexec python3 /usr/local/bin/metterxp/modules/pmkur.py")
    def onbellekpkttemizle():
        if os.path.isfile(solus):
            print("\nÖnbellek temizleme modülü açılıyor...")
            os.system("pkexec python3 /usr/local/bin/metterxp/modules/onbellekpkttemizle.py")
            messagebox.showinfo("Bilgilendirme","Önbellek başarıyla temizlendi.")
        else:
            print("\nÖnbellek ve gereksiz paketleri temizleme modülü açılıyor...")
            os.system("pkexec python3 /usr/local/bin/metterxp/modules/onbellekpkttemizle.py")
            messagebox.showinfo("Bilgilendirme","Önbellek ve gereksiz paketler başarıyla temizlendi.")            
    def mxphakkinda():
        print("\nMetterXP hakkında modülü açılıyor...")
        os.system("python3 /usr/local/bin/metterxp/hakkinda.py")
    def mxpguncelle():
        print("\nMetterXP'ı güncelle modülü açılıyor...")
        os.system("python3 /usr/local/bin/metterxp/yukselt.py")
    def islemsecim():
        yazi1.config(text="Lütfen yapmak istediğiniz işlemi aşağıdaki listeden seçiniz.")
        b_metin1=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 3", text="\n")
        b_metin1.pack()
        islemsecimbuton1=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Program kur/yeniden kur/kaldır", command=prkurkaldır)
        islemsecimbuton1.pack()
        islemsecimbuton2=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Program/paket arama", command=prara)
        islemsecimbuton2.pack()
        islemsecimbuton3=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Masaüstü ortamı/pencere yöneticisi\nkur/yeniden kur/kaldır",command=dewmkurkaldır)
        islemsecimbuton3.pack()
        islemsecimbuton4=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Sistemi güncelle",command=sistemiguncelle)
        islemsecimbuton4.pack()
        islemsecimbuton5=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Yazılımları yapılandır",command=yapilandir)
        islemsecimbuton5.pack()
        islemsecimbuton6=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Bazı dosya yöneticilerini kök haklarıyla aç",command=fmkok)
        islemsecimbuton6.pack()
        islemsecimbuton7=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Bazı GNU/Linux dağıtımları hakkında",command=distro)
        islemsecimbuton7.pack()
        islemsecimbuton8=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Paket yöneticisi kur/yeniden kur",command=pmkur)
        islemsecimbuton8.pack()
        if os.path.isfile(solus):
            islemsecimbuton9=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Önbelleği temizle",command=onbellekpkttemizle)
        else:
            islemsecimbuton9=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Önbelleği ve gereksiz paketleri temizle",command=onbellekpkttemizle)
        islemsecimbuton9.pack()
        if os.path.isfile(debian):
            def kaliarackur():
                pass
            def hatacoz():
                print("\nProgram/paket hatalarını çöz modülü açılıyor...")
                os.system("pkexec python3 /usr/local/bin/metterxp/modules/hatacoz.py")
                messagebox.showinfo("Bilgilendirme","Program/paket hataları çözüldü.")
            islemsecimbuton10=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Kali Linux araçlarını kur",command=kaliarackur)
            islemsecimbuton10.pack()
            islemsecimbuton11=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="Program/paket hatalarını çöz",command=hatacoz)
            islemsecimbuton11.pack()            
        b_metin2=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 3", text="\n")
        b_metin2.pack()
        mxp_hakkinda=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="MetterXP hakkında",command=mxphakkinda)
        mxp_hakkinda.pack()
        mxp_yukselt=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="MetterXP'ı güncelle",command=mxpguncelle)
        mxp_yukselt.pack()
        b_metin3=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 3", text="\n")
        b_metin3.pack()
        mxpkapat_buton=Button(pencere, font="arial 10", cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="3", text="MetterXP'ı kapat",command=mxpkapat)
        mxpkapat_buton.pack()
        
    if os.path.isfile("/usr/local/bin/metterxp/firststartsuccesful"):
        pencere=Tk()
        pencere.title("MetterXP")
        pencere.config(background="#000000")
        pencere.resizable(0, 0)
        
        menu1=Menu(pencere)
        pencere.config(menu=menu1)
        dosya=Menu(menu1, tearoff=0)
        menu1.add_cascade(label="Dosya",menu=dosya)
        dosya.add_command(label="Çıkış", command=mxpkapat)
        
        yazi1=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 10 bold")
        yazi1.pack()
        
        islemsecim()
    else:
        def exitfirststart():
            # os.system("cd /usr/local/bin/metterxp ; sudo touch firststartsuccesful")
            pencere.title("MetterXP")
            metin1.destroy()
            h_buton.destroy()
            menu1=Menu(pencere)
            pencere.config(menu=menu1)
            dosya=Menu(menu1, tearoff=0)
            menu1.add_cascade(label="Dosya",menu=dosya)
            dosya.add_command(label="Çıkış", command=mxpkapat)
            islemsecim()
        
        pencere=Tk()
        pencere.title("MetterXP'a hoşgeldiniz! | MetterXP")
        pencere.config(background="#000000")
        pencere.resizable(0, 0) 
        
        metin1=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 12 bold italic", text="\nİlk defa MetterXP programını açtığınız tespit edildi.\n\n\nMetterXP araç kutusunda bulunan bazı özellikler:\nProgram kurma/yeniden kurma/kaldırma\nProgram/paket arama\nMasaüstü ortamı/pencere yöneticisi kurma/yeniden kurma/kaldımar\nPaket yöneticisi kurma/yeniden kurma\nSistemi güncelleme\nÇeşitli yapılandırmalar (.bashrc, GRUB, Cups, Plank, Wine ve bilgisayar adı)\nVe dahası...\n\nBilinen hatalar: Program kur/yeniden/kur/kaldır ile program arama özelliklerindeki çıktılarda bulunan anlamsız semboller\n\n\nMetterXP, yürüteceği herhangi bir işlem için garanti vermemektedir (bakınız GPLv3).\n")
        metin1.pack()
        
        yazi1=Label(pencere, background="#000000", foreground="#FFFFFF", font="arial 10 bold")
        yazi1.pack()
        
        h_buton=Button(pencere, cursor="hand2", activebackground="#03035B", activeforeground="#FFFFFF", foreground="#000000", background="#FFFFFF", borderwidth="5")
        h_buton.config(font="arial 11", text="Ana Menü",command=exitfirststart)
        h_buton.pack()
    
    mainloop()


def main_cli():
    if os.path.isfile("/usr/local/bin/MetterXP/firststartsuccesful"):
        print("MetterXP'a hoş geldiniz!")
    else:
        print("\nUyarı: Görünüşe göre daha önce MetterXP'ı hiç açmamışsınız. Bu yüzden MetterXP, varsayılan grafik arayüz modunda başlatılıyor...")
        main_gui()
        exit()
    if "yardım" in args or "-y" in args or "-h" in args:
        print("\nMetterXP, program kur/yeniden kur/kaldır, masaüstü ortamı/pencere yöneticisi kur/yeniden kur/kaldır, sistem güncelleme, çeşitli yapılandırma özelliklerine (GRUB, Terminal, Plank, WINE...), paket yöneticisi kurma vs. özelliklere sahip olan bir araç kutusudur.")
        print("İşte bütün kullanımlar:")
        print("yardım/-y/-h                   Yardım ekranını (burayı) göster")
        print("prkurkaldır                    Program kur/yeniden kur/kaldır")
        print("prara                          Program/paket ara")
        print("dewmkurkaldır                  Masaüstü ortamı/pencere yöneticisi kur/yeniden kur/kaldır")
        print("sistemigüncelle                Sistemi güncelle")
        print("yapılandır                     Yazılımları yapılandır")
        print("fmkök                          Bazı dosya yöneticilerini kök haklarıyla aç")
        print("dağıtımlar                     Bazı GNU/Linux dağıtımları hakkında")
        print("pmkur                          Paket yöneticisi kur/yeniden kur")
        print("hakkında                       MetterXP hakkında")
        print("güncelle                       MetterXP'ı güncelle")
        if os.path.isfile(solus):
            print("önbellektemizle                Önbelleği temizle")
        else:
            print("önbellekpakettemizle           Önbelleği ve gereksiz paketleri temizle")
        if os.path.isfile(debian):
            print("kaliaraçkur                    Kali Linux araçlarını kur\nhataçözücü                     Hata çözücü\n")
        sys.exit()
    elif "prkurkaldır" in args:
        print("\nProgram kur/yeniden kur/kaldır modülü açılıyor...")
        os.system("pkexec python3 /usr/local/bin/metterxp/modules/prkurkaldır.py")
        sys.exit()
    elif "prara" in args:
        print("\nProgram/paket arama modülü açılıyor...")
        os.system("python3 /usr/local/bin/metterxp/modules/prara.py")
        sys.exit()
    elif "dewmkurkaldır" in args:
        print("\nMasaüstü ortamı/pencere yöneticisi kur/yeniden kur/kaldır modülü açılıyor...")
        os.system("pkexec python3 /usr/local/bin/metterxp/modules/dewmkurkaldır.py")
        sys.exit()
    elif "sistemigüncelle" in args:
        print("\nSistem güncelleme modülü açılıyor...")
        os.system("pkexec python3 /usr/local/bin/metterxp/modules/sistemiguncelle.py")
        print("Sistem güncellemesi varsa başarıyla tamamlandı.")
        sys.exit()
    elif "yapılandır" in args:
        print("\nYazılımları yapılandır modülü açılıyor...")
        os.system("pkexec python3 /usr/local/bin/metterxp/modules/yapilandir.py")
        sys.exit()
    elif "fmkök" in args:
        print("\nBazı dosya yöneticileri kök haklarıyla aç modülü açılıyor...")
        os.system("pkexec python3 /usr/local/bin/metterxp/modules/fmkok.py")
        sys.exit()
    elif "dağıtımlar" in args:
        print("\nBazı GNU/Linux dağıtımları hakkında modülü açılıyor...")
        os.system("python3 /usr/local/bin/metterxp/modules/distro.py")
        sys.exit()
    elif "pmkur" in args:
        print("\nPaket yöneticisi kur/yeniden kur modülü açılıyor...")
        os.system("pkexec python3 /usr/local/bin/metterxp/modules/pmkur.py")
        sys.exit()
    elif "hakkında" in args:
        print("\nMetterXP hakkında modülü açılıyor...")
        os.system("python3 /usr/local/bin/metterxp/hakkinda.py")
    elif "güncelle" in args:
        print("\nMetterXP'ı güncelle modülü açılıyor...")
        os.system("python3 /usr/local/bin/metterxp/yukselt.py")
        print("\nMetterXP başarıyla güncellendi!\nMetterXP kapatılıyor...")
        sys.exit()
    if os.path.isfile(solus):    
        if "önbellektemizle" in args:
            print("\nÖnbellek temizleme modülü açılıyor...")
            os.system("pkexec python3 /usr/local/bin/metterxp/modules/onbellekpkttemizle.py")
            sys.exit()
    else:
        if "önbellekpakettemizle" in args:
            print("\nÖnbellek ve gereksiz paketleri temizleme modülü açılıyor...")
            os.system("pkexec python3 /usr/local/bin/metterxp/modules/onbellekpkttemizle.py")
            sys.exit()
    if os.path.isfile(debian):
        if "hataçözücü" in args:
            print("\nHata çözme modülü açılıyor...")
            os.system("pkexec python3 /usr/local/bin/metterxp/modules/hatacoz.py")
            sys.exit()
        elif "kaliaraçkur" in args:
            print("\nKali Linux araçlarını kur modülü açılıyor...")
            os.system("pkexec python3 /usr/local/bin/metterxp/modules/kaliarackur.py")
            sys.exit()
    else:
        main_gui()
        
if os.name == "nt":
    print("MetterXP'a hoş geldiniz!\nMetterXP, NT çekirdeğini kullanan işletim sistemlerinde çalışmaz.\nLütfen şu üç GNU/Linux dağıtımından birini temel alan bir GNU/Linux dağıtımıyla programı açmayı deneyiniz:\nDebian GNU/Linux, Fedora Linux, Solus\n\nMetterXP kapatılıyor...")
    exit()
elif os.path.isfile(debian):
    main_cli()
elif os.path.isfile(fedora):
    main_cli()
elif os.path.isfile(solus):
    main_cli()
else:
    print("MetterXP'a hoş geldiniz!\nKullandığınız işletim sistemini/dağıtımı MetterXP tam anlamıyla desteklemiyor.\nLütfen şu üç GNU/Linux dağıtımından birini temel alan bir GNU/Linux dağıtımıyla programı açmayı deneyiniz:\nDebian GNU/Linux, Fedora Linux, Solus\n\nMetterXP kapatılıyor...")
    exit()
