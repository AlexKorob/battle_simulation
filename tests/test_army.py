import unittest
import json
from models.army import Army
from models.squad import Squad


class TestArmy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('config_armies.json', 'r') as file:
            json_obj = json.load(file)

        cls.parameters = list(json_obj.values())
        print("Test Army---------------")

    @classmethod
    def tearDownClass(cls):
        print("End Test Army-----------")
        print()

    def setUp(self):
        self.all_armies = [Army(**parameter) for parameter in self.parameters]
        self.army = self.all_armies[0]

    def test_can_choose_targets(self):
        target = self.army.choose_targets(self.all_armies)
        self.assertIsInstance(target, list)
        for squad in target:
            self.assertIsInstance(squad, Squad)
            for own_squad in self.army.squads:
                self.assertNotEqual(squad, own_squad)

    def test_is_alive(self):
        self.assertTrue(self.army.alive)

    def test_is_dead(self):
        self.army.squads = []
        self.assertFalse(self.army.alive)
