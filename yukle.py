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

# Gerekli modülleri içe aktarma:
import os

# Yükleyici kısım:
def main():
    if os.path.isfile(debian):
        os.system(" apt install python3 python3-tk")
    elif os.path.isfile(fedora):
        os.system(" dnf install python3-tkinter")
    elif os.path.isfile(solus):
        os.system(" eopkg it python3-tkinter")
    os.system("chmod +x metterxp.desktop")
    os.system(" mv metterxp.desktop /usr/share/applications")
    os.system(" mv python3.policy /usr/share/polkit-1/actions")
    os.system("chmod +x metterxp.py &&  mv metterxp.py /usr/bin/metterxp")
    if os.path.isfile(solus):
        os.system("cd /usr ;  mkdir local ; cd local ;  mkdir bin")
    os.system(" mkdir /usr/local/bin/metterxp")
    os.system(" mkdir /usr/local/bin/metterxp/modules")
    os.system(" mv modules/* /usr/local/bin/metterxp/modules")
    os.system(" mv icon.png /usr/local/bin/metterxp")
    os.system(" mv LICENSE /usr/local/bin/metterxp")     
    if os.path.isfile("/usr/share/applications/metterxp.desktop") or os.path.isfile("/usr/share/polkit-1/actions/python3.policy") or os.path.isfile("/usr/bin/metterxp") or os.path.isdir("/usr/local/bin/metterxp"):
        print("\nKurulum tamamlandı, umarız MetterXP amacına uygun şekilde size yardımcı olur.\nMetterXP yükleyicisi kapatılıyor...")
        exit()
    else:
        print("\nHata! Kurulum başarısız.\n\nMetterXP yükleyicisi kapatılıyor...")
        exit() 
        
# Lisans koşulları:
def entry():
    kosul=input("MetterXP yükleyicisine hoşgeldiniz!\n\nMetterXP ile yükleyicisi GNU General Public License, Version 3.0 altında lisanslanmıştır.\nBu lisansı şurada görüntüleyebilirsiniz: https://www.gnu.org/licenses/gpl-3.0-standalone.html\nLisansın koşullarını kabul ediyorsanuz 'devam',\nLisansın koşullarını kabul etmiyorsanız 'çıkış' yazınız.\nSeçiminiz: ")
    if kosul == 'devam':
        main()
    if kosul == 'çıkış':
        print("\nMetterXP yükleyicisi kapatılıyor...")
#İşletim sistemi kontrolü:
debian="/etc/debian_version"
fedora="/etc/fedora-release"
solus="/etc/solus-release"
if os.name == "nt":
    print("Hata!\nMetterXP NT çekirdeğini kullanan işletim sistemlerinde çalışmaz.\nLütfen şu üç GNU/Linux dağıtımından birini temel alan bir GNU/Linux dağıtımıyla programı açmayı deneyiniz:\nDebian GNU/Linux, Fedora Linux, Solus\n\nMetterXP yükleyicisi kapatılıyor...")
    exit()
elif os.path.isfile(debian):
    entry()
elif os.path.isfile(fedora):
    entry()
elif os.path.isfile(solus):
    entry()
else:
    print("Hata!\nKullandığınız işletim sistemini/dağıtımı MetterXP tam anlamıyla desteklemiyor.\nLütfen şu üç GNU/Linux dağıtımından birini temel alan bir GNU/Linux dağıtımıyla programı açmayı deneyiniz:\nDebian GNU/Linux, Fedora Linux, Solus\n\nMetterXP yükleyicisi kapatılıyor...")
    exit()
