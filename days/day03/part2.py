from dataclasses import dataclass, field
from pathlib import Path
import itertools


from days.common.data_parser import read_lines_from_file


def get_gear_pos(
    coordinates: tuple[int, int], schematic: list[str]
) -> tuple[int, int] | None:
    """
    Gets coordinates of gear adjacent to given number
    """
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
        if point == "*":
            return x + x_, y + y_


@dataclass
class HeatMapPoint:
    counter: int = 0
    numbers: list[int] = field(default_factory=list)


def get_gear_heatmap(schematic):
    width, height = len(schematic[0]), len(schematic)
    heatmap = [[HeatMapPoint() for _ in range(width)] for _ in range(height)]
    temp_number = []
    temp_number_is_part = False
    last_point = None

    for y, line in enumerate(schematic):
        for x, char in enumerate(line):
            if char.isdigit():
                temp_number.append(char)
                point = get_gear_pos((x, y), schematic)
                if point:
                    temp_number_is_part = True
                    last_point = point
            else:
                if temp_number and temp_number_is_part and last_point:
                    gear = heatmap[last_point[1]][last_point[0]]
                    gear.counter += 1
                    gear.numbers.append(int("".join(temp_number)))

                temp_number = []
                temp_number_is_part = False
    return heatmap


def sum_of_gear_ratios(schematic):
    # It may not look pretty, but I personally like some functional programming.
    return sum(
        map(
            lambda x: x.numbers[0] * x.numbers[1],
            filter(
                lambda x: x.counter == 2,
                itertools.chain.from_iterable(get_gear_heatmap(schematic)),
            ),
        )
    )


def main():
    input_values = list(read_lines_from_file(Path(__file__).parent / "input.txt"))
    print(sum_of_gear_ratios(input_values))


if __name__ == "__main__":
    main()
