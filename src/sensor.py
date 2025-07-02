class Sensor:
    """
    Represents a generic sensor placed in the car park.
    """

    def __init__(self, location, car_park_reference=None):
        """
        Initializes the sensor with a location and optional car park link.
        """
        self.location = location
        self.car_park_reference = car_park_reference

    def __str__(self):
        return f"Sensor at {self.location}"


class EntrySensor(Sensor):
    """
    A sensor that detects vehicles entering the car park.
    """

    def detect_vehicle(self, plate_number):
        self.car_park_reference.add_car(plate_number)


class ExitSensor(Sensor):
    """
    A sensor that detects vehicles exiting the car park.
    """

    def detect_vehicle(self, plate_number):
        self.car_park_reference.remove_car(plate_number)


class ExitSensor(Sensor):
    """
    Specialized sensor class for detecting vehicles exiting the car park.
    """
    pass

