#!/usr/bin/env python3

# LICENSE !!!!!
## Copyright (C) 2022, 2023 MuKonqi (Muhammed Abdurrahman)
## Apiutaller is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## Apiutaller is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with Apiutaller.  If not, see <https://www.gnu.org/licenses/>.

# README !!!!!
## Dear developer,
### You can make comment lines if you want skip some steps.
### You must set up variables in below.
### In the your program README file(s) you must specify that the user should run the Apiutaller with root user.
### If you are going to use it without changing the main code, just set in the section below variables according to the warnings.
### You must read variables warnings.
### When you want to update Apiutaller, simply copy the main code section right after the 'VARIABLES' section below from https://github.com/MuKonqi/apiutaller/blob/main/apiutaller.py link.

# VARIABLES !!!!!
## Warning! Folder names must end with this: /
## Warning! You must use "" when you don't use any.
## Warning! If your file doesn't have <> in its name, don't type it. It was written by MuKonqi as the file name would go there.
appname="MetterXP" # Option: "<your program name>"
appfolder="/usr/bin/" # Option: "<your main code folder>"
appfileold="metterxp.py" # Option: "<your main code file old name>"
appfilenew="metterxp" # Option: "<your main code file new name>"
policyfile="io.github.mukonqi.metterxp.policy" # Options: "<your policy file>" and any
appdesktopfile="metterxp.desktop" # Options: "<your desktop file>" and any
mainappfolder="/usr/local/bin/" # Options: "<your way to main app folder>" and any
mainappfoldername="metterxp" # Options: "<your main app folder name for icons, modules etc.>" and any
licensename="GPLv3" # # Options: "<your program's license>" and any
appdev="MuKonqi" # Option: "<your name>"
appcopyright="Copyright (C) 2021, 2022, 2023 MuKonqi (Muhammed Abdurrahman)" # Option: "<your copyright nofication>"
applicense='MetterXP is free software: you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\n\nMetterXP is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License\nalong with MetterXP.  If not, see <https://www.gnu.org/licenses/>.' # Option: "<important section from your program's license>" 
debian_apt_support="true" # Options: For true "true", and for false "false"
debian_apt_dependencies="git python3 python3-tk curl" # Options: "<your program's dependencies>" and any
fedora_dnf_support="true" # Options: For true "true", and for false "false"
fedora_dnf_dependencies="git python3 python3-tkinter curl" # Options: "<your program's dependencies>" and any
arch_pacman_support="false" # Options: For true "true", and for false "false"
arch_pacman_dependencies=any # Options: "<your program's dependencies>" and any
opensuse_zypper_support="false" # Options: For true "true", and for false "false"
opensuse_zypper_dependencies=any # Options: "<your program's dependencies>" and any
rhel_yum_support="false" # Options: For true "true", and for false "false"
rhel_yum_dependencies=any # Options: "<your program's dependencies>" and any
solus_eopkg_support="true" # Options: For true "true", and for false "false"
solus_eopkg_dependencies="git python3 python3-tkinter curl" # Options: "<your program's dependencies>" and any
void_xbps_support="false" # Options: For true "true", and for false "false"
void_xbps_dependencies=any # Options: "<your program's dependencies>" and any
pisi_pisi_support="false" # Options: For true "true", and for false "false"
pisi_pisi_dependencies=any # Options: "<your program's dependencies>" and any
other_gnulinux_support="false" # Options: For true "true", and for false "false"
python_pip_dependencies=any # Options: "<your program's dependencies>" and any
python3_pip3_dependencies=any # Options: "<your program's dependencies>" and any

# !!!!! MAIN CODE !!!!!

Apiutaller="v2.0"

import os
import time
import sys
from sys import platform

args=sys.argv[1:]
lang="default"
r=0
ls=0

if not os.getuid() == 0:
    exit("Only root can run Apiutaller!\nSadece kök Apiutaller'i çalıştırabilir!")

