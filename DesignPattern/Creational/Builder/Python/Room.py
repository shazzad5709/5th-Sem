class Room:
    def __init__(self, number):
        self.number = number
        self.sides = {}

    def set_side(self, direction, side):
        self.sides[direction] = side