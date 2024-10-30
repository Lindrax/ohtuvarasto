import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_neg_konstruktori(self):
        self.virheellinen = Varasto(-1, -1)
        self.assertAlmostEqual(self.virheellinen.tilavuus, 0)
        self.assertAlmostEqual(self.virheellinen.saldo,0)

    def test_liika_saldo(self):
        self.virhe = Varasto(5, 8)
        self.assertAlmostEqual(self.virhe.saldo, self.virhe.tilavuus)
    

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)
    
    def test_liika_lisays(self):
        self.varasto.lisaa_varastoon(20)
        
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_neg_lisays(self):
        holder = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, holder)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_ota_neg(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0.0)

    def test_liikaa(self):
        s= self.varasto.saldo
        x = self.varasto.ota_varastosta(20)
        self.assertAlmostEqual(s, x)

    def test_print(self):
        s = self.varasto.__str__()
        self.assertAlmostEqual(f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}", s )
