from years.year23.day03.part2 import sum_of_gear_ratios


def test_day03_part2():
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

    assert sum_of_gear_ratios(input_values) == 467835
