DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]

LEFT_TURNS = {
    "NORTH": "WEST",
    "WEST": "SOUTH", 
    "SOUTH": "EAST",
    "EAST": "NORTH"
}

RIGHT_TURNS = {
    "NORTH": "EAST",
    "EAST": "SOUTH",
    "SOUTH": "WEST", 
    "WEST": "NORTH"
}


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

    def move(self, table):
        if not self.placed:
            return

        move_map = {
            "NORTH": (0, 1),
            "EAST": (1, 0),
            "SOUTH": (0, -1),
            "WEST": (-1, 0),
        }

        dx, dy = move_map[self.facing]
        new_x = self.x + dx
        new_y = self.y + dy

        if table.is_valid_position(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def left(self):
        if self.placed:
            self.facing = LEFT_TURNS[self.facing]

    def right(self):
        if self.placed:
            self.facing = RIGHT_TURNS[self.facing]
