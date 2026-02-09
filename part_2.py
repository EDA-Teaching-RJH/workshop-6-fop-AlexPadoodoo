#Task 2.1: System Status
rover_status = {
    "Battery": 100,
    "Heater": "Off",
    "Camera": "Standby"
}

print(f"Battery Charge: {rover_status["Battery"]}","%")


#Task 2.2: System Update
#Car has now turned on
rover_status.update({"Battery": 85})
rover_status.update({"Heater": "On"})
rover_status.update({"Speed": 5})

print(rover_status)