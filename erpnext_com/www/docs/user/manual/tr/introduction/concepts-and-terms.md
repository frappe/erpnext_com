<!-- add-breadcrumbs -->
# Kavramlar ve Terimler

Uygulamaya başlamadan önce, şu terminolojiyi tanıyalım:
ERPNext'te bazı temel kavramlar kullanılmıştır.

* * *
### Temel konseptler

#### Şirket

Bu, ERPNext'in ayarlandığı Şirket kayıtlarını temsil eder. Aynı kurulumla,
her biri farklı bir tüzel kişiliği temsil eden birden fazla Şirket kaydı
oluşturabilirsiniz. Her bir Şirket için muhasebe farklı olacaktır,
ancak Müşteri, Tedarikçi ve Kalem kayıtlarını paylaşacaklardır.

> Kurulum> Şirket

#### Müşteri

Bir müşteriyi temsil eder. Müşteri, bir birey veya kuruluş olabilir.
Her Müşteri için birden fazla Kontak ve Adres oluşturabilirsiniz.

> Satış> Müşteri

#### Tedarikçi

Mal veya hizmet tedarikçisini temsil eder. Telekom şirketiniz bir Tedarikçi,
hammadde Tedarikçiniz de öyle. Yine, Tedarikçi, bir birey veya kuruluş
olabilir ve birden fazla Kontak ve Adrese sahip olabilir.

> Satın Alma> Tedarikçi

#### Ürün

Satın alınan, satılan veya üretilen ve özgün şekilde tanımlanmış bir Ürün, 
alt ürün veya Hizmet.

> Stok> Ürün

#### Muhasebe

Bir Hesap, finansal ve ticari işlemlerin yapıldığı bir başlıktır.
Örneğin, “Seyahat Giderleri” bir hesap, “Müşteri Zoe”, “Tedarikçi Mae” birer hesaplardır.
ERPNext Müşteriler ve Tedarikçiler için otomatik olarak hesaplar oluşturur.

> Muhasebe> Hesap Tablosu

#### Adres

Bir adres, bir Müşterinin veya Tedarikçinin konum ayrıntılarını gösterir.
Bunlar Genel Müdürlük, Fabrika, Depo, Dükkan vb. Farklı yerler olabilir.

> Satış> Adres

#### İrtibat

Bireysel İrtibatlar bir Müşteriye veya Tedarikçiye aittir veya bunlardan
 bağımsız irtibatlardır. Bir kişinin e-posta ve telefon numarası gibi
bir adı ve iletişim bilgileri vardır.

> Satış> İrtibatlar

#### İletişim

Bir Kontak veya ön satış ile tüm İletişimin bir listesi. Sistemden gönderilen
tüm e-postalar İletişim tablosuna eklenir.

> Destek> İletişim

#### Fiyat listesi

Bir Fiyat Listesi, farklı fiyat planlarının saklanabileceği bir yerdir.
Belirli bir Listede depolanan bir dizi Ürün fiyatına verdiğiniz bir addır.

> Satış> Fiyat Listesi


> Satın Alma> Fiyat Listesi

* * *
#### Muhasebe

#### Mali yıl

Mali Yılı veya Muhasebe Yılı'nı temsil eder. Aynı anda birden fazla Mali Yılı
çalıştırabilirsiniz. Her Mali Yılın bir başlangıç tarihi ve bitiş tarihi vardır
ve işlemler yalnızca bu dönemde kaydedilebilir. Bir mali yılı “kapattığınızda”,
bir sonraki mali yıl için bakiyeleri “açılış” bakiyeleri olarak aktarılır.

> Kurulum> Şirket> Mali Yıl

#### Maliyet Merkezi

Bir Maliyet Merkezi bir Hesap gibidir, ancak tek fark, yapısının işinizi
Hesaplardan daha yakından temsil etmesidir. Örneğin, Hesap Planınızda
harcamalarınızı türüne göre (örneğin, seyahat, pazarlama vb.) Ayırabilirsiniz.
Maliyet Merkezleri Tablosunda, bunları ürün grubuna veya iş grubuna göre
(örneğin, çevrimiçi satışlar, perakende satışlar vb.) Ayırabilirsiniz.

> Hesaplar> Maliyet Merkezleri Tablosu

#### Journal Entry

A document that contains General Ledger (GL) entries and the sum of Debits and
Credits of those entries is the same. In ERPNext you can update Payments,
Returns, etc., using Journal Entries.

> Accounts > Journal Entry

#### Satış Faturası

Ürünlerin (mal veya hizmetlerin) teslimatı için Müşterilere gönderilen fatura.