def main_install():
    def final():
        if r == 0:
            if lang == "en":
                exit("Successful, "+appname+" installed on your system.")
            elif lang == "tr":
                exit("Başarılı, "+appname+" sisteminize yüklendi.") 
    
    if python_pip_dependencies != any:
        if not os.path.isfile("/usr/bin/pip") or not os.path.isfile("/bin/pip"):
            if lang == "default" or lang == "en":
                print("Pip is not found. If Apiutaller supports pip installation on the distribution you are using, the installation will start.")
            if lang == "default" or lang == "tr":
                print("Pip bulunamadı. Apiutaller kullandığınız dağıtımda pip kurulumunu destekliyorsa kurulum başlayacaktır.")  
            if os.path.isfile("/etc/debian_version"):
                os.system("apt install -y python-pip")
            elif os.path.isfile("/etc/fedora-release"):
                os.system("dnf install -y python-pip")
            elif os.path.isfile("/bin/pacman") or os.path.isfile("/usr/bin/pacman"):
                os.system("pacman -S -y python2-pip --noconfirm")
            elif os.path.isfile("/usr/bin/yum") and not os.path.isfile("/etc/fedora-release"):
                os.system("yum install -y epel-release python-pip")
            elif os.path.isfile("/usr/bin/zypper"):
                os.system("zypper install --non-interactive python-pip")
            elif os.path.isfile("/etc/solus-release"):
                os.system("eopkg install -y pip")
            elif os.path.isdir("/etc/xbps.d"):
                os.system("xbps-install -y python-pip")
            else:
                if lang == "default" or lang == "en":
                    exit("Apiutaller can not install pip on the distribution you are using.")
                if lang == "default" or lang == "tr":
                    exit("Apiutaller kullandığınız dağıtıma pip yükleyemez.")        
        os.system("pip install "+python_pip_dependencies)
    elif python3_pip3_dependencies != any:
        if not os.path.isfile("/usr/bin/pip3") or not os.path.isfile("/bin/pip3"):
            if lang == "default" or lang == "en":
                print("Pip3 is not found. If Apiutaller supports pip3 installation on the distribution you are using, the installation will start.")
            if lang == "default" or lang == "tr":
                print("Pip3 bulunamadı. Apiutaller kullandığınız dağıtımda pip3 kurulumunu destekliyorsa kurulum başlayacaktır.")  
            if os.path.isfile("/etc/debian_version"):
                os.system("apt install -y python3-pip")
            elif os.path.isfile("/etc/fedora-release"):
                os.system("dnf install -y python3-pip")
            elif os.path.isfile("/bin/pacman") or os.path.isfile("/usr/bin/pacman"):
                os.system("pacman -S -y python-pip --noconfirm")
            elif os.path.isfile("/usr/bin/yum") and not os.path.isfile("/etc/fedora-release"):
                os.system("yum install -y epel-release python-pip")
            elif os.path.isfile("/usr/bin/zypper"):
                os.system("zypper install --non-interactive python3-pip")
            elif os.path.isfile("/etc/solus-release"):
                os.system("eopkg install -y pip")
            elif os.path.isdir("/etc/xbps.d"):
                os.system("xbps-install -y python3-pip")
            else:
                if lang == "default" or lang == "en":
                    exit("Apiutaller can not install pip3 on the distribution you are using.")
                if lang == "default" or lang == "tr":
                    exit("Apiutaller kullandığınız dağıtıma pip3 yükleyemez.")                    
        os.system("pip3 install "+python3_pip3_dependencies)

    os.system("chmod +x *")

    if not os.path.isdir(appfolder):
        os.system("mkdir "+appfolder)
    os.system("cd app ; chmod +x "+appfileold+" ; cp "+appfileold+" "+appfolder+appfilenew)
    if os.path.isfile(appfolder+appfilenew):
        if policyfile == any and appdesktopfile == any and mainappfolder == any and mainappfoldername == any:
            final()    
    else:
        if lang == "en":
            print("First installation step didn't succeed.")
        elif lang == "tr":
            print("Birinci kurma adımı başarısız.")        

    if policyfile != any:
        if not os.path.isdir("/usr/share/polkit-1/actions"):
            os.system("mkdir /usr/share/polkit-1/actions")
        os.system("cd app ; chmod +x "+policyfile+" ; cp "+policyfile+" /usr/share/polkit-1/actions/")
        if os.path.isfile("/usr/share/polkit-1/actions/"+policyfile):
            if appdesktopfile == any and mainappfolder == any and mainappfoldername == any:
                final()
        else:
            if lang == "en":
                print("Second installation step didn't succeed.")
            elif lang == "tr":
                print("İkinci kurma adımı başarısız.")   
    if appdesktopfile != any:
        if not os.path.isdir("/usr/share/applications"):
            os.system("mkdir /usr/share/applications")
        os.system("cd app ; cp "+appdesktopfile+" /usr/share/applications")
        if os.path.isfile("/usr/share/applications/"+appdesktopfile):
            if mainappfolder == any and mainappfoldername == any:
                final()     
        else:
            if lang == "en":
                print("Third installation step didn't succeed.")
            elif lang == "tr":
                print("üçüncü kurma adımı başarısız.") 
    
    if mainappfolder != any and mainappfoldername != any:
        if not os.path.isdir(mainappfolder):
            if mainappfolder == "/usr/local/bin/":
                os.system("mkdir /usr/local/ ; mkdir /usr/local/bin/")
            else:
                os.system("mkdir "+mainappfolder)
        os.system("mkdir "+mainappfolder+mainappfoldername)
        os.system("cd app ; cp -r * "+mainappfolder+mainappfoldername)
        if policyfile != any:
            os.system("cd "+mainappfolder+mainappfoldername+" ; rm "+policyfile)
        if appdesktopfile != any:
            os.system("cd "+mainappfolder+mainappfoldername+" ; rm "+appdesktopfile)
        os.system("cd "+mainappfolder+mainappfoldername+" ; rm "+appfileold)
        os.system("mkdir "+mainappfolder+mainappfoldername+"/apiutaller")
        os.system("cp apiutaller.py "+mainappfolder+mainappfoldername+"/apiutaller")
        if os.path.isdir(mainappfolder+mainappfoldername):
            final()       
        else:
            if lang == "en":
                print("Last installation step didn't succeed.")
            elif lang == "tr":
                print("Son kurma adımı başarısız.")           

