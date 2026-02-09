#Task 3.1: THe motor controller
print("----- Motor Speed is between 0 and 100 mph -----")

try:
    motor_speed = int(input("Enter Motor Speed: "))
    print(f"Speed Set To: {motor_speed}", "mph")
except ValueError:
    print("Error: Corrupted Signal. Maintaining Current Speed")