#Task 3.1: THe motor controller
print("----- Motor Speed is between 0 and 100 mph -----")

try:
    motor_speed = int(input("Enter Motor Speed: "))
    print(f"Speed Set To: {motor_speed}", "mph")
except ValueError:
    print("Error: Corrupted Signal. Maintaining Current Speed")

#Task 3.2: The persistent reciever
def get_coordinate():
    while True:
        try:
            x = int(input("Enter an X coordinate: "))
            print(f"X coordinate set to: {x}")
            if x>100 or x< -100:
                print("Coordinate out of range! Please try again.")
            else:
                break    
        except ValueError:
            print("Invalid Coordinate. Try again")

get_coordinate()


#Task 3.3: Range Checks (logical errors)
#Edit 3.2 to make the speed range appropriate