def control_and_install():
    if os.path.isfile("/etc/debian_version"):
        if debian_apt_dependencies != any and debian_apt_support == "true":
            os.system("apt install -y "+debian_apt_dependencies)
            main_install()
        elif debian_apt_dependencies == any and debian_apt_support == "true":
            main_install()
        elif debian_apt_support == "false":
            if lang == "en":
                exit("Fatal error!\nYou can't install "+appname+" because Debian GNU/Linux based distributions not supported from "+appname+". If you think this is a mistake, please contact with "+appdev+".")
            elif lang == "tr":
                exit("Ölümcül hata!\nSiz "+appname+" uygulamasını yükleyemezsiniz çünkü Debian GNU/Linux tabanlı dağıtımlar "+appname+" tarafından desteklenmiyor. Bunu hata olduğunu düşünüyorsanız "+appdev+" ile iletişime geçin.")        


    elif os.path.isfile("/etc/fedora-release"):
        if fedora_dnf_dependencies != any and fedora_dnf_support == "true":
            os.system("dnf install -y "+fedora_dnf_dependencies)
            main_install()
        elif fedora_dnf_dependencies == any and fedora_dnf_support == "true":
            main_install()
        elif fedora_dnf_support == "false":
            if lang == "en":
                exit("Fatal error!\nYou can't install "+appname+" because Fedora Linux based distributions not supported from "+appname+". If you think this is a mistake, please contact with "+appdev+".")
            elif lang == "tr":
                exit("Ölümcül hata!\nSiz "+appname+" uygulamasını yükleyemezsiniz çünkü Fedora Linux tabanlı dağıtımlar "+appname+" tarafından desteklenmiyor. Bunu hata olduğunu düşünüyorsanız "+appdev+" ile iletişime geçin.")        

    elif os.path.isfile("/bin/pacman") or os.path.isfile("/usr/bin/pacman"):
        if arch_pacman_dependencies != any and arch_pacman_support == "true":
            os.system("pacman -S -y "+arch_pacman_dependencies+" --noconfirm")
            main_install()
        elif arch_pacman_dependencies == any and arch_pacman_support == "true":
            main_install()
        elif arch_pacman_support == "false":
            if lang == "en":
                exit("Fatal error!\nYou can't install "+appname+" because Arch Linux based distributions not supported from "+appname+". If you think this is a mistake, please contact with "+appdev+".")
            elif lang == "tr":
                exit("Ölümcül hata!\nSiz "+appname+" uygulamasını yükleyemezsiniz çünkü Arch Linux tabanlı dağıtımlar "+appname+" tarafından desteklenmiyor. Bunu hata olduğunu düşünüyorsanız "+appdev+" ile iletişime geçin.")          

    elif os.path.isfile("/usr/bin/yum") and not os.path.isfile("/etc/fedora-release"):
        if rhel_yum_dependencies != any and rhel_yum_support == "true":
            os.system("yum install -y "+rhel_yum_dependencies)
            main_install()
        elif rhel_yum_dependencies == any and rhel_yum_support == "true":
            main_install()
        elif rhel_yum_support == "false":
            if lang == "en":
                exit("Fatal error!\nYou can't install "+appname+" because the distribution with yum package manager you are using not supported from "+appname+". If you think this is a mistake, please contact with "+appdev+".")
            elif lang == "tr":
                exit("Ölümcül hata!\nSiz "+appname+" uygulamasını yükleyemezsiniz çünkü sizin kulladığınız dağıtım ile yum paket yöneticisi "+appname+" tarafından desteklenmiyor. Bunu hata olduğunu düşünüyorsanız "+appdev+" ile iletişime geçin.")         

    elif os.path.isfile("/usr/bin/zypper"):
        if opensuse_zypper_dependencies != any and opensuse_zypper_support == "true":
            os.system("zypper install --non-interactive "+opensuse_zypper_dependencies)
            main_install()
        elif opensuse_zypper_dependencies == any and opensuse_zypper_support == "true":
            main_install()
        elif opensuse_zypper_support == "false":
            if lang == "en":
                exit("Fatal error!\nYou can't install "+appname+" because OpenSUSE not supported from "+appname+". If you think this is a mistake, please contact with "+appdev+".")
            elif lang == "tr":
                exit("Ölümcül hata!\nSiz "+appname+" uygulamasını yükleyemezsiniz çünkü OpenSUSE "+appname+" tarafından desteklenmiyor. Bunu hata olduğunu düşünüyorsanız "+appdev+" ile iletişime geçin.")  

    elif os.path.isfile("/etc/solus-release"):
        if solus_eopkg_dependencies != any and solus_eopkg_support == "true":
            os.system("eopkg install -y "+solus_eopkg_dependencies)
            main_install()
        elif solus_eopkg_dependencies == any and solus_eopkg_support == "true":
            main_install()
        elif solus_eopkg_support == "false":
            if lang == "en":
                exit("Fatal error!\nYou can't install "+appname+" because Solus not supported from "+appname+". If you think this is a mistake, please contact with "+appdev+".")
            elif lang == "tr":
                exit("Ölümcül hata!\nSiz "+appname+" uygulamasını yükleyemezsiniz çünkü Solus "+appname+" tarafından desteklenmiyor. Bunu hata olduğunu düşünüyorsanız "+appdev+" ile iletişime geçin.")         

    elif os.path.isfile("/etc/pisilinux-release"):
        if pisi_pisi_dependencies != any and pisi_pisi_support == "true":
            os.system("pisi install -y "+pisi_pisi_dependencies)
            main_install()
        elif pisi_pisi_dependencies == any and pisi_pisi_support == "true":
            main_install()
        elif pisi_pisi_support == "false":
            if lang == "en":
                exit("Fatal error!\nYou can't install "+appname+" because Pisi GNU/Linux not supported from "+appname+". If you think this is a mistake, please contact with "+appdev+".")
            elif lang == "tr":
                exit("Ölümcül hata!\nSiz "+appname+" uygulamasını yükleyemezsiniz çünkü Pisi GNU/Linux "+appname+" tarafından desteklenmiyor. Bunu hata olduğunu düşünüyorsanız "+appdev+" ile iletişime geçin.")         

    elif os.path.isdir("/etc/xbps.d"):
        if void_xbps_dependencies != any and void_xbps_support == "true":
            os.system("xbps-install -y "+void_xbps_dependencies)
            main_install()
        elif void_xbps_dependencies == any and void_xbps_support == "true":
            main_install()
        elif void_xbps_support == "false":
            if lang == "en":
                exit("Fatal error!\nYou can't install "+appname+" because the Void Linux not supported from "+appname+". If you think this is a mistake, please contact with "+appdev+".")
            elif lang == "tr":
                exit("Ölümcül hata!\nSiz "+appname+" uygulamasını yükleyemezsiniz çünkü Void Linux "+appname+" tarafından desteklenmiyor. Bunu hata olduğunu düşünüyorsanız "+appdev+" ile iletişime geçin.")        

    elif platform == "linux":
        if other_gnulinux_support == "true":
            main_install()
        else:
            if lang == "en":
                exit("Fatal error!\nYou can't install "+appname+" because the distribution you are using not supported from "+appname+". If you think this is a mistake, please contact with "+appdev+".")
            elif lang == "tr":
                exit("Ölümcül hata!\nSiz "+appname+" uygulamasını yükleyemezsiniz çünkü sizin kulladığınız dağıtım "+appname+" tarafından desteklenmiyor. Bunu hata olduğunu düşünüyorsanız "+appdev+" ile iletişime geçin.")
    else:
        if lang == "en":
            exit("Fatal error!\nYou can't install "+appname+" because the OS you are using not supported from "+appname+". If you think this is a mistake, please contact with "+appdev+".")
        elif lang == "tr":
            exit("Ölümcül hata!\nSiz "+appname+" uygulamasını yükleyemezsiniz çünkü sizin kullanıdığınız İS "+appname+" tarafından desteklenmiyor. Bunu hata olduğunu düşünüyorsanız "+appdev+" ile iletişime geçin.")
    


