#!/usr/bin/env python3

#Copyright (C) 2021, Muhammed Abdurrahman

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

#İçe aktarma:
import os
import time
#Giriş:
print("BetterXP Installer'a hoş geldiniz!")
#İşletim sistemi kontrolü:
name=os.name
if name == "nt":
    print("BetterXP ve BetterXP Installer, NT çekirdeğini kullanan işletim sistemlerinde (Windows, ReactOS) çalışmaz.")
    print("BetterXP Installer kapatılıyor.")
    time.sleep(3)
    exit()
#Debian GNU/Linux mu değil mi kontrolü:
if os.path.isfile('/etc/debian_version'):
    print("Şimdi aşağıda kullandığınız dağıtım ya da kullandığınız dağıtımın taban aldığı dağıtım ve paket yöneticisi gözükecektir. İşlemlerde buna göre yapılacaktır.")
    set_systembase="Dağıtım: Debian"
    set_packagemanager="Paket Yöneticisi: APT"
    print(set_systembase)     
    print(set_packagemanager)   
    sonuc = input("Bunlar doğru mu?(evet/hayır):")
    if sonuc == "evet":      
        islem = input("Lütfen BetterXP Installer'da çalıştırmak istediğiniz komutu seçiniz.(kur/bilgi/çıkış):")
        if islem == "kur":
            user="/home/"
            user1="$USER"
            user2="/Masaüstü/"
            user3=user+user1+user2
            user4="/Desktop/"
            user5=user+user1+user4
            os.system("sudo apt install python3 python3-tk git -y")
            os.system("sudo git clone https://github.com/androidprotmmas/BetterXP_Debian.git")
            os.system("sudo mv BetterXP_Debian BetterXP")
            os.system("cd BetterXP")
            os.system("sudo rm -rf .git")
            os.system("cd")
            os.system("sudo mv BetterXP /usr/local/bin/")
            os.system("chmod +x BetterXP.desktop")
            os.system("sudo cp BetterXP.desktop /usr/share/applications")
            try:
                os.system("sudo cp BetterXP.desktop "+user3)
            except:
                try:
                    os.system("sudo cp BetterXP.desktop "+user5)
                except:
                    print("Bazı hatalarla karşılaşıldı, kurulum yarıda kesildi.")
                    print("BetterXP Installer kapatılıyor.")
                    time.sleep(3)
                    exit()
            os.system("chmod +x betterxp.sh && sudo cp betterxp.sh /usr/bin/betterxp")
            os.system("sudo apt install nano -y")
            print("Az sonra karşınıza çıkacak pencerede kullanıcı adınızı girmeniz gerekecektir.")
            time.sleep(3)
            os.system("sudo nano /usr/local/bin/BetterXP/whoami.txt")        
            print("BetterXP kuruldu. Umarız BetterXP sizin daha iyi bir deneyim yaşamanızı sağlar.")
            print("BetterXP Installer kapatılıyor.")
            time.sleep(3)
            exit()
        elif islem == "bilgi":
            print("BetterXP Installer, BetterXP'yi kurmanızı sağlayan bir araçtır.")
            print("Lisans: GPL 3.0")
            kapat = input('BetterXP Installer "evet" yazdığınız an kapanacaktır:')
            if kapat == "evet":
                exit()
            else:
                print("Yanlış bir cevap girdiniz. BetterXP Installer kapatılıyor.")
                time.sleep(3)
                exit()
        elif islem == "çıkış":
            exit()
        else:
            print("Yanlış bir cevap girdiniz. BetterXP Installer kapatılıyor.")
            time.sleep(3)
            exit()
    elif sonuc == "hayır":
        print("Verdiğiniz cevaba göre, kullandığınız dağıtım ya da onun taban aldığı dağıtım yanlış algılandı. Lütfen bunu bize bildirin.")
        print("BetterXP Installer kapatılıyor.")
        time.sleep(3)
        exit()
    else:
        print("Yanlış bir cevap girdiniz. BetterXP Installer kapatılıyor.")
        time.sleep(3)
        exit()
