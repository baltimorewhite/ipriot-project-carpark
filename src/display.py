class Display:
    """
    Represents a display screen that shows messages and status information to users entering or exiting the car park.
    """

    def __init__(self, display_identifier, message_text="", is_display_on=False):
        self.display_identifier = display_identifier  # Unique ID used to identify this display unit
        self.message_text = message_text              # Current message shown on the display
        self.is_display_on = is_display_on            # Boolean indicating whether the display is powered on

    def __str__(self):
        """
        Returns a summary of the display's current state.
        """
        return f"Display {self.display_identifier}: {self.message_text}"

