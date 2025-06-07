DIRECTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']

class Robot:
    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None
        self.placed = False

    def place(self, x, y, facing, table):
        if facing not in DIRECTIONS:
            return
        if table.is_valid_position(x, y):
            self.x = x
            self.y = y
            self.facing = facing
            self.placed = True

    def report(self):
        if self.placed:
            return f"{self.x},{self.y},{self.facing}"
        return None
