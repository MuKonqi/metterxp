#!/usr/bin/env python3

# Copyright (C) 2021, Muhammed Abdurrahman

# BetterXP and BetterXP Installer is free software:
# you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# BetterXP and BetterXP Installer is distributed in the hope 
# that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.   
# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with BetterXP and BetterXP Installer.
# If not, see <https://www.gnu.org/licenses/>.

#İçe aktarma:
import os
import time
#Giriş:
print("BetterXP Installer'a hoş geldiniz!")
#İşletim sistemi kontrolü:
name=os.name
if name == "nt":
    print("BetterXP ve BetterXP Installer, NT çekirdeğini kullanan işletim sistemlerinde (Windows, ReactOS) çalışmaz.\nBetterXP Installer kapatılıyor...")
    time.sleep(3)
    exit()
#Debian GNU/Linux mu değil mi kontrolü:
if os.path.isfile('/etc/debian_version'):
    print("Şimdi aşağıda kullandığınız dağıtım ya da kullandığınız dağıtımın taban aldığı dağıtım ve paket yöneticisi gözükecektir. İşlemlerde buna göre yapılacaktır.")
    set_systembase="Dağıtım: Debian GNU/Linux tabanlı"
    set_packagemanager="Paket Yöneticisi: DPKG"
    print(set_systembase)     
    print(set_packagemanager)   
    sonuc = input("Bunlar doğru mu?(evet/hayır): ")
    if sonuc == "evet":      
        islem = input("Lütfen BetterXP Installer'da çalıştırmak istediğiniz komutu seçiniz.(kur/bilgi/çıkış): ")
        if islem == "kur":
            user="/home/"
            user1=input("Kuruluma başlanması için BetterXP'ı kullanacak kişinin kullanıcı adını girmeniz gerekmektedir: ")
            user2="/Masaüstü/"
            user3=user+user1+user2
            user4="/Desktop/"
            user5=user+user1+user4
            os.system("sudo apt install python3 python3-tk git -y")
            os.system("sudo git clone https://github.com/MuKonqi/BetterXP.git")
            os.system("sudo mv BetterXP/BetterXP /usr/local/bin/")
            os.system("chmod +x BetterXP.desktop")
            os.system("sudo cp BetterXP.desktop /usr/share/applications")
            try:
                os.system("sudo cp BetterXP.desktop "+user3)
            except:
                try:
                    os.system("sudo cp BetterXP.desktop "+user5)
                except:
                    print("Bazı hatalarla karşılaşıldı, kurulum yarıda kesildi.\nBetterXP Installer kapatılıyor...")
                    time.sleep(3)
                    exit()
            os.system("sudo cp ml.mukonqi.pkexec.betterxp.policy /usr/share/polkit-1/actions")
            os.system("chmod +x betterxp.py && sudo cp betterxp.py /usr/bin/betterxp")
            os.system("cd /usr/local/bin/BetterXP ; sudo touch whoami.txt")
            myusernameadd=open('/usr/local/bin/BetterXP/whoami.txt', "w")
            myusernameadd.write(user1)
            myusernameadd.close()
            print("BetterXP kuruldu. Umarız BetterXP sizin daha iyi bir deneyim yaşamanızı sağlar.\nBetterXP Installer kapatılıyor...")
            time.sleep(3)
            exit()
        elif islem == "bilgi":
            print("BetterXP Installer, BetterXP'ı kurmanızı sağlayan bir araçtır.")
            print("Lisans: GPL 3.0")
            kapat = input('BetterXP Installer "evet" yazdığınız an kapanacaktır:')
            if kapat == "evet":
                exit()
            else:
                print("Yanlış bir cevap girdiniz.\nBetterXP Installer kapatılıyor...")
                time.sleep(3)
                exit()
        elif islem == "çıkış":
            exit()
        else:
            print("Yanlış bir cevap girdiniz.\nBetterXP Installer kapatılıyor...")
            time.sleep(3)
            exit()
    elif sonuc == "hayır":
        print("Verdiğiniz cevaba göre, kullandığınız dağıtım ya da onun taban aldığı dağıtım yanlış algılandı. Lütfen bunu bize bildirin.\nBetterXP Installer kapatılıyor...")
        time.sleep(3)
        exit()
    else:
        print("Yanlış bir cevap girdiniz.\nBetterXP Installer kapatılıyor.")
        time.sleep(3)
        exit()
