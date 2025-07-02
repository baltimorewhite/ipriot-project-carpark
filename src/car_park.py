from pathlib import Path
from display import Display
from sensor import Sensor


class CarPark:
    """
    Represents a car park with a specific location, capacity,
    and associated components like displays and sensors.
    """

    def __init__(
        self,
        location,
        capacity,
        registered_plate_numbers=None,
        registered_displays=None,
        log_file=Path("log.txt")
    ):
        """
        Initializes a new instance of the CarPark class.

        :param location: The physical or named location of the car park.
        :param capacity: The maximum number of vehicles the car park can hold.
        :param registered_plate_numbers: Optional list of license plates currently in the car park.
        :param registered_displays: Optional list of Display instances registered with the car park.
        """
        self.location = location
        self.capacity = capacity
        self.registered_plate_numbers = registered_plate_numbers or []
        self.registered_displays = registered_displays or []
        self.log_file = log_file

    def __str__(self):
        """
        Returns a summary of the car park.
        """
        return f"Car park located at {self.location}, with a total capacity of {self.capacity} bays."

    def register(self, component):
        """
        Adds a Display or Sensor component to the car park system.

        :param component: An instance of either Display or Sensor to associate with this CarPark.
        :raises TypeError: If the provided object is not a Display or Sensor.
        """
        if not isinstance(component, (Display, Sensor)):
            raise TypeError("Component must be an instance of Display or Sensor")

        if isinstance(component, Display):
            self.registered_displays.append(component)
        else:
            component.car_park_reference = self

    @property
    def available_bays(self):
        """
        Calculates the number of available bays in the car park.
        Ensures it never returns a negative value.
        """
        return max(self.capacity - len(self.registered_plate_numbers), 0)

    def add_car(self, plate_number):
        """
        Registers a vehicle entry by storing its license plate and updating all displays.

        :param plate_number: The license plate number of the entering vehicle.
        """
        self.registered_plate_numbers.append(plate_number)
        self.update_displays()

    def remove_car(self, plate_number):
        """
        Registers a vehicle exit by removing its plate from the system and updating all displays.

        :param plate_number: The license plate number of the exiting vehicle.
        :raises ValueError: If the plate is not found in the car park.
        """
        if plate_number not in self.registered_plate_numbers:
            raise ValueError(f"Plate number {plate_number} not found in the car park.")
        self.registered_plate_numbers.remove(plate_number)
        self.update_displays()

    def update_displays(self):
        """
        Sends current car park status to all connected displays.
        """
        display_data = {
            "available_bays": self.available_bays
        }
        for display in self.registered_displays:
            display.update(display_data)
