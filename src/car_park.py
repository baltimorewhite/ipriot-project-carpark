from display import Display
from sensor import Sensor

class CarPark:
    """
    Represents a car park with a specific location, capacity, and associated components.
    """

    def __init__(self, location, capacity, registered_plate_numbers=None, registered_displays=None):
        self.location = location  # Physical or geographic name of the car park
        self.capacity = capacity  # Total number of parking bays
        self.registered_plate_numbers = registered_plate_numbers or []  # List of strings representing vehicle plates
        self.registered_displays = registered_displays or []  # List of Display instances

    def __str__(self):
        return f"Car park located at {self.location}, with a total capacity of {self.capacity} bays."
