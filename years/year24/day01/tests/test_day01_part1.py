from years.year24.day01.part1 import get_sum_of_differences


def test_day01_part1():
    input_values = ("3   4", "4   3", "2   5", "1   3", "3   9", "3   3")

    assert get_sum_of_differences(input_values) == 11
