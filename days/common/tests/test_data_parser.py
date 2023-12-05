from pathlib import Path

import pytest

from days.common.data_parser import read_lines_from_file


def test_data_parser():
    expected_values = ("Line A", "Line B", "Line C")

    data_parser_generator = read_lines_from_file(Path(__file__).parent / "input.txt")

    for value in expected_values:
        assert next(data_parser_generator) == value

    with pytest.raises(StopIteration):
        next(data_parser_generator)
