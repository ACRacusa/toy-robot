from src.robot import Robot
from src.table import Table

def test_valid_place_and_report():
    robot = Robot()
    table = Table()
    robot.place(0, 0, "NORTH", table)
    assert robot.report() == "0,0,NORTH"

def test_ignore_invalid_place():
    robot = Robot()
    table = Table()
    robot.place(5, 5, "WEST", table)
    assert robot.report() is None

def test_ignore_invalid_direction():
    robot = Robot()
    table = Table()
    robot.place(0, 0, "UP", table)
    assert robot.report() is None
