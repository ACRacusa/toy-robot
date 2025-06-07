from src.table import Table

def test_valid_positions():
    table = Table()
    assert table.is_valid_position(0, 0)
    assert table.is_valid_position(4, 4)
    assert not table.is_valid_position(5, 5)
    assert not table.is_valid_position(-1, 0)
