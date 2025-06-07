from src.robot import Robot
from src.table import Table


class TestRobot:
    def setup_method(self):
        self.robot = Robot()
        self.table = Table()

    def test_valid_place_and_report(self):
        self.robot.place(0, 0, "NORTH", self.table)
        assert self.robot.report() == "0,0,NORTH"

    def test_ignore_invalid_place(self):
        self.robot.place(5, 5, "WEST", self.table)
        assert self.robot.report() is None

    def test_ignore_invalid_direction(self):
        self.robot.place(0, 0, "UP", self.table)
        assert self.robot.report() is None

    def test_move_north(self):
        self.robot.place(0, 0, "NORTH", self.table)
        self.robot.move(self.table)
        assert self.robot.report() == "0,1,NORTH"

    def test_turn_left(self):
        self.robot.place(0, 0, "NORTH", self.table)
        self.robot.left()
        assert self.robot.report() == "0,0,WEST"

    def test_turn_right(self):
        self.robot.place(0, 0, "NORTH", self.table)
        self.robot.right()
        assert self.robot.report() == "0,0,EAST"

    def test_multiple_rotations(self):
        self.robot.place(0, 0, "NORTH", self.table)
        self.robot.right()
        self.robot.right()
        assert self.robot.report() == "0,0,SOUTH"

    def test_move_off_table_ignored(self):
        self.robot.place(0, 4, "NORTH", self.table)
        self.robot.move(self.table)
        assert self.robot.report() == "0,4,NORTH"
