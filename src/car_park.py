import json
from pathlib import Path
from datetime import datetime  # we'll use this to timestamp entries
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
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)  # create the file if it doesn't exist

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
        self._log_car_activity(plate_number, "entered")

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
        self._log_car_activity(plate_number, "exited")

    def update_displays(self):
        """
        Sends current car park status to all connected displays.
        """
        display_data = {
            "available_bays": self.available_bays
        }
        for display in self.registered_displays:
            display.update(display_data)

    def _log_car_activity(self, plate, action):
        """
        Writes an entry to the car park log file with plate, action, and timestamp.
        """
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        """
        Creates a CarPark object from a config JSON file.
        """
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)

        return cls(
            location=config["location"],
            capacity=config["capacity"],
            log_file=config["log_file"],
            registered_plate_numbers=config.get("registered_plate_numbers", [])
        )

    def write_config(self, filename=Path("config.json")):
        """
        Saves the car park's location, capacity, log file path, and plate numbers to a config file.
        """
        config_data = {
            "location": self.location,
            "capacity": self.capacity,
            "log_file": str(self.log_file),
            "registered_plate_numbers": self.registered_plate_numbers
        }

        filename = filename if isinstance(filename, Path) else Path(filename)
        with filename.open("w") as f:
            json.dump(config_data, f, indent=4)


