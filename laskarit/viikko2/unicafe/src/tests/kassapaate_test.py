import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaatteen_saldo_alustetaan_oikein(self):
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassapaatteen_edulliset_on_alustettu_oikein(self):
        self.assertAlmostEqual(self.kassapaate.edulliset, 0)

    def test_kassapaatteen_maukkat_on_alustettu_oikein(self):
        self.assertAlmostEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_kun_saldo_riittää_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_toimii_kun_saldo_riittää_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_vaihtoraha_edullinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertAlmostEqual(vaihtoraha, 60)

    def test_kateisosto_vaihtoraha_maukas(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertAlmostEqual(vaihtoraha, 100)

    def test_tilastot_kasvavat_kateisostolla_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertAlmostEqual(self.kassapaate.edulliset, 1)

    def test_tilastot_kasvavat_kateisostolla_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_raha_ei_riita_edullinen_kassa_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_raha_ei_riita_maukas_kassa_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_raha_ei_riita_tilastot_ei_muutu_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertAlmostEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_raha_ei_riita_tilastot_ei_muutu_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_raha_ei_riita_vaihtoraha_edullinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertAlmostEqual(vaihtoraha, 100)

    def test_kateisosto_raha_ei_riita_vaihtoraha_maukas(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertAlmostEqual(vaihtoraha, 100)

    def test_kortti_osta_edullinen(self):
        kortti = Maksukortti(10000)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertTrue(onnistui)
        self.assertAlmostEqual(kortti.saldo, 10000 - 240)

    def test_kortti_osta_maukas(self):
        kortti = Maksukortti(100000)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertTrue(onnistui)
        self.assertAlmostEqual(kortti.saldo, 100000 - 400)
    
    def test_kortti_tilastot_edullinen(self):
        kortti = Maksukortti(10000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertAlmostEqual(self.kassapaate.edulliset, 1)
    
    def test_kortti_tilastot_maukas(self):
        kortti = Maksukortti(10000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 1)
    
    def test_korti_raha_ei_riita_edullinen(self):
        kortti = Maksukortti(100)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertFalse(onnistui)
        self.assertAlmostEqual(kortti.saldo, 100)
        self.assertAlmostEqual(self.kassapaate.edulliset, 0)

    def test_korti_raha_ei_riita_maukas(self):
        kortti = Maksukortti(100)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertFalse(onnistui)
        self.assertAlmostEqual(kortti.saldo, 100)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 0)
    
    def test_kassan_rahamaara_ei_muutu_kortilla_edullinen(self):
        kortti = Maksukortti(10000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kassan_rahamaara_ei_muutu_kortilla_maukas(self):
        kortti = Maksukortti(10000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kortille_lataaminen(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)
        self.assertAlmostEqual(kortti.saldo, 500)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000 + 500)
    
    def test_kortille_lataaminen_epaonnistuu(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, -1)
        self.assertAlmostEqual(kortti.saldo, 0)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_raha_euroina(self):
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
