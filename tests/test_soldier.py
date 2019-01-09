import unittest
from unittest.mock import patch
from models.units.soldier import Soldier
from random import randint


class TestSoldier(unittest.TestCase):
    def test_is_alive(self):
        self.assertTrue(Soldier().alive())

    def test_is_dead(self):
        soldier = Soldier()
        soldier.get_damage(100)
        self.assertFalse(soldier.alive())

    def test_recharge(self):
        
