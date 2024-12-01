import re
import math
from pathlib import Path

from years.common.data_parser import read_lines_from_file


def sum_of_possible_game_ids(lines):
    quantity_of_color_regex = r"(\d+ (?:blue|red|green))"
    sum_of_power = 0
    for line in lines:
        max_number_of_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        quantities_of_colors = re.findall(quantity_of_color_regex, line)
        for quantity, color in map(str.split, quantities_of_colors):
            if int(quantity) > max_number_of_cubes[color]:
                max_number_of_cubes[color] = int(quantity)
        sum_of_power += math.prod(max_number_of_cubes.values())

    return sum_of_power


def main():
    print(
        sum_of_possible_game_ids(
            read_lines_from_file(Path(__file__).parent / "input.txt")
        )
    )


if __name__ == "__main__":
    main()
