from pathlib import Path

from years.common.data_parser import read_lines_from_file


def is_number_a_part(coordinates: tuple, schematic: list[str]):
    x, y = coordinates
    potential_points = [
        (1, 1),
        (1, 0),
        (1, -1),
        (0, 1),
        (0, -1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
    ]
    for x_, y_ in potential_points:
        try:
            point = schematic[y + y_][x + x_]
        except IndexError:
            continue
        if not point.isdigit() and point != ".":
            return True
    return False


def sum_of_part_numbers(schematic):
    result = 0
    temp_number = []
    temp_number_is_part = False
    for y, line in enumerate(schematic):
        for x, char in enumerate(line):
            if char.isdigit():
                temp_number.append(char)
                if is_number_a_part((x, y), schematic):
                    temp_number_is_part = True
            else:
                if temp_number and temp_number_is_part:
                    result += int("".join(temp_number))
                temp_number = []
                temp_number_is_part = False
    return result


def main():
    input_values = list(read_lines_from_file(Path(__file__).parent / "input.txt"))
    print(sum_of_part_numbers(input_values))


if __name__ == "__main__":
    main()
