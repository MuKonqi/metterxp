
# ***BetterXP***
**Son kullanıcı için tasarlandı.**

BetterXP, program kurma/kaldırma, masaüstü ortamı kurma/kaldırma, sistem güncelleme, çeşitli yapılandırma özelliklerine (GRUB, Terminal, Plank, WINE...), paket yöneticisi kurma vs. özelliklere sahiptir.

Temel: Terminalden kurtulun, Sürüm 2

Yazıldığı dil: Python, Version 3 (Python 3)

Arayüz: Tkinter

Platform desteği: Debian GNU/Linux, Fedora Linux, Solus tabanları

Lisans: GNU General Public License 3
__________________________________________________________________________________________________________________________________________________________________
# ***Kurulum***
BetterXP'ı yükleyecek **BetterXP Installer**'ı çalıştırmak için yapmanız gerekenler şunlardır:
1. İlk başta Git ile Python3 paketini yüklemek gerekir. Bunun için:

Eğer Debian tabanlı bir GNU/Linux dağıtımı kullanıyorsanız ```sudo apt install git python3 -y```; 

Eğer Fedora tabanlı bir GNU/Linux dağıtımı kullanıyorsanız ```sudo dnf install git python3 -y```; 

Eğer Solus tabanlı bir GNU/Linux dağıtımı kullanıyorsanız ```sudo eopkg it git python3 -y``` komutunu terminale yazmanız gerekir.

2. Şimdi ise terminale şu komutu girin: ```git clone https://github.com/MuKonqi/BetterXP.git ; cd BetterXP/Installer ; sudo python3 installer.py ; cd 
; rm -rf BetterXP```

Bundan sonra BetterXP Installer, bilgisayarınıza uygun BetterXP sürümünü kuracaktır. İyi günler dileriz.
