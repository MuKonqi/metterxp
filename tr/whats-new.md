---
layout: page-tr
title: MetterXP 2.0.0
---
# MetterXP 2.0.0
## Yenilikler: 

Çoklu dil desteği eklendi. Yeni dil: İngilizce


1.2-1 sürümündeki tema ile birlikte toplamda 10 adet tema 2.0.0 sürümünde eklendi.


Asıl MetterXP dosyasında os.system yerine subprocess.Popen'e geçildi. Bu, bazı modülleri başlatırken uygulamanın kasmış görünümünden kurtulmasını sağlarken aynı zamanda kullanıcının hep yeniden MetterXP'ı 
açmamasını sağladı.


Asıl MetterXP dosyasında "MetterXP'ı güncelle" butonu kaldırıldı, "MetterXP seçenekleri" butonu eklendi. 


Asıl MetterXP dosyasına MetterXP adında menü seçeneği eklendi. Bunda şu seçenekler vardır: MetterXP hakkında, MetterXP seçenekleri, MetterXP'ı güncelle, MetterXP'ı kaldır


yukle.py kurucusundan apiutaller kurucusuna ve silicisine geçildi.


Uygulamayı silmek için apiutaller'a ek olarak MetterXP'ı kaldır modülü yapıldı.


Flatpak uygulamalarını kurma/yeniden kurma/kaldırma eklendi.


Özel GUI uygulama başlatma eklendi.


Plank'ı yapılandırma özelliği kaldırıldı.


.bashrc dosyası için yeni bir sıfırlama seçeneği eklendi.


Bloat olan yerler azaltıldı.


Buton, metin, boşluk metini ve çokça şey yeniden adlandırıldı. Bu kodun daha derli toplu olmasını sağladı. Not: En sondaki n'ler o şeyin numarasıdır.

Eski: islemsecimbutonn, yazin, b_metinn

Yeni: buttonn, textn, spacen


Çoğu def()'lerin ve buton vs. şeylerin adı İngilizce yapıldı. Bu, global anlamda insanlara kolaylık sağlar.


python3.policy dosyası silindi, [io.github.mukonqi.metterxp](https://mukonqi.github.io/metterxp).policy eklendi. Bu, "Kimlik doğrulaması gerekli" yerine "MetterXP için kimlik doğrulaması gerekli" yazmasını sağladı ve uygulamayı silerken python3.policy dosyasına ihtiyaç duyan uygulamaların bozulmasını engelledi.