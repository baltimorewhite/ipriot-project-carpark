from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display
from pathlib import Path

# Create a car park object with the location 'moondalup', capacity 100, and log file 'moondalup.txt'
car_park = CarPark(location="moondalup", capacity=100, log_file=Path("moondalup.txt"))

# Write the car park configuration to a file called 'moondalup_config.json'
car_park.write_config("moondalup_config.json")

# Reinitialize the car park object from the 'moondalup_config.json' file
car_park = CarPark.from_config("moondalup_config.json")

# Create an entry sensor object with location 'Gate 1' and link it to the car park
entry_sensor = EntrySensor(location="Gate 1", car_park_reference=car_park)

# Create an exit sensor object with location 'Gate 2' and link it to the car park
exit_sensor = ExitSensor(location="Gate 2", car_park_reference=car_park)

# Create a display object at 'Main Entrance'
display = Display(location="Main Entrance")

# Register all components with the car park
car_park.register(entry_sensor)
car_park.register(exit_sensor)
car_park.register(display)

# Drive 10 cars into the car park via the entry sensor
for i in range(10):
    plate = f"MOON-{i+1:03}"
    entry_sensor.detect_vehicle(plate)

# Drive 2 cars out of the car park via the exit sensor
exit_sensor.detect_vehicle("MOON-003")
exit_sensor.detect_vehicle("MOON-007")

# Output display state
print(display)
