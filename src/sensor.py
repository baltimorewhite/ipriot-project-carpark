class Sensor:
    """
    Base class for all sensors that interact with the car park.
    Intended to be subclassed by EntrySensor and ExitSensor.
    """

    def __init__(self, sensor_identifier, is_active=False, car_park_reference=None):
        """
        Initialize a generic sensor.

        :param sensor_identifier: Unique identifier for the sensor.
        :param is_active: Boolean flag indicating if the sensor is operational.
        :param car_park_reference: Reference to the car park this sensor is assigned to.
        """
        self.sensor_identifier = sensor_identifier
        self.is_active = is_active
        self.car_park_reference = car_park_reference

    def __str__(self):
        """
        Return a readable status of the sensor.
        """
        sensor_status = "Active" if self.is_active else "Inactive"
        return f"Sensor {self.sensor_identifier} is currently {sensor_status}."


class EntrySensor(Sensor):
    """
    Specialized sensor class for detecting vehicles entering the car park.
    """
    pass


class ExitSensor(Sensor):
    """
    Specialized sensor class for detecting vehicles exiting the car park.
    """
    pass