#Fedora Linux mu değil mi kontrolü:
elif os.path.isfile('/etc/fedora-release'):
    print("Şimdi aşağıda kullandığınız dağıtım ya da kullandığınız dağıtımın taban aldığı dağıtım ve paket yöneticisi gözükecektir. İşlemlerde buna göre yapılacaktır.")
    set_systembase="Dağıtım: Fedora Linux tabanlı"
    set_packagemanager="Paket Yöneticisi: DNF"
    print(set_systembase)     
    print(set_packagemanager)   
    sonuc = input("Bunlar doğru mu?(evet/hayır): ")
    if sonuc == "evet":      
        islem = input("Lütfen BetterXP Installer'da çalıştırmak istediğiniz komutu seçiniz.(kur/bilgi/çıkış): ")
        if islem == "kur":
            user="/home/"
            user1=input("Kuruluma başlanması için BetterXP'ı kullanacak kişinin kullanıcı adını girmeniz gerekmektedir: ")
            user2="/Masaüstü/"
            user3=user+user1+user2
            user4="/Desktop/"
            user5=user+user1+user4
            os.system("sudo dnf install python3 python3-tkinter git -y")
            os.system("sudo git clone https://github.com/MuKonqi/BetterXP.git")
            os.system("sudo mv BetterXP/BetterXP /usr/local/bin/")
            os.system("chmod +x BetterXP.desktop")
            os.system("sudo cp BetterXP.desktop /usr/share/applications")
            try:
                os.system("sudo cp BetterXP.desktop "+user3)
            except:
                try:
                    os.system("sudo cp BetterXP.desktop "+user5)
                except:
                    print("Bazı hatalarla karşılaşıldı, kurulum yarıda kesildi.\nBetterXP Installer kapatılıyor...")
                    time.sleep(3)
                    exit()
            os.system("sudo cp ml.mukonqi.pkexec.betterxp.policy /usr/share/polkit-1/actions")
            os.system("chmod +x betterxp.py && sudo cp betterxp.py /usr/bin/betterxp")
            myusernameadd=open('/usr/local/bin/BetterXP/whoami.txt', "w")
            myusernameadd.write(user1)
            myusernameadd.close()
            os.system("sudo rm -rf BetterXP")
            print("BetterXP kuruldu. Umarız BetterXP sizin daha iyi bir deneyim yaşamanızı sağlar.\nBetterXP Installer kapatılıyor...")
            time.sleep(3)
            exit()
        elif islem == "bilgi":
            print("BetterXP Installer, BetterXP'ı kurmanızı sağlayan bir araçtır.")
            print("Lisans: GPL 3.0")
            kapat = input('BetterXP Installer "evet" yazdığınız an kapanacaktır:')
            if kapat == "evet":
                exit()
            else:
                print("Yanlış bir cevap girdiniz.\nBetterXP Installer kapatılıyor...")
                time.sleep(3)
                exit()
        elif islem == "çıkış":
            exit()
        else:
            print("Yanlış bir cevap girdiniz.\nBetterXP Installer kapatılıyor...")
            time.sleep(3)
            exit()
    elif sonuc == "hayır":
        print("Verdiğiniz cevaba göre, kullandığınız dağıtım ya da onun taban aldığı dağıtım yanlış algılandı. Lütfen bunu bize bildirin.\nBetterXP Installer kapatılıyor...")
        time.sleep(3)
        exit()
    else:
        print("Yanlış bir cevap girdiniz.\nBetterXP Installer kapatılıyor.")
        time.sleep(3)
        exit()
