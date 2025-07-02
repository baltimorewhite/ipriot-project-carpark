class Display:
    """
    Represents a display unit in the car park that shows real-time information.
    """

    def __init__(self, location):
        """
        Initializes the display with its location and a blank message.

        :param location: The physical location of the display (e.g., 'Gate A').
        """
        self.location = location
        self.message = ""

    def update(self, data_dictionary):
        """
        Updates the display message based on the data received from the CarPark.

        :param data_dictionary: A dictionary containing data like available bays, temperature, and time.
        """
        display_parts = []

        if "available_bays" in data_dictionary:
            display_parts.append(f"Available bays: {data_dictionary['available_bays']}")
        if "temperature" in data_dictionary:
            display_parts.append(f"Temperature: {data_dictionary['temperature']}°C")
        if "time" in data_dictionary:
            display_parts.append(f"Time: {data_dictionary['time']}")

        self.message = " | ".join(display_parts)

    def __str__(self):
        return f"Display at {self.location}: {self.message}"
