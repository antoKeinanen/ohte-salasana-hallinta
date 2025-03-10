import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alustetaan(self):
        self.assertAlmostEqual(self.maksukortti.saldo, 1000)
    
    def test_kortille_voi_lisata_saldoa(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertAlmostEqual(self.maksukortti.saldo, 2000)

    def test_saldo_vahenee_kun_rahaa_on_riittavasti(self):
        self.maksukortti.ota_rahaa(500)
        self.assertAlmostEqual(self.maksukortti.saldo, 500)
    
    def test_saldo_ei_muutu_jos_rahaa_ei_ole(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertAlmostEqual(self.maksukortti.saldo, 1000)
    
    def test_kortilta_otto_palauttaa_true_jos_onnistui(self):
        onnistui = self.maksukortti.ota_rahaa(500)
        self.assertTrue(onnistui)
    
    def test_kortilta_otto_palauttaa_false_jos_ei_onnistunut(self):
        onnistui = self.maksukortti.ota_rahaa(2000)
        self.assertFalse(onnistui)