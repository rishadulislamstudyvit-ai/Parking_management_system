from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# =========================
# Abstract Base Classes
# =========================

class Vehicle(ABC):
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.entry_time = None
        self.exit_time = None

    def enter(self):
        self.entry_time = datetime.now()

    def exit(self):
        self.exit_time = datetime.now()

    def get_duration_hours(self):
        duration = self.exit_time - self.entry_time
        return duration.total_seconds() / 3600

    @abstractmethod
    def calculate_fee(self, duration, pricing_strategy):
        pass

class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, duration, rate):
        pass

# =========================
# Pricing Strategies
# =========================

class PeakPricing(PricingStrategy):
    def calculate(self, duration, rate):
        return duration * (rate + 2)

class OffPeakPricing(PricingStrategy):
    def calculate(self, duration, rate):
        return duration * rate

class WeekendPricing(PricingStrategy):
    def calculate(self, duration, rate):
        return duration * (rate + 1)

# =========================
# Vehicle Types (Inheritance)
# =========================

class Car(Vehicle):
    def calculate_fee(self, duration, pricing_strategy):
        return pricing_strategy.calculate(duration, rate=5)

class Bike(Vehicle):
    def calculate_fee(self, duration, pricing_strategy):
        return pricing_strategy.calculate(duration, rate=2)

class Truck(Vehicle):
    def calculate_fee(self, duration, pricing_strategy):
        return pricing_strategy.calculate(duration, rate=8)

# =========================
# Parking Pass
# =========================

class ParkingPass:
    def __init__(self, pass_id, valid_until):
        self.pass_id = pass_id
        self.valid_until = valid_until

    def is_valid(self):
        return datetime.now() <= self.valid_until

# =========================
# Parking Space
# =========================

class ParkingSpace:
    def __init__(self, space_id):
        self.space_id = space_id
        self.is_occupied = False

    def occupy(self):
        self.is_occupied = True

    def free(self):
        self.is_occupied = False

# =========================
# Parking System
# =========================

class ParkingSystem:
    def __init__(self, total_spaces=300):
        self.spaces = [ParkingSpace(i + 1) for i in range(total_spaces)]
        self.parked_vehicles = {}

    def check_availability(self):
        return len([space for space in self.spaces if not space.is_occupied])

    def vehicle_entry(self, vehicle):
        for space in self.spaces:
            if not space.is_occupied:
                space.occupy()
                vehicle.enter()
                self.parked_vehicles[vehicle.vehicle_id] = (vehicle, space)
                return True
        return False

    def vehicle_exit(self, vehicle_id, pricing_strategy):
        if vehicle_id in self.parked_vehicles:
            vehicle, space = self.parked_vehicles[vehicle_id]
            vehicle.exit()
            duration = vehicle.get_duration_hours()
            fee = vehicle.calculate_fee(duration, pricing_strategy)
            space.free()
            del self.parked_vehicles[vehicle_id]
            return duration, fee
        return None, None

# =========================
# Main Program (Sample Run)
# =========================

def main():
    system = ParkingSystem()
    print("Urban City Parking Management System")
    print("Available spaces:", system.check_availability())

    vehicle = Car("CAR101")

    pricing_strategy = PeakPricing()

    if system.vehicle_entry(vehicle):
        print("Vehicle entered successfully")

    input("Press Enter to simulate vehicle exit...")

    duration, fee = system.vehicle_exit("CAR101", pricing_strategy)
    print("Parking Duration:", round(duration, 2), "hours")
    print("Parking Fee: $", round(fee, 2))

if __name__ == "__main__":
    main()
