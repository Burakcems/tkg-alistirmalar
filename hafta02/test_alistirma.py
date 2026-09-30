# Bu dosyayı DEĞİŞTİRMEYİN. Her `test_` fonksiyonu bir alıştırmayı kontrol eder.
# Bir test başarısız olursa, hangi assert satırının tuttuğunu çıktıda görürsünüz.

from alistirma import isaret, donem_notu, harf_say, faktoriyel, gecenler


def test_isaret():
    assert isaret(5) == "pozitif"
    assert isaret(-3) == "negatif"
    assert isaret(0) == "sıfır"          # sınır
    assert isaret(1) == "pozitif"
    assert isaret(-1) == "negatif"


def test_donem_notu():
    assert round(donem_notu(50, 70), 2) == 62.0
    assert round(donem_notu(100, 100), 2) == 100.0
    assert round(donem_notu(0, 0), 2) == 0.0
    assert round(donem_notu(100, 0), 2) == 40.0   # vize ağırlığı
    assert round(donem_notu(0, 100), 2) == 60.0   # final ağırlığı


def test_harf_say():
    assert harf_say("merhaba", "a") == 2
    assert harf_say("merhaba", "z") == 0
    assert harf_say("", "a") == 0                 # boş metin
    assert harf_say("Ankara", "a") == 2           # büyük "A" sayılmaz
    assert harf_say("Ankara", "A") == 1


def test_faktoriyel():
    assert faktoriyel(5) == 120
    assert faktoriyel(1) == 1
    assert faktoriyel(0) == 1                     # sınır
    assert faktoriyel(10) == 3628800


def test_gecenler():
    assert gecenler([70, 45, 90]) == [70, 90]
    assert gecenler([60, 59]) == [60]             # tam sınır
    assert gecenler([10, 20]) == []
    assert gecenler([]) == []
    assert gecenler([95, 60, 100]) == [95, 60, 100]   # sıra bozulmamalı
