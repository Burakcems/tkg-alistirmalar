import pytest
from alistirma import indirim_orani, sepet_toplami, en_pahali_urun

def test_indirim_orani_sinirlar():
    assert indirim_orani(0) == 0
    assert indirim_orani(99) == 0
    assert indirim_orani(100) == 5
    assert indirim_orani(499) == 5
    assert indirim_orani(500) == 10
    assert indirim_orani(999) == 10
    assert indirim_orani(1000) == 15
    assert indirim_orani(1500) == 15

def test_indirim_orani_negatif():
    with pytest.raises(ValueError):
        indirim_orani(-1)
    with pytest.raises(ValueError):
        indirim_orani(-50)

def test_sepet_toplami():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 2},
        {"urun": "simit", "fiyat": 15, "adet": 3},
        {"urun": "tost", "fiyat": 60, "adet": 1},
    ]
    assert sepet_toplami(sepet) == 145

def test_sepet_toplami_bos():
    assert sepet_toplami([]) == 0

def test_sepet_toplami_sifir_adet():
    with pytest.raises(ValueError):
        sepet_toplami([{"urun": "su", "fiyat": 5, "adet": 0}])

def test_sepet_toplami_negatif_adet():
    with pytest.raises(ValueError):
        sepet_toplami([{"urun": "su", "fiyat": 5, "adet": -2}])

def test_en_pahali_urun():
    sepet = [
        {"urun": "kalem", "fiyat": 15, "adet": 5},
        {"urun": "çanta", "fiyat": 300, "adet": 1},
        {"urun": "defter", "fiyat": 45, "adet": 2}
    ]
    assert en_pahali_urun(sepet) == "çanta"

def test_en_pahali_urun_esit_fiyat():
    sepet = [
        {"urun": "kırmızı kalem", "fiyat": 50, "adet": 1},
        {"urun": "mavi kalem", "fiyat": 50, "adet": 1},
        {"urun": "silgi", "fiyat": 10, "adet": 3}
    ]
    assert en_pahali_urun(sepet) == "kırmızı kalem"

def test_en_pahali_urun_bos():
    assert en_pahali_urun([]) is None