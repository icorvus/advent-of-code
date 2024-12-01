from years.year23.day01.part1 import sum_of_calibration_values


def test_day01_part1():
    input_values = ("1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet")

    assert sum_of_calibration_values(input_values) == 142
