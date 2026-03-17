caaret-CUPP (Custom User Passwords Profiler)

Bu modül, hedef kişi hakkında bilinen spesifik verileri kullanarak kişiselleştirilmiş bir Wordlist (Sözlük) oluşturmak için caaret tarafından geliştirilmiştir. Standart listelerin aksine, hedefin kişisel tercihlerini baz alarak çok daha yüksek başarı oranı sunar.
🧠 Çalışma Mantığı

İnsanlar genellikle şifrelerini hatırlaması kolay olan kişisel bilgilerinden türetirler. caaret-CUPP, girilen ham verileri (isim, doğum yılı, evcil hayvan vb.) alarak şu profesyonel işlemleri gerçekleştirir:

    Akıllı Kombinasyon: Verileri birbirleriyle çapraz eşleştirir (Örn: İsim + Yıl, Soyad + Nickname).

    Varyasyon Üretimi: Kelimelerin baş harflerini otomatik büyütür (Mami) veya tamamen küçük harfe (mami) çevirerek deneme sayısını artırır.

    Özel Karakter Entegrasyonu: Şifrelerin sonuna siber dünyada en çok kullanılan karakterleri (!, @, *) ve sayı dizilerini (123, 07) ekler.

    Optimizasyon: Aynı şifrenin birden fazla kez üretilmesini engelleyerek dosya boyutunu küçük, tarama hızını yüksek tutar.

📋 Giriş Parametreleri (Girdi Havuzu)
Alan	Örnek Girdi
Ad / Soyad	mami / caaret
Nickname	mami07
Doğum Yılı	2005 / 05
Partner / Çocuk	sevgi / 2026
Evcil Hayvan	boncuk
Şanslı Sayılar	34 / 1905
🚀 Mobil Kullanım ve Kayıt

Uygulama, üretilen listeyi Android cihazlarda en kolay erişilebilir nokta olan Download (İndirilenler) klasörüne otomatik olarak kaydeder.

    Dosya Yolu: /storage/emulated/0/Download/[isim]_wordlist.txt

    Format: Her satırda bir şifre olacak şekilde .txt formatında çıktı verir.

    Erişim: Dosya yöneticisinden direkt açılabilir ve diğer sızma testi araçlarına aktarılabilir.

🛠️ Teknik Özellikler

    Dil: Python

    Algoritma: itertools kütüphanesi ile yüksek hızlı çapraz eşleştirme.

    Uyumluluk: Üretilen listeler; Hash Breaker, Hydra, Medusa ve Metasploit gibi tüm profesyonel araçlarla tam uyumludur.