def main_uninstall():
    os.system("cd "+appfolder+" ; rm "+appfilenew)
    if os.path.isfile(appfolder+appfilenew):
        if lang == "default" or lang == "en":
            exit("First uninstallation step didn't succeed.")
        elif lang == "default" or lang == "tr":
            exit("Birinci kaldırma adımı başarısız.")
            
    if policyfile != any:    
        os.system("cd /usr/share/polkit-1/actions ; rm "+policyfile)
        if os.path.isfile("/usr/share/polkit-1/actions/"+policyfile):
            if lang == "default" or lang == "en":
                exit("Second uninstallation step didn't succeed.")
            elif lang == "default" or lang == "tr":
                exit("İkinci kaldırma adımı başarısız.")
    
    if appdesktopfile != any:
        os.system("cd /usr/share/applications ; rm "+appdesktopfile)
        if os.path.isfile("/usr/share/applications/"+appdesktopfile):
            if lang == "default" or lang == "en":
                exit("Third uninstallation step didn't succeed.")
            elif lang == "default" or lang == "tr":
                exit("Üçüncü kaldırma adımı başarısız.")

    if mainappfolder != any and mainappfoldername != any:
        os.system("cd "+mainappfolder+" ; rm -rf "+mainappfoldername)
        if os.path.isdir(mainappfolder+mainappfoldername):
            if lang == "en":
                exit("Last uninstallation step didn't succeed.")
            elif lang == "tr":
                exit("Son kaldırma adımı başarısız.")
    
    if r == 0:
        if lang == "en":
            exit("Succesfull, "+appname+" is removed on your system. You can share your feedback with "+appdev+".")
        elif lang == "tr":
            exit("Başarılı ,"+appname+" sisteminizden kaldırıldı. Geri bildiriminizi "+appdev+" ile paylaşabilirsiniz.")

