from vehicle import Car, Bike, Truck
from pricing import PeakPricing, OffPeakPricing, WeekendPricing
from parking_system import ParkingSystem
from pass import ParkingPass
from datetime import datetime, timedelta


def main():
    system = ParkingSystem()

    print("Urban City Parking System")
    print("Available spaces:", system.check_availability())

    vehicle = Car("CAR101")
    pricing = PeakPricing()

    if system.vehicle_entry(vehicle):
        print("Vehicle entered successfully")

    input("Press Enter to simulate exit...")

    duration, fee = system.vehicle_exit("CAR101", pricing)
    print("Parking Duration:", round(duration, 2), "hours")
    print("Parking Fee: $", round(fee, 2))


if __name__ == "__main__":
    main()
