class Display:
    """
    Represents a display screen that shows dynamic messages about car park status.
    """

    def __init__(self, display_identifier, message_text="", is_display_on=False):
        """
        Initialize a new Display object.

        :param display_identifier: Unique ID used to identify this display.
        :param message_text: The message currently shown on the display.
        :param is_display_on: Boolean indicating whether the display is currently active.
        """
        self.display_identifier = display_identifier
        self.message_text = message_text
        self.is_display_on = is_display_on

    def update(self, data_dictionary):
        """
        Updates the display's message using values from the provided data dictionary.

        :param data_dictionary: Dictionary with display data, e.g., {'available_bays': 5}.
        :raises TypeError: If the input is not a dictionary.
        """
        if not isinstance(data_dictionary, dict):
            raise TypeError("Data provided to Display.update must be a dictionary.")

        available_bays = data_dictionary.get("available_bays", "Unknown")
        self.message_text = f"Available bays: {available_bays}"

    def __str__(self):
        """
        Return a summary of the display's current message.
        """
        return f"Display {self.display_identifier}: {self.message_text}"
