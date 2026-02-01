from abc import ABC, abstractmethod


class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, duration, rate):
        pass


class PeakPricing(PricingStrategy):
    def calculate(self, duration, rate):
        return duration * (rate + 2)


class OffPeakPricing(PricingStrategy):
    def calculate(self, duration, rate):
        return duration * rate


class WeekendPricing(PricingStrategy):
    def calculate(self, duration, rate):
        return duration * (rate + 1)
