<!-- add-breadcrumbs -->
# Uygulama stratejisi

Operasyonlarınızı ERPNext'te yönetmeye başlamadan,
önce sisteme ve kullanılan terimlere aşina olmalısınız.
Bunun için uygulamanın iki aşamada gerçekleşmesini öneriyoruz.

* Bir ** Test Aşaması **, günlük işlemlerinizi temsil eden sahte kayıtları ve canlı verilere girmeye başladığımız ** Canlı Aşama **.

### Test Aşaması

   *  Kullanım Kılavuzunu Okuyun
   * [Https://erpnext.com] adresinde ücretsiz bir hesap oluşturun (https://erpnext.com) (denemenin en kolay yolu).
   * İlk Müşteri, Tedarikçi ve Ürününüzü oluşturun. Birkaç tane daha ekleyin, böylece onlara aşina olursunuz.
   * Öğelerinizi sınıflandırabilmeniz için Müşteri Grupları, Ürün Grupları, Depolar, Tedarikçi Grupları oluşturun.
   * Standart bir satış döngüsü tamamlayın - Potansiyel Müşteri> Fırsat> Teklif> Satış Siparişi> Teslimat Notu> Satış Faturası> Ödeme (Muhasebe Kayıt Girişi)
   * Standart bir satın alma döngüsü tamamlayın - Malzeme Talebi> Satınalma Siparişi> Satınalma Fişi> Ödeme (Muhasebe Kayıt Girişi).
   * Bir üretim döngüsü tamamlayın (varsa) - BOM> Üretim Planlama Aracı> İş Emri> Malzeme Sorunları
   * Gerçek bir yaşam senaryosunu sisteme kopyalayın.
   * Özel alanlar oluşturun, baskı formatları vb.
   
   ### Canlı Aşama

ERPNext'e aşina olduktan sonra, canlı verilerinizi girmeye başlayın!

  * Test verilerinin bulunduğu hesabını temizleyin veya daha iyisi, yeni bir kurulum başlatın.
  * İşlemlerinizi silmek istiyorsanız, Öğe, Müşteri, Tedarikçi, BOM vb. Ana verilerinizi değil, Şirketinizin işlemlerini silip yeni başlatabilirsiniz. Bunu yapmak için, Ayarlar> Kurulum> Şirket üzerinden Şirket Kaydını açın ve Şirket formunun altındaki ** Şirket İşlemlerini Sil ** düğmesine tıklayarak Şirketinizin işlemlerini silin.
  * Ayrıca [https://erpnext.com] adresinde (https://erpnext.com) yeni bir hesap oluşturabilir ve 14 günlük ücretsiz denemeyi kullanabilirsiniz. [ERPNext'i dağıtmanın daha fazla yolunu öğrenin] (erpnext ile başlarken)
  * Tüm modülleri Müşteri Grupları, Ürün Grupları, Depolar, Malzeme Listeleri vb. İle ayarlayın.
  * Veri Alma Aracı'nı kullanarak Müşterileri, Tedarikçileri, Öğeleri, Kişileri ve Adresleri Alın.
  * Stok Mutabakatı Aracını kullanarak açılış stoğunu alın.
  * Kayıt girdisi ile açılış muhasebesi girişleri oluşturun ve olağan Satış Faturaları ve Satınalma Faturaları oluşturun.
  * Yardıma ihtiyacınız varsa, [destek satın alabilirsiniz] (https://erpnext.com/pricing) veya [kullanıcı forumunda sorun] (https://discuss.erpnext.com).

{Sonraki}