def main_reinstall():
    global r
    r=1
    main_uninstall()
    if lang == "en":
        print("Uninstallation is completed. Installation is starting.")
    elif lang == "tr":
        print("Kaldırma tamamlandı. Yüklemeye geçiliyor.")
    control_and_install()
    if lang == "en":
        exit("Succesfull, "+appname+" is reinstalled on your system.")
    elif lang == "tr":
        exit("Başarılı, "+appname+" siteminizde yeniden yüklendi.")



def operation():
    if lang == "en":
        oa=input("What do you want to do? You should type 'install' if you want to install "+appname+", 'reinstall' if you want to reinstall, 'uninstall' to uninstall; type anything to exit Apiutaller. Your decision: ")
    elif lang == "tr":
        oa=input("Ne yapmak istersiniz? Eğer "+appname+" programını kurmak istiyorsanız 'kur', yeniden kurmak istiyorsanız 'yeniden kur', kaldırmak için 'kaldır'; Apiutaller'den çıkış için herhangi bir şey yazınız. Kararınız: ")
    if oa == "install" or oa == "kur":
        control_and_install()
    elif oa == "reinstall" or oa == "yeniden kur":
        main_reinstall()
    elif oa == "uninstall" or oa == "kaldır":
        main_uninstall()
    else:
        exit()
        
        
