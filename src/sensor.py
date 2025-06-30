class Sensor:
    """
    Represents a sensor that detects vehicles and interacts with the car park.
    """

    def __init__(self, sensor_identifier, is_active=False, car_park_reference=None):
        self.sensor_identifier = sensor_identifier  # Unique ID to identify this sensor
        self.is_active = is_active  # Sensor operational status
        self.car_park_reference = car_park_reference  # Reference to the CarPark this sensor belongs to

    def __str__(self):
        status = "Active" if self.is_active else "Inactive"
        return f"Sensor {self.sensor_identifier} ({status})"
