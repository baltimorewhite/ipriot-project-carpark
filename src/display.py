class Display:
    """
    Represents a display screen showing dynamic messages to users at the car park.
    """

    def __init__(self, display_identifier, message_text="", is_display_on=False):
        self.display_identifier = display_identifier  # Unique ID to distinguish this display
        self.message_text = message_text  # Current message being displayed
        self.is_display_on = is_display_on  # Indicates if the display is active or powered on

    def __str__(self):
        return f"Display {self.display_identifier}: {self.message_text}"
