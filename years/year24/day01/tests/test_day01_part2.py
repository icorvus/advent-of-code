from years.year24.day01.part2 import get_sum_of_similarities


def test_day01_part1():
    input_values = ("3   4", "4   3", "2   5", "1   3", "3   9", "3   3")

    assert get_sum_of_similarities(input_values) == 31
