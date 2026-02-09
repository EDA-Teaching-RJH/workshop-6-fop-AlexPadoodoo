#Task 2.1: System Status
rover_status = {
    "Battery": 100,
    "Heater": "Off",
    "Camera": "Standby"
}

print(f"Battery Charge: {rover_status["Battery"]}","%")


#Task 2.2: System Update
rover_status.update({"Battery": 85})
rover_status.update({"Heater": "On"})
rover_status.update({"Speed": 5}) #Car has now turned on and moving

print(rover_status)

#Task 2.3: The Science Log (Nesting)
mission_log = [
    {"Site": "Crater A", "Radiation": "Low", "Water": False}
    {"Site": "Dune B", "Radiation": "High", "Water": True}
]

#Challenge: Create a loop