#Solus mu değil mi kontrolü:
elif os.path.isfile('/etc/solus-release'):
    print("Şimdi aşağıda kullandığınız dağıtım ya da kullandığınız dağıtımın taban aldığı dağıtım ve paket yöneticisi gözükecektir. İşlemlerde buna göre yapılacaktır.")
    set_systembase="Dağıtım: Solus tabanlı"
    set_packagemanager="Paket Yöneticisi: EOPKG"
    print(set_systembase)     
    print(set_packagemanager)   
    sonuc = input("Bunlar doğru mu?(evet/hayır): ")
    if sonuc == "evet":      
        islem = input("Lütfen BetterXP Installer'da çalıştırmak istediğiniz komutu seçiniz.(kur/bilgi/çıkış): ")
        if islem == "kur":
            user="/home/"
            user1=input("Kuruluma başlanması için BetterXP'ı kullanacak kişinin kullanıcı adını girmeniz gerekmektedir: ")
            user2="/Masaüstü/"
            user3=user+user1+user2
            user4="/Desktop/"
            user5=user+user1+user4
            os.system("sudo eopkg it python3 python3-tkinter git -y")
            os.system("sudo mkdir /usr/local ; sudo mkdir /usr/local/bin")
            os.system("sudo git clone https://github.com/MuKonqi/BetterXP.git")
            os.system("sudo mv BetterXP/BetterXP /usr/local/bin/")
            os.system("chmod +x BetterXP.desktop")
            os.system("sudo cp BetterXP.desktop /usr/share/applications")
            try:
                os.system("sudo cp BetterXP.desktop "+user3)
            except:
                try:
                    os.system("sudo cp BetterXP.desktop "+user5)
                except:
                    print("Bazı hatalarla karşılaşıldı, kurulum yarıda kesildi.\nBetterXP Installer kapatılıyor...")
                    time.sleep(3)
                    exit()
            os.system("sudo cp ml.mukonqi.pkexec.betterxp.policy /usr/share/polkit-1/actions")
            os.system("chmod +x betterxp.py && sudo cp betterxp.py /usr/bin/betterxp")
            myusernameadd=open('/usr/local/bin/BetterXP/whoami.txt', "w")
            myusernameadd.write(user1)
            myusernameadd.close()
            print("BetterXP kuruldu. Umarız BetterXP sizin daha iyi bir deneyim yaşamanızı sağlar.\nBetterXP Installer kapatılıyor...")
            time.sleep(3)
            exit()
        elif islem == "bilgi":
            print("BetterXP Installer, BetterXP'ı kurmanızı sağlayan bir araçtır.")
            print("Lisans: GPL 3.0")
            kapat = input('BetterXP Installer "evet" yazdığınız an kapanacaktır:')
            if kapat == "evet":
                exit()
            else:
                print("Yanlış bir cevap girdiniz.\nBetterXP Installer kapatılıyor...")
                time.sleep(3)
                exit()
        elif islem == "çıkış":
            exit()
        else:
            print("Yanlış bir cevap girdiniz.\nBetterXP Installer kapatılıyor...")
            time.sleep(3)
            exit()
    elif sonuc == "hayır":
        print("Verdiğiniz cevaba göre, kullandığınız dağıtım ya da onun taban aldığı dağıtım yanlış algılandı. Lütfen bunu bize bildirin.\nBetterXP Installer kapatılıyor...")
        time.sleep(3)
        exit()
    else:
        print("Yanlış bir cevap girdiniz.\nBetterXP Installer kapatılıyor.")
        time.sleep(3)
        exit()
#Desteklenmeyen dağıtımlar:
else:
    print("Kullandığınız GNU/Linux veya Linux dağıtımını BetterXP ve BetterXP Installer tam anlamıyla desteklemiyor.")
    other = input("Hangi komutu çalıştırmak istersiniz?(bilgi/çıkış):")
    if other == "bilgi":
        print("BetterXP Installer, BetterXP'ı kurmanızı sağlayan bir araçtır.")
        print("Lisans: GPL 3.0")
        kapat = input('BetterXP Installer "evet" yazdığınız an kapanacaktır:')
        if kapat == "evet":
            exit()
        else:
            print("Yanlış bir cevap girdiniz.\nBetterXP Installer kapatılıyor.")
            time.sleep(3)
            exit()   
    elif other == "çıkış":
        exit()
    else:
        print("Yanlış bir cevap girdiniz.\nBetterXP Installer kapatılıyor.")
        time.sleep(3)
        exit()    