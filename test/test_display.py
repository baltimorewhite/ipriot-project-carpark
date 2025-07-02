import unittest
from src.display import Display

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display(location="Gate A")

    def test_display_starts_with_empty_message(self):
        self.assertEqual(self.display.message, "")

    def test_update_message_with_available_bays(self):
        data = {"available_bays": 42}
        self.display.update(data)
        self.assertEqual(self.display.message, "Available bays: 42")

    def test_update_message_with_multiple_fields(self):
        data = {
            "available_bays": 17,
            "temperature": 22,
            "time": "10:45 AM"
        }
        self.display.update(data)
        expected_message = "Available bays: 17 | Temperature: 22°C | Time: 10:45 AM"
        self.assertEqual(self.display.message, expected_message)