#Fedora Linux mu değil mi kontrolü:
elif os.path.isfile('/etc/fedora-release'):
    print("Şimdi aşağıda kullandığınız dağıtım ya da kullandığınız dağıtımın taban aldığı dağıtım ve paket yöneticisi gözükecektir. İşlemlerde buna göre yapılacaktır.")
    set_systembase="Dağıtım: Fedora"
    set_packagemanager="Paket Yöneticisi: DNF"
    print(set_systembase)     
    print(set_packagemanager)   
    sonuc = input("Bunlar doğru mu?(evet/hayır):")
    if sonuc == "evet":      
        islem = input("Lütfen BetterXP Installer'da çalıştırmak istediğiniz komutu seçiniz.(kur/bilgi/çıkış):")
        if islem == "kur":
            user="/home/"
            user1="$USER"
            user2="/Masaüstü/"
            user3=user+user1+user2
            user4="/Desktop/"
            user5=user+user1+user4
            os.system("sudo dnf install python3 python3-tkinter git -y")
            os.system("sudo git clone https://github.com/androidprotmmas/BetterXP_Fedora.git")
            os.system("sudo mv BetterXP_Fedora BetterXP")
            os.system("cd BetterXP")
            os.system("sudo rm -rf .git")
            os.system("cd")
            os.system("sudo mv BetterXP /usr/local/bin/")
            os.system("chmod +x BetterXP.desktop")
            os.system("sudo cp BetterXP.desktop /usr/share/applications")
            try:
                os.system("sudo cp BetterXP.desktop "+user3)
            except:
                try:
                    os.system("sudo cp BetterXP.desktop "+user5)
                except:
                    print("Bazı hatalarla karşılaşıldı, kurulum yarıda kesildi.")
                    print("BetterXP Installer kapatılıyor.")
                    time.sleep(3)
                    exit()
            os.system("chmod +x betterxp.sh && sudo cp betterxp.sh /usr/bin/betterxp")
            os.system("sudo dnf install nano -y")
            print("Az sonra karşınıza çıkacak pencerede kullanıcı adınızı girmeniz gerekecektir.")
            time.sleep(3)
            os.system("sudo nano /usr/local/bin/BetterXP/whoami.txt")
            print("BetterXP kuruldu. Umarız BetterXP sizin daha iyi bir deneyim yaşamanızı sağlar.")
            print("BetterXP Installer kapatılıyor.")
            time.sleep(3)
            exit()
        elif islem == "bilgi":
            print("BetterXP Installer, BetterXP'yi kurmanızı sağlayan bir araçtır.")
            print("Lisans: GPL 3.0")
            kapat = input('BetterXP Installer "evet" yazdığınız an kapanacaktır:')
            if kapat == "evet":
                exit()
            else:
                print("Yanlış bir cevap girdiniz. BetterXP Installer kapatılıyor.")
                time.sleep(3)
                exit()
        elif islem == "çıkış":
            exit()
        else:
            print("Yanlış bir cevap girdiniz. BetterXP Installer kapatılıyor.")
            time.sleep(3)
            exit()
    elif sonuc == "hayır":
        print("Verdiğiniz cevaba göre, kullandığınız dağıtım ya da onun taban aldığı dağıtım yanlış algılandı. Lütfen bunu bize bildirin.")
        print("BetterXP Installer kapatılıyor.")
        time.sleep(3)
        exit()
    else:
        print("Yanlış bir cevap girdiniz. BetterXP Installer kapatılıyor.")
        time.sleep(3)
        exit()
