from src.simulator import Simulator


class TestSimulator:
    def setup_method(self):
        self.simulator = Simulator()

    def test_simulator_sequence(self):
        self.simulator.execute("PLACE 1,2,EAST")
        self.simulator.execute("MOVE")
        self.simulator.execute("MOVE")
        self.simulator.execute("LEFT")
        self.simulator.execute("MOVE")
        assert self.simulator.robot.report() == "3,3,NORTH"
