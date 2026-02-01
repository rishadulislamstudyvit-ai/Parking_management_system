from abc import ABC, abstractmethod
from datetime import datetime


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


class Car(Vehicle):
    def calculate_fee(self, duration, pricing_strategy):
        return pricing_strategy.calculate(duration, rate=5)


class Bike(Vehicle):
    def calculate_fee(self, duration, pricing_strategy):
        return pricing_strategy.calculate(duration, rate=2)


class Truck(Vehicle):
    def calculate_fee(self, duration, pricing_strategy):
        return pricing_strategy.calculate(duration, rate=8)