#Solus mu değil mi kontrolü:
elif os.path.isfile('/etc/solus-release'):
    print("Şimdi aşağıda kullandığınız dağıtım ya da kullandığınız dağıtımın taban aldığı dağıtım ve paket yöneticisi gözükecektir. İşlemlerde buna göre yapılacaktır.")
    set_systembase="Dağıtım: Solus"
    set_packagemanager="Paket Yöneticisi: EOPKG"
    print(set_systembase)     
    print(set_packagemanager)   
    sonuc = input("Bunlar doğru mu?(evet/hayır):")
    if sonuc == "evet":      
        islem = input("Lütfen BetterXP Installer'da çalıştırmak istediğiniz komutu seçiniz.(kur/bilgi/çıkış):")
        if islem == "kur":
            user="/home/"
            user1="$USER"
            user2="/Masaüstü/"
            user3=user+user1+user2
            user4="/Desktop/"
            user5=user+user1+user4
            os.system("sudo eopkg it python3 python3-tkinter git -y")
            os.system("sudo mkdir /usr/local ; sudo mkdir /usr/local/bin")
            os.system("sudo git clone https://github.com/androidprotmmas/BetterXP_Solus.git")
            os.system("sudo mv BetterXP_Solus BetterXP")
            os.system("cd BetterXP")
            os.system("sudo rm -rf .git")
            os.system("cd")
            os.system("sudo mv BetterXP /usr/local/bin/")
            os.system("chmod +x BetterXP.desktop")
            os.system("sudo cp BetterXP.desktop /usr/share/applications")
            try:
                os.system("sudo cp BetterXP.desktop "+user3)
            except:
                try:
                    os.system("sudo cp BetterXP.desktop "+user5)
                except:
                    print("Bazı hatalarla karşılaşıldı, kurulum yarıda kesildi.")
                    print("BetterXP Installer kapatılıyor.")
                    time.sleep(3)
                    exit()
            os.system("chmod +x betterxp.sh && sudo cp betterxp.sh /usr/bin/betterxp")
            os.system("sudo eopkg it nano -y")
            print("Az sonra karşınıza çıkacak pencerede kullanıcı adınızı girmeniz gerekecektir.")
            time.sleep(3)
            os.system("sudo nano /usr/local/bin/BetterXP/whoami.txt")
            print("BetterXP kuruldu. Umarız BetterXP sizin daha iyi bir deneyim yaşamanızı sağlar.")
            print("BetterXP Installer kapatılıyor.")
            time.sleep(3)
            exit()
        elif islem == "bilgi":
            print("BetterXP Installer, BetterXP'yi kurmanızı sağlayan bir araçtır.")
            print("Lisans: GPL 3.0")
            kapat = input('BetterXP Installer "evet" yazdığınız an kapanacaktır:')
            if kapat == "evet":
                exit()
            else:
                print("Yanlış bir cevap girdiniz. BetterXP Installer kapatılıyor.")
                time.sleep(3)
                exit()
        elif islem == "çıkış":
            exit()
        else:
            print("Yanlış bir cevap girdiniz. BetterXP Installer kapatılıyor.")
            time.sleep(3)
            exit()
    elif sonuc == "hayır":
        print("Verdiğiniz cevaba göre, kullandığınız dağıtım ya da onun taban aldığı dağıtım yanlış algılandı. Lütfen bunu bize bildirin.")
        print("BetterXP Installer kapatılıyor.")
        time.sleep(3)
        exit()
    else:
        print("Yanlış bir cevap girdiniz. BetterXP Installer kapatılıyor.")
        time.sleep(3)
        exit()
#Desteklenmeyen dağıtımlar:
else:
    print("Kullandığınız GNU/Linux veya Linux dağıtımını BetterXP ve BetterXP Installer tam anlamıyla desteklemiyor.")
    other = input("Hangi komutu çalıştırmak istersiniz?(bilgi/çıkış):")
    if other == "bilgi":
        print("BetterXP Installer, BetterXP'yi kurmanızı sağlayan bir araçtır.")
        print("Lisans: GPL 3.0")
        kapat = input('BetterXP Installer "evet" yazdığınız an kapanacaktır:')
        if kapat == "evet":
            exit()
        else:
            print("Yanlış bir cevap girdiniz. BetterXP Installer kapatılıyor.")
            time.sleep(3)
            exit()   
    elif other == "çıkış":
        exit()
    else:
        print("Yanlış bir cevap girdiniz. BetterXP Installer kapatılıyor.")
        time.sleep(3)
        exit()    
