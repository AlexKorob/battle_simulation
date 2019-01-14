import unittest
from unittest.mock import patch
from models.units.soldier import Soldier


class TestSoldier(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Test Soldier---------------")

    @classmethod
    def tearDownClass(cls):
        print("End Test Soldier-----------")
        print()

    def setUp(self):
        self.soldier = Soldier()

    def test_is_alive(self):
        self.assertTrue(self.soldier.alive)

    def test_is_dead(self):
        self.soldier.get_damage(100)
        self.assertFalse(self.soldier.alive)

    def test_has_recharge(self):
        self.assertTrue(self.soldier.recharge)

    def test_is_recharged(self):
        """ Check readying to battle """
        self.assertTrue(self.soldier.recharged)

    def test_is_damage(self):
        self.assertTrue(self.soldier.damage())

    def test_is_attack(self):
        self.assertGreater(self.soldier.attack(), 0)

    def test_levelup_after_gave_damage(self):
        self.soldier.damage()
        self.assertEqual(self.soldier.experience, 1)

    @patch("models.units.soldier.randint")
    def test_recharge_in_interval(self, mock_randint):
        mock_randint.return_value = 100
        self.assertEqual(Soldier().recharge, 100)
        mock_randint.return_value = 1000
        self.assertEqual(Soldier().recharge, 1000)

        mock_randint.assert_called_with(100, 1000)
