from parking_space import ParkingSpace


class ParkingSystem:
    def __init__(self, total_spaces=300):
        self.spaces = [ParkingSpace(i + 1) for i in range(total_spaces)]
        self.parked_vehicles = {}

    def check_availability(self):
        return len([s for s in self.spaces if not s.is_occupied])

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
