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


def test_move_north():
    robot = Robot()
    table = Table()
    robot.place(0, 0, "NORTH", table)
    robot.move(table)
    assert robot.report() == "0,1,NORTH"


def test_move_east():
    robot = Robot()
    table = Table()
    robot.place(0, 0, "EAST", table)
    robot.move(table)
    assert robot.report() == "1,0,EAST"


def test_move_south():
    robot = Robot()
    table = Table()
    robot.place(0, 0, "SOUTH", table)
    robot.move(table)
    assert robot.report() == "0,-1,SOUTH"


def test_move_west():
    robot = Robot()
    table = Table()
    robot.place(0, 0, "WEST", table)
    robot.move(table)
    assert robot.report() == "-1,0,WEST"


def test_move_off_table_ignored():
    robot = Robot()
    table = Table()
    robot.place(0, 4, "NORTH", table)
    robot.move(table)
    assert robot.report() == "0,4,NORTH"
