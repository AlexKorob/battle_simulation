import unittest
import json
from models.army import Army
from models.squad import Squad
from unittest.mock import patch


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

    @patch("models.army.choice", return_value='weakest')
    def test_army_can_choose_the_most_weakly_squad(self, mock_choose_list):
        target = self.all_armies[1].squads[0]
        target.get_damage(20)
        self.assertIs(self.army.choose_target(self.all_armies), self.all_armies[1].squads[0])

    @patch("models.army.choice", return_value='stronger')
    def test_army_can_choose_the_most_stronger_squad(self, mock_choose_list):
        target = [self.all_armies[1].squads[0], len(self.all_armies[1].squads[0].members)]

        for army in self.all_armies[1:]:
            for squad in army.squads:
                if len(squad.members) > target[1]:
                    target[0] = squad
                    target[1] = len(squad.members)

        self.assertIs(self.army.choose_target(self.all_armies), target[0])

    def test_is_alive(self):
        self.assertTrue(self.army.alive)

    def test_is_dead(self):
        self.army.squads = []
        self.assertFalse(self.army.alive)
