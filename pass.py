from datetime import datetime


class ParkingPass:
    def __init__(self, pass_id, valid_until):
        self.pass_id = pass_id
        self.valid_until = valid_until

    def is_valid(self):
        return datetime.now() <= self.valid_until
