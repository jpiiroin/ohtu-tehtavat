import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_loytyy_pelaaja(self):
        pelaaja = self.statistics.search("Semenko")
        self.assertAlmostEqual(pelaaja.name, "Semenko")

    def test_ei_loydy_pelaaja(self):
        pelaaja = self.statistics.search("Simenko")
        assert pelaaja is None

    def test_testaa_tulostus(self):
        pelaaja = self.statistics.search("Gretzky")
        self.assertAlmostEqual(str(pelaaja), "Gretzky EDM 35 + 89 = 124")

    def test_testaa_joukkue(self):
        joukkue = self.statistics.team("EDM")
        joukkue = [i.name for i in joukkue]
        assert joukkue == ['Semenko', 'Kurri', 'Gretzky']

    def test_testaa_parhaat(self):
        parhaat = self.statistics.top_scorers(3)
        parhaat = [i.name for i in parhaat]
        assert parhaat == ['Gretzky', 'Lemieux', 'Yzerman', 'Kurri']

