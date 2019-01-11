import unittest
from models.units.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Test Vehicle---------------")

    @classmethod
    def tearDownClass(cls):
        print("End Test Vehicle-----------")
        print()

    def setUp(self):
        self.vehicle = Vehicle(3)

    def test_is_dead(self):
        self.vehicle.get_damage(100)
        self.assertFalse(self.vehicle.alive)

    def test_is_alive(self):
        self.assertTrue(self.vehicle.alive)

    def test_count_operators(self):
        self.vehicle = Vehicle(operators=0)
        self.assertGreaterEqual(len(self.vehicle.operators), 1)

    def test_is_damage(self):
        self.assertGreater(self.vehicle.damage(), 0)

    def test_has_recharge(self):
        self.assertTrue(self.vehicle.recharge)

    def test_is_recharged(self):
        """ Check readying to battle """
        self.assertTrue(self.vehicle.recharged)

    def test_is_attack(self):
        self.assertGreater(self.vehicle.attack(), 0)
