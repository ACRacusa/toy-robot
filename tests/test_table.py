from src.table import Table


class TestTable:
    def setup_method(self):
        self.table = Table()

    def test_valid_positions(self):
        assert self.table.is_valid_position(0, 0)
        assert self.table.is_valid_position(4, 4)
        assert not self.table.is_valid_position(5, 5)
        assert not self.table.is_valid_position(-1, 0)
