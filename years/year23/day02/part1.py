import re
from pathlib import Path

from years.common.data_parser import read_lines_from_file

MAX_NUMBER_OF_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def sum_of_possible_game_ids(lines):
    game_id_regex = r"Game (?P<id>\d+):"
    quantity_of_color_regex = r"(\d+ (?:blue|red|green))"
    sum_of_ids = 0
    for line in lines:
        is_game_possible = True
        quantities_of_colors = re.findall(quantity_of_color_regex, line)
        for quantity, color in map(str.split, quantities_of_colors):
            if int(quantity) > MAX_NUMBER_OF_CUBES[color]:
                is_game_possible = False
                break
        if is_game_possible:
            match_ = re.match(game_id_regex, line)
            sum_of_ids += int(match_.group("id"))

    return sum_of_ids


def main():
    print(
        sum_of_possible_game_ids(
            read_lines_from_file(Path(__file__).parent / "input.txt")
        )
    )


if __name__ == "__main__":
    main()
