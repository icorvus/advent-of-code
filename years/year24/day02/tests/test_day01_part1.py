from years.year24.day02.part1 import get_number_of_safe_reports


def test_day01_part1():
    input_values = (
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    )

    assert get_number_of_safe_reports(input_values) == 2
