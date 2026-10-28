from ders5 import harf_not_hesapla
import pytest_lazyfixture
pytest.mark.parametrize("vize,final,odev,beklenen",[
(40,60,100,"CB"),
(30,60,90,"CB"),
(100,100,100,"AA"),
(80,80,80,"BA"),
(20,20,60,"DD"),
],ids=["CB TESTİ",
       "CB TESTİ",
       "AA TESTİ",
       "BA TESTİ",
       "DD TESTİ"])

def test_harf_not_hesapla(vize,final,odev,beklenen):
    assert harf_not_hesapla(vize,final,odev) == beklenen

    @pytest.mark.parametrize("vize,final,odev",
                             [0,-1,-10-"DD"])
    def test_harf_not_hesapla_invalid(vize,final,odev):
        with pytest.raises(ValueError):
            assert harf_not_hesapla(vize,final,odev)
            