> Hesaplar> Satış Faturası

#### Satınalma Faturası

Malların (mal veya hizmetlerin) teslimatı için Tedarikçi tarafından gönderilen bir fatura.

> Hesaplar> Satınalma Faturası

#### Para birimi

ERPNext, işlemlerinizi birden fazla para biriminde yapmanızı sağlar.
Hesap defteriniz için yalnızca bir para birimi var. Faturalarınızı farklı
para birimlerinde ödemeli olarak kaydederken, tutar belirtilen dönüşüm oranı
ile varsayılan para birimine dönüştürülür.

> Kurulum> Para Birimi

* * *

### Satış

#### Müşteri Grubu

Genellikle pazar segmentine dayalı olarak Müşterilerin sınıflandırılması.

> Satış> Kurulum> Müşteri Grubu

#### Potansiyel Müşteri

Gelecekteki bir iş kaynağı olabilecek bir kişi. Bir fırsat, yaratabilir.
(“bir satışa yol açabilir”).

> CRM> Potensiyel Müşteri

#### Fırsat

Potansiyel bir satış. (“iş fırsatı”).

> CRM> Fırsat

#### Teklif

Müşterinin bir ürünü veya hizmeti fiyatlandırma isteği.

> Satış> Teklif

#### Satış Siparişi

Müşteri tarafından onaylanan bir Ürünün (ürün veya hizmet) 
teslimatını ve fiyatınıgösteren bir not. Teslimatlar,
İş Emirleri ve Faturalar Satış Siparişleri bazında yapılır.

> Satış> Satış Siparişi

#### Bölge

Satış yönetimi için coğrafi bir alan sınıflandırması.
Bölgeler için hedefler belirleyebilirsiniz ve her satış bir
Bölgeye bağlanır.

> Satış> Kurulum> Bölge

#### Satış Ortağı
Şirketin ürünlerini genellikle bir komisyon için satan üçüncü
 taraf bir distribütör / satıcı / satış ortağı / komisyon acentesi.
 
> Satış> Kurulum> Satış Ortağı

#### Satis Personeli

Müşteri ile iletişim kuran ve anlaşmaları sonuçlandıran kişi.
Satış Personeli için hedefler belirleyebilir ve bunları
işlemlerde etiketleyebilirsiniz.

> Satış> Kurulum> Satış Personeli

* * *

### Satınalma

#### Satınalma Siparişi

Bir Tedarikçiye, belirtilen Malları belirtilen maliyet, miktar,
tarih ve diğer şartlar altında teslim etmek için verilen sözleşme.

> Satın Alma> Satınalma Siparişi

#### Malzeme Talebi

Bir Kullanıcı tarafından yapılan veya bir Ürün Öğesi satın almak
için Üretim Planında yeniden sipariş seviyesine veya öngörülen miktara
göre ERPNext tarafından otomatik olarak oluşturulan bir istek.

> Satın Alma> Malzeme Talebi

* * *

### Depo (Envanter)

#### Depo

Stok girişlerinin yapıldığı Depo.

> Stok> Depo

#### Stok Girişi

Depodan Depoya veya bir Depodan diğerine malzeme aktarımı.

> Stok> Stok Girişi

#### İrsaliye

Sevkıyat için adet içeren öğelerin listesi. Bir irsaliye,
gönderdiğiniz yerden Depoya ait Ürün stoklarını azaltacaktır.
Bir Müşteri Siparişine karşı genellikle bir irsaliye oluşturulur.

> Stok> İrsaliye

#### Satınalma İrsaliyesi

Bir Satınalma Siparişine karşı, belirli bir Ürünün
Tedarikçiden alındığını belirten evrak.

> Stok> Satınalma İrsaliyesi

#### Seri Numarası

Bir Ürünün belirli birimlerine verilen benzersiz bir sayı.

> Hisse Senedi> Seri Numarası

#### Yığın

Bir grup olarak satın alınabilecek veya üretilebilecek
belirli bir Maddenin birimler grubuna verilen bir sayı.

> Stok> Yığın

#### Stok Muhasebe Girişi

Bir depodan diğerine, tüm malzeme hareketi için toplu bir Tablodur.
Bu; Stok Girişi, İrsaliye, Satın Alma Fişi ve Satış Faturası(POS)
yapıldığında güncellenen tablodur.

#### Stok Mutabakatı

Bir elektronik tablo (CSV) dosyasından birden fazla öğenin stoğunu güncelleyin.

> Stok> Araçlar> Stok Mutabakatı

#### Kalite Kontrol

