import unittest
from models.units.soldier import Soldier


class TestSoldier(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Test Soldier---------------")

    @classmethod
    def tearDownClass(cls):
        print("End Test Soldier-----------")
        print()

    def test_is_alive(self):
        self.assertTrue(Soldier().alive)

    def test_is_dead(self):
        soldier = Soldier()
        soldier.get_damage(100)
        self.assertFalse(soldier.alive)

    def test_has_recharge(self):
        self.assertTrue(Soldier().recharge)

    def test_is_recharged(self):
        """ Check readying to battle """
        self.assertTrue(Soldier().recharged)

    def test_is_damage(self):
        self.assertTrue(Soldier().damage())

    def test_is_attack(self):
        self.assertGreater(Soldier().attack(), 0)