def license():
    global ls
    if lang == "en":
        if ls == 0:
            print("Welcome to the Apiutaller "+Apiutaller+" setup wizard, which is currently set to "+appname+"!\nApiutaller are licensed under the GPLv3.\n"+appname+" is licensed with "+licensename+".\n")
        li=input("Type 'y' if you accept these licenses, 'n' if you don't; type 's' to show information about this licenses. Decision: ")
        if li == "y":
            operation()
        elif li == "n":
            if ls == 0:
                print("\n\n\nA important section about the GPLv3 used by Apiutaller wizard and copyright information are below.\n\n    Copyright (C) 2022, 2023 MuKonqi (Muhammed Abdurrahman)\nApiutaller is free software: you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\nApiutaller is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\nYou should have received a copy of the GNU General Public License\nalong with Apiutaller.  If not, see <https://www.gnu.org/licenses/>.\n\n\nCopyright information and important section about "+licensename+" for "+appname+" is below.\n\n    "+appcopyright+"\n"+applicense+"\n\n\nThe text above was automatically printed in case it might change your mind.\n\n")
            confirm=input("If you don't accept licenses again, Apiutaller will be closed.\nWrite 'y' if you accept licenses, anything else if you don't accept licenses. Decision: ")
            if confirm == 'y':
                operation()
            else:
                exit("You didn't reaccept the licenses, the Apiutaller setup wizard was closed.")
        elif li == "s":
            ls=1
            print("\n\n\nA important section about the GPLv3 used by Apiutaller wizard and copyright information are below.\n\n    Copyright (C) 2022, 2023 MuKonqi (Muhammed Abdurrahman)\nApiutaller is free software: you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\nApiutaller is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\nYou should have received a copy of the GNU General Public License\nalong with Apiutaller.  If not, see <https://www.gnu.org/licenses/>.\n\n\nCopyright information and important section about "+licensename+" for "+appname+" is below.\n\n    "+appcopyright+"\n"+applicense+"\n\n\n")
            license()
        else:
            license()
    elif lang == "tr": 
        if ls == 0:
            print("Şuanda "+appname+" için ayarlı Apiutaller "+Apiutaller+" kurulum sihirbazına hoş geldiniz!\nApiutaller, GPLv3 ile lisanslanmıştır.\n"+appname+" ise "+licensename+" ile lisanslanmıştır.\n")  
        li=input("Bu lisansları kabul ediyorsanız 'e', etmiyorsanız 'h'; bu lisanslarla ilgili bilgi göstermek için 'g' yazınız. Karar: ")
        if li == "e":
            operation()
        elif li == "h":
            if ls == 0:
                print("\n\n\nApiutaller sihirbazının kullandığı GPLv3 ile ilgili önemli bölüm ve telif hakkı bilgisi aşağıdadır.\n\n    Copyright (C) 2022, 2023 MuKonqi (Muhammed Abdurrahman)\nApiutaller is free software: you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\nApiutaller is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\nYou should have received a copy of the GNU General Public License\nalong with Apiutaller.  If not, see <https://www.gnu.org/licenses/>.\n\n\nTelif hakkı bilgisi ve "+licensename+" hakkında önemli bölüm, "+appname+" aşağıdadır.\n\n    "+appcopyright+"\n"+applicense+"\n\n\nYukarıdaki metin belki fikrinizin değişmesinde sebep olur diye otomatik yazdırıldı.\n\n")
            confirm=input("Tekrar lisansları kabul etmezseniz, Apiutaller kapatılacak.\nLisansları kabul ediyorsanız 'e', kabul etmiyorsanız herhangi bir şey yazınız. Karar :")
            if confirm == 'e':
                operation()
            else:
                exit("Lisansları tekrardan kabul etmediniz, Apiutaller kurulum sihirbazı kapatıldı.")
        elif li == "g":
            ls=1
            print("\n\n\nApiutaller sihirbazının kullandığı GPLv3 ile ilgili önemli bölüm ve telif hakkı bilgisi aşağıdadır.\n\n    Copyright (C) 2022, 2023 MuKonqi (Muhammed Abdurrahman)\nApiutaller is free software: you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\nApiutaller is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\nYou should have received a copy of the GNU General Public License\nalong with Apiutaller.  If not, see <https://www.gnu.org/licenses/>.\n\n\nTelif hakkı bilgisi ve "+licensename+" hakkında önemli bölüm, "+appname+" için aşağıdadır.\n\n    "+appcopyright+"\n"+applicense+"\n\n\n")
            license()
        else:
            license()