Tedarikçiden alınan ya da müşteriye teslim edildilecek bir ürünün
belirli kriterlere göre kontrolünün yapılması için hazırlanmış bir evrak.

> Stok> Kalite Kontrol

#### Ürün Grubu

Ürünlerin bir sınıflandırması.

> Stok> Ayar> Ürün Grubu

* * *

### İnsan Kaynakları Yönetimi

#### Çalışan

Şirket de istihdam edilen veya ayrılmış olan bir kişinin kaydı.

> İnsan Kaynakları> Çalışan

#### İzin Talepleri

Onaylanmış veya reddedilmiş izin taleblerinin kaydı.

> İnsan Kaynakları> İzin Talepleri

#### İzin Tipi

Bir izin türü (örneğin; Hastalık İzni, Doğum İzni, vb.).

> İnsan Kaynakları> İzin ve Devam > İzin Tipi

#### Bordro Girişi

Çalışanlar için birden fazla Bordro Fişi oluşturulmasında yardımcı olan bir araç.

> İnsan Kaynakları> Bordro Girişi

#### Maaş Bordrosu

Bir Çalışana verilen aylık maaşın bir kaydı.

> İnsan Kaynakları> Maaş Bordrosu

#### Maaş Yapısı

Çalışanların maaşının (kazançlarının), vergi ve diğer sosyal
güvenlik kesintilerinin tüm bileşenlerini tanımlayan bir şablon.

> İnsan Kaynakları> Maaş ve Bordro> Maaş Yapısı


#### Değerleme

Bir Çalışanın belirli parametreler temelinde belirli bir süre boyunca
 performansının kaydı.

> İnsan Kaynakları> Değerleme

#### Değerleme Şablonu

Çalışanların performansının farklı parametrelerini ve belirli bir rol
için ağırlıklarını kaydeden bir şablon.

> İnsan Kaynakları> Çalışan Kurulumu> Değerleme Şablonu

#### Devamsızlık

Belirli bir günde bir Çalışanın varlığını veya yokluğunu gösteren bir kayıt.

> İnsan Kaynakları> Devamsızlık

* * *

### Üretim

#### Malzeme Listesi (BOM)

Bir Ürün üretmek için gereken operasyonların ve malzeme miktarlarının bir listesi.
Satın alımları planlamak ve ürün maliyetlerini oluşturmak için bir Malzeme Listesi (BOM) kullanılır.

> Üretim> Malzeme Listesi

#### İş İstasyonu

Bir ürün Listesi için operasyonun gerçekleştiği yer. Ürünün doğrudan maliyetinin hesaplamasında faydası vardır.

> Üretim> İş İstasyonu

#### İş Emri

Belirli bir ürünün belirtilen miktarlarda ve şekilde üretilemesi için hazırlanmış evrak.

> Üretim> İş Emri

#### Üretim Planlama Aracı

Belirli bir süreçte Açık Satış Siparişlerine dayalı İş Emri ve Satınalma Talebinin otomatik olarak yaratılması için bir araç.

> Üretim> Üretim Planlama Aracı

* * *

### Web sitesi

#### Blog yazısı

ERPNext web sitesi modülünden oluşturulan web sitesinin “Blog” bölümünde yer alan kısa bir makale. Blog, "Web Günlüğü" nin kısa bir şeklidir.

> Web Sitesi> Blog Yazısı

#### İnternet sayfası

ERPNext tarafından oluşturulan web sitesinde bir URL'ye (web adresi) sahip web sayfası.

> Web Sitesi> Web Sayfası

* * *

### Kurulum / Özelleştirme

#### Özel alan

Bir form / masada kullanıcı tanımlı bir alan.

> Kurulum> ERPNext'i Özelleştir> Özel Alan

#### Global Defaults

Bu, çeşitli parametreler için varsayılan değerleri ayarladığınız bölümdür.
sistemi.

> Kurulum> Veri> Genel Varsayılanlar

#### Yazdırma Başlığı

Sadece yazdırma işelemi üzerinde ayarlanabilen bir başlık.
Örneğin, “Teklif” veya “Pro forma Fatura” başlıklı bir Teklif yazdırmak istiyorsunuz.

> Kurulum> Marka ve Baskı> Baskı Başlıkları

#### Şartlar ve koşullar

Sözleşme şartlarınızın metni.

> Satış> Kurulum> Şartlar ve Koşullar

#### Ölçü Birimi (UOM)

Bir Ürün için miktarın nasıl ölçüleceği. Örneğin, Kg, Adet, Çift, Paket, vb.

> Stok> Kurulum> UOM

{Sonraki}