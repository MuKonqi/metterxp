import os
import time
#Giriş:
print("BetterXP Installer'a hoşgeldiniz!")
#İşletim sistemi kontrolü:
name=os.name
if name == "nt":
    print("BetterXP ve BetterXP Installer, NT çekirdeğini kullanan işletim sistemlerinde (Windows, ReactOS) çalışmaz.")
    print("BetterXP Installer kapatılıyor.")
    time.sleep(3)
    exit()
#Debian mı değil mi kontrolü:
if os.path.isfile('/etc/debian_version'):
    print("Şimdi aşağıda kullandığınız dağıtım ya da kullandığınız dağıtımın taban aldığı dağıtım ve paket yöneticisi gözükecektir. İşlemlerde buna göre yapılacaktır.")
    set_systembase="Dağıtım: Debian"
    set_packagemanager="Paket Yöneticisi: APT"
    print(set_systembase)     
    print(set_packagemanager)   
    sonuc = input("Bunlar doğru mu?(evet/hayır):")
    if sonuc == "evet":      
        islem = input("Lütfen BetterXP Installer'da çalıştırmak istediğiniz komutu seçiniz.(kur/kaldır/güncelle/bilgi/çıkış):")
        if islem == "kur":
            user="/home/"
            user1 = input("Kuruluma başlanması için kullanıcı adınızı girmeniz gerekmektedir:")
            user2="/Masaüstü/"
            user3=user+user1+user2
            user4="/Desktop/"
            user5=user+user1+user4
            print("Gerekli paketler yükleniyor. Lütfen sizde onay veriniz.")
            os.system("sudo apt install python3 python3-tk git snapd")
            os.system("sudo git clone https://github.com/androidprotmmas/BetterXP_Debian.git")
            os.system("sudo mv BetterXP_Debian BetterXP")
            os.system("cd BetterXP")
            os.system("sudo rm -rf .git")
            os.system("cd")
            os.system("sudo mv BetterXP /usr/local/bin/")
            os.system("git clone https://github.com/androidprotmmas/BetterXP_desktop.git")
            os.system("cd BetterXP_desktop")
            os.system("chmod +x BetterXP.desktop")
            try:
                os.system("sudo mv BetterXP.desktop "+user3)
            except:
                try:
                    os.system("sudo mv BetterXP.desktop "+user5)
                except:
                    print("Bazı hatalarla karşılaşıldı, kurulum yarıda kesildi.")
                    print("BetterXP Installer kapatılıyor.")
                    time.sleep(3)
                    exit()
            print("Az sonra karşınıza çıkacak pencerede kullanıcı adınızı tekrar girmeniz gerekecektir.")
            os.system("sudo apt install nano -y && sudo nano /usr/local/bin/BetterXP/whoami.txt")
            print("BetterXP kuruldu. Umarız BetterXP sizin daha iyi bir deneyim yaşamanızı sağlar.")
            print("BetterXP Installer kapatılıyor.")
            time.sleep(3)
            exit()
        elif islem == "kaldır":
            sil = input("Gittiğinize üzüldük, bundan emin misiniz?(evet/hayır)")
            if sil == "evet":
                os.system("cd /usr/local/bin && sudo rm -rf BetterXP")
                print("BetterXP başarıyla sisteminizden kaldırıldı.")
                time.sleep(3)
                exit()
        elif islem == "güncelle":
            os.system("sudo git clone https://github.com/androidprotmmas/BetterXP_Debian.git")
            os.system("sudo rm -rf /usr/local/bin/BetterXP/up.py")
            os.system("sudo mv BetterXP_Debian /usr/local/bin/BetterXP")
            os.system("sudo cp -r /usr/local/bin/BetterXP/BetterXP_Debian/up.py /usr/local/bin/BetterXP")
            os.system("sudo python3 /usr/local/bin/BetterXP/up.py")
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
#Fedora mı değil mi kontrolü:
elif os.path.isfile('/etc/fedora-release'):
    print("Şimdi aşağıda kullandığınız dağıtım ya da kullandığınız dağıtımın taban aldığı dağıtım ve paket yöneticisi gözükecektir. İşlemlerde buna göre yapılacaktır.")
    set_systembase="Dağıtım: Fedora"
    set_packagemanager="Paket Yöneticisi: DNF"
    print(set_systembase)     
    print(set_packagemanager)   
    sonuc = input("Bunlar doğru mu?(evet/hayır):")
    if sonuc == "evet":      
        islem = input("Lütfen BetterXP Installer'da çalıştırmak istediğiniz komutu seçiniz.(kur/kaldır/güncelle/bilgi/çıkış):")
        if islem == "kur":
            user="/home/"
            user1 = input("Kuruluma başlanması için kullanıcı adınızı girmeniz gerekmektedir:")
            user2="/Masaüstü/"
            user3=user+user1+user2
            user4="/Desktop/"
            user5=user+user1+user4
            print("Gerekli paketler yükleniyor. Lütfen sizde onay veriniz.")
            os.system("sudo dnf install python3 python3-tkinter git")
            os.system("sudo git clone https://github.com/androidprotmmas/BetterXP_Fedora.git")
            os.system("sudo mv BetterXP_Fedora BetterXP")
            os.system("cd BetterXP")
            os.system("sudo rm -rf .git")
            os.system("cd")
            os.system("sudo mv BetterXP /usr/local/bin/")
            os.system("git clone https://github.com/androidprotmmas/BetterXP_desktop.git")
            os.system("cd BetterXP_desktop")
            os.system("chmod +x BetterXP.desktop")
            try:
                os.system("sudo mv BetterXP.desktop "+user3)
            except:
                try:
                    os.system("sudo mv BetterXP.desktop "+user5)
                except:
                    print("Bazı hatalarla karşılaşıldı, kurulum yarıda kesildi.")
                    print("BetterXP Installer kapatılıyor.")
                    time.sleep(3)
                    exit()
            print("Az sonra karşınıza çıkacak pencerede kullanıcı adınızı tekrar girmeniz gerekecektir.")
            os.system("sudo dnf install nano -y && sudo nano /usr/local/bin/BetterXP/whoami.txt")
            print("BetterXP kuruldu. Umarız BetterXP sizin daha iyi bir deneyim yaşamanızı sağlar.")
            print("BetterXP Installer kapatılıyor.")
            time.sleep(3)
            exit()
        elif islem == "kaldır":
            sil = input("Gittiğinize üzüldük, bundan emin misiniz?(evet/hayır)")
            if sil == "evet":
                os.system("cd /usr/local/bin && sudo rm -rf BetterXP")
                print("BetterXP başarıyla sisteminizden kaldırıldı.")
                time.sleep(3)
                exit()
        elif islem == "güncelle":
            os.system("sudo git clone https://github.com/androidprotmmas/BetterXP_Fedora.git")
            os.system("sudo rm -rf /usr/local/bin/BetterXP/up.py")
            os.system("sudo mv BetterXP_Fedora /usr/local/bin/BetterXP")
            os.system("sudo cp -r /usr/local/bin/BetterXP/BetterXP_Fedora/up.py /usr/local/bin/BetterXP")
            os.system("sudo python3 /usr/local/bin/BetterXP/up.py")
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
        islem = input("Lütfen BetterXP Installer'da çalıştırmak istediğiniz komutu seçiniz.(kur/kaldır/güncelle/bilgi/çıkış):")
        if islem == "kur":
            user="/home/"
            user1 = input("Kuruluma başlanması için kullanıcı adınızı girmeniz gerekmektedir:")
            user2="/Masaüstü/"
            user3=user+user1+user2
            user4="/Desktop/"
            user5=user+user1+user4
            print("Gerekli paketler yükleniyor. Lütfen sizde onay veriniz.")
            os.system("sudo eopkg it python3 python3-tkinter git")
            os.system("sudo mkdir /usr/local ; sudo mkdir /usr/local/bin")
            os.system("sudo git clone https://github.com/androidprotmmas/BetterXP_Solus.git")
            os.system("sudo mv BetterXP_Solus BetterXP")
            os.system("cd BetterXP")
            os.system("sudo rm -rf .git")
            os.system("cd")
            os.system("sudo mv BetterXP /usr/local/bin/")
            os.system("git clone https://github.com/androidprotmmas/BetterXP_desktop.git")
            os.system("cd BetterXP_desktop")
            os.system("chmod +x BetterXP.desktop")
            try:
                os.system("sudo mv BetterXP.desktop "+user3)
            except:
                try:
                    os.system("sudo mv BetterXP.desktop "+user5)
                except:
                    print("Bazı hatalarla karşılaşıldı, kurulum yarıda kesildi.")
                    print("BetterXP Installer kapatılıyor.")
                    time.sleep(3)
                    exit()
            print("Az sonra karşınıza çıkacak pencerede kullanıcı adınızı tekrar girmeniz gerekecektir.")
            os.system("sudo eopkg it nano -y && sudo nano /usr/local/bin/BetterXP/whoami.txt")
            print("BetterXP kuruldu. Umarız BetterXP sizin daha iyi bir deneyim yaşamanızı sağlar.")
            print("BetterXP Installer kapatılıyor.")
            time.sleep(3)
            exit()
        elif islem == "kaldır":
            sil = input("Gittiğinize üzüldük, bundan emin misiniz?(evet/hayır)")
            if sil == "evet":
                os.system("cd /usr/local/bin && sudo rm -rf BetterXP")
                print("BetterXP başarıyla sisteminizden kaldırıldı.")
                time.sleep(3)
                exit()
        elif islem == "güncelle":
            os.system("sudo git clone https://github.com/androidprotmmas/BetterXP_Solus.git")
            os.system("sudo rm -rf /usr/local/bin/BetterXP/up.py")
            os.system("sudo mv BetterXP_Solus /usr/local/bin/BetterXP")
            os.system("sudo cp -r /usr/local/bin/BetterXP/BetterXP_Fedora/up.py /usr/local/bin/BetterXP")
            os.system("sudo python3 /usr/local/bin/BetterXP/up.py")
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