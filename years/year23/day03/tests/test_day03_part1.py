from years.year23.day03.part1 import sum_of_part_numbers


def test_day03_part1():
    input_values = (
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    )

    assert sum_of_part_numbers(input_values) == 4361
