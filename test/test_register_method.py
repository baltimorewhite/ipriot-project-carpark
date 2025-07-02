import unittest
from src.car_park import CarPark
from display import Display
from sensor import EntrySensor, ExitSensor

class TestCarParkRegister(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("Registration Test Lot", 50)
        self.display = Display("Main Gate")
        self.entry_sensor = EntrySensor("North Entrance")
        self.exit_sensor = ExitSensor("South Exit")

    def test_register_display_adds_to_registered_displays(self):
        self.car_park.register(self.display)
        self.assertIn(self.display, self.car_park.registered_displays)

    def test_register_sensor_sets_reference(self):
        self.car_park.register(self.entry_sensor)
        self.assertEqual(self.entry_sensor.car_park_reference, self.car_park)

    def test_register_unsupported_component_raises_error(self):
        with self.assertRaises(TypeError):
            self.car_park.register("not a valid component")
