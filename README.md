# TKG alıştırmaları

Dönem boyunca her hafta bu repoya yeni bir klasör eklenecek: `hafta02/`, `hafta03/`, ...
Her klasörde o haftanın alıştırması ve onu kontrol eden testler var (ör. `alistirma.py` ve `test_alistirma.py`).
Her `push` yaptığınızda GitHub Actions testleri sizin yerinize çalıştırır.

## Dönem başında bir kez

1. Bu sayfanın sağ üstündeki **Fork** düğmesine basın, ardından **Create fork** deyin.
   Artık hesabınızda bu reponun bir kopyası var.
2. Kendi fork'unuzda **Actions** sekmesini açın ve
   **I understand my workflows, go ahead and enable them** düğmesine basın.
   Bunu yapmazsanız testler hiç çalışmaz.
3. Kendi fork'unuzu bilgisayarınıza indirin:
   ```bash
   git clone https://github.com/KULLANICI-ADINIZ/REPO-ADI.git
   cd REPO-ADI
   ```
4. Kendi fork'unuzun linkini paylaşın. Dönem boyunca yalnızca bu link kullanılacak.

## Her hafta

1. **Yeni haftayı alın.** Önce elinizdeki değişiklikleri commit'leyip `push` edin.
   Sonra GitHub'da kendi fork'unuzda **Sync fork → Update branch** düğmesine basın ve bilgisayarınızda:
   ```bash
   git pull
   ```
   Yeni `haftaNN/` klasörü gelir.
2. **Alıştırmayı yapın.** O haftanın klasörüne girip `alistirma.py` dosyasındaki fonksiyonları doldurun.
   Kendi bilgisayarınızda deneyin:
   ```bash
   cd hafta02
   python -m pip install pytest
   python -m pytest -v
   ```
3. **Her fonksiyonu bitirdiğinizde commit'leyip gönderin.**
   ```bash
   git add alistirma.py
   git commit -m "isaret fonksiyonu yazıldı"
   git push
   ```
4. **Sonucu görün.** Fork'unuzun **Actions** sekmesinde her hafta ayrı bir satırdır.
   Yeşil ✅ o haftanın tamam olduğunu, kırmızı ❌ bir şeyin eksik olduğunu gösterir.
   Kırmızıya tıklayıp hangi adımın başarısız olduğunu okuyun.

## Kurallar

- `test_alistirma.py` dosyalarını ve `.github/` klasörünü **değiştirmeyin**.
  Testleri değiştirerek geçmek alıştırmanın amacını ortadan kaldırır.
- Her hafta için o haftanın klasöründe en az **3 ayrı commit** yapın.
  Tek seferde hepsini göndermek Git kontrolünü geçmez.

## Her haftada kontrol edilenler

| Adım | Ne bakıyor? |
|---|---|
| Python testleri | `alistirma.py` içindeki fonksiyonlar doğru çalışıyor mu? |
| Git kontrolü | O haftanın klasöründe en az 3 commit yapılmış mı? |

## Sık karşılaşılan sorunlar

- **Actions sekmesi boş:** Dönem başındaki 2. adımı yapmadınız.
- **`git pull` "divergent branches" hatası veriyor:** Bilgisayarınızda push etmediğiniz commit var.
  `git pull --no-rebase` ile birleştirip `git push` yapın.
- **pytest "import file mismatch" hatası veriyor:** Testleri reponun ana klasöründen çalıştırdınız.
  Önce `cd hafta02` gibi o haftanın klasörüne girin.
