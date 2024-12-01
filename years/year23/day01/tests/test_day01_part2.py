from years.year23.day01.part2 import sum_of_calibration_values


def test_first_day_second_part():
    input_values = (
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    )

    assert sum_of_calibration_values(input_values) == 281
