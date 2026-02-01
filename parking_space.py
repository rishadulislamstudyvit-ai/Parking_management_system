class ParkingSpace:
    def __init__(self, space_id):
        self.space_id = space_id
        self.is_occupied = False

    def occupy(self):
        self.is_occupied = True

    def free(self):
        self.is_occupied = False