def welcome():
    global lang
    print("     Copyright (C) 2022, 2023 MuKonqi (Muhammed Abdurrahman)")
    language=input("For choosing English type 'en', for choosing Turkish type 'tr'.\nİngilizce seçmek için 'en', Türkçe seçmek için 'tr' yazınız.\n  Decision / Karar: ")
    if lang == "default" and language == 'en':
        lang="en"
        license()
    elif lang == "default" and language == 'tr':
        lang="tr"
        license()
    else:
        welcome()
    
if "--install" in args or "--kur" in args:
    print("Copyright (C) 2022, 2023 MuKonqi (Muhammed Abdurrahman)")
    print("If you do not press Ctrl+C within 3 seconds, the installation will start and you will be deemed to have accepted both the GPLv3 license used by Apiutaller and the "+licensename+" license used by the "+appname+" program.")
    time.sleep(3)
    control_and_install()
elif "--reinstall" in args or "--yeniden kur" in args:
    print("Copyright (C) 2022, 2023 MuKonqi (Muhammed Abdurrahman)")
    print("If you do not press Ctrl+C within 3 seconds, the reinstallation will start and you will be deemed to have accepted both the GPLv3 license used by Apiutaller and the "+licensename+" license used by the "+appname+" program.")
    time.sleep(3)
    main_reinstall()    
elif "--uninstall" in args or "--sil" in args:
    print("Copyright (C) 2022, 2023 MuKonqi (Muhammed Abdurrahman)")
    print("If you do not press Ctrl+C within 3 seconds, the uninstallation will start and you will be deemed to have accepted both the GPLv3 license used by Apiutaller and the "+licensename+" license used by the "+appname+" program.")
    time.sleep(3)
    main_uninstall()
else:
    welcome()