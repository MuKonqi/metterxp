---
layout: page
title: Kurulum
---
## Kurulum
Öncelikle bilgisayarınızda kurulumun başlaması için şunların olması gerekmektedir: Git, Python3, sudo/su/doas (genellikle sudo kullanılır)<br />
Eğer Debian GNU/Linux kullanıyorsanız 'sudo apt install git python3 -y',<br />
Eğer Fedora Linux kullanıyorsanız 'sudo dnf install git python3 -y',<br />
Eğer Solus kullanıyorsanız 'sudo eopkg install git python3 -y' yazınız.<br />
Eğer sudo kullanıyorsanız 'git clone https://github.com/MuKonqi/metterxp.git ; cd metterxp ; sudo python3 yukle.py' yazınız.<br />
Eğer su kullanıyorsanız 'git clone https://github.com/MuKonqi/metterxp.git ; cd metterxp ; su' yazınız. Sonra 'cd /home/kullaniciadiniz/metterxp ; python3 yukle.py' yazınız. Not: kullanıcıadiniz yerine kullanıcı adı gelmelidir!<br />
Eğer doas kullanıyorsanız 'git clone https://github.com/MuKonqi/metterxp.git ; cd metterxp ; doas python3 yukle.py' yazınız.