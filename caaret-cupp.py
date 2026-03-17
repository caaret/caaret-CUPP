import itertools

def caaret_cupp():
    print("--- caaret-CUPP Wordlist Generator ---")
    
    data = []
    
    kisi_isim = input("Ad: ").lower()
    kisi_soy = input("Soyad: ").lower()
    kisi_nick = input("Nickname: ").lower()
    kisi_yil = input("Doğum Yılı (YYYY): ")
    
    partner_isim = input("Partner Ad: ").lower()
    partner_yil = input("Partner Doğum Yılı (YYYY): ")
    
    hayvan = input("Evcil Hayvan Adı: ").lower()
    ozel_sayi = input("Şanslı Sayı/Şehir Plaka: ")

    words = [kisi_isim, kisi_soy, kisi_nick, partner_isim, hayvan]
    years = [kisi_yil, kisi_yil[2:], partner_yil, partner_yil[2:], "123", "1905", "1907", "1903", "34", ozel_sayi]
    special = ["!", "@", "*", "", "123"]

    words = [w for w in words if w]
    years = [y for y in years if y]

    wordlist = set() 

    for w in words:
        for y in years:
            for s in special:
                wordlist.add(f"{w}{y}{s}")
                wordlist.add(f"{w.capitalize()}{y}{s}") 

    if kisi_isim and partner_isim:
        wordlist.add(f"{kisi_isim}{partner_isim}")
        wordlist.add(f"{partner_isim}{kisi_isim}")

    for w in words:
        for s in ["!", "!!", "123", "34", "07"]:
            wordlist.add(f"{w}{s}")

    filename = f"{kisi_isim}_wordlist.txt"
    with open(filename, "w") as f:
        for pw in sorted(wordlist):
            f.write(pw + "\n")
            
    print(f"\n[+] İşlem Tamam! {len(wordlist)} adet şifre üretildi.")
    print(f"[+] Dosya Adı: {filename}")

caaret_cupp()