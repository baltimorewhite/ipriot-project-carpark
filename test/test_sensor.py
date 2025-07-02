import unittest
from src.sensor import EntrySensor, ExitSensor
from src.car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("Sensor Test Site", 2)
        self.entry_sensor = EntrySensor("Entry Gate", self.car_park)
        self.exit_sensor = ExitSensor("Exit Gate", self.car_park)

    def test_entry_sensor_adds_car_to_car_park(self):
        self.entry_sensor.detect_vehicle("XYZ-123")
        self.assertIn("XYZ-123", self.car_park.registered_plate_numbers)
        self.assertEqual(self.car_park.available_bays, 1)

    def test_exit_sensor_removes_car_from_car_park(self):
        self.car_park.add_car("XYZ-123")
        self.exit_sensor.detect_vehicle("XYZ-123")
        self.assertNotIn("XYZ-123", self.car_park.registered_plate_numbers)
        self.assertEqual(self.car_park.available_bays, 2)

    def test_entry_and_exit_sequence(self):
        self.entry_sensor.detect_vehicle("TEST-456")
        self.exit_sensor.detect_vehicle("TEST-456")
        self.assertEqual(self.car_park.available_bays, 2)
