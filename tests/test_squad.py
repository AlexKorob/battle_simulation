import unittest
import json
from models.squad import Squad


class TestSquad(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('config_armies.json', 'r') as file:
            json_obj = json.load(file)

        army_1 = list(json_obj.values())[0]
        cls.units = army_1["units"]

        print("Test Squad---------------")

    @classmethod
    def tearDownClass(cls):
        print("End Test Squad-----------")
        print()

    def setUp(self):
        self.squad = Squad(self.units, "squad")

    def test_can_not_take_more_then_10_units(self):
        with self.assertRaises(AssertionError):
            self.squad = Squad({"Soldier": {
                                  "numbers": 6},
                                "Vehicle": {
                                  "operators": 3,
                                  "numbers": 5}}, "squad")

    def test_is_attack(self):
        self.assertTrue(self.squad.attack())

    def test_is_damage(self):
        self.assertTrue(self.squad.damage())

    def test_is_alive(self):
        self.assertTrue(self.squad.alive)

    def test_is_dead(self):
        self.squad.get_damage(100)
        self.assertFalse(self.squad.alive)

    def test_can_take_damage(self):
        health_before_damage = self.squad.health
        self.squad.get_damage(1)
        health_after_damage = self.squad.health
        self.assertGreater(health_before_damage, health_after_damage)
