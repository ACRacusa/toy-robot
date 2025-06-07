from .robot import Robot
from .table import Table
from .config import TABLE_WIDTH, TABLE_HEIGHT


class Simulator:
    # Processes robot commands
    def __init__(self):
        self.robot = Robot()
        self.table = Table(TABLE_WIDTH, TABLE_HEIGHT)

    def execute(self, command_str):
        command_str = command_str.strip().upper()

        if not command_str:
            return

        if command_str.startswith("PLACE"):
            try:
                args = command_str[6:].split(",")
                x = int(args[0])
                y = int(args[1])
                facing = args[2]
                self.robot.place(x, y, facing, self.table)
            except (IndexError, ValueError):
                pass
        elif command_str == "MOVE":
            self.robot.move(self.table)
        elif command_str == "LEFT":
            self.robot.left()
        elif command_str == "RIGHT":
            self.robot.right()
        elif command_str == "REPORT":
            report = self.robot.report()
            if report:
                print(report)
