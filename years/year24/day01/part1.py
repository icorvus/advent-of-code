from pathlib import Path
from collections.abc import Iterable

from years.common.data_parser import read_lines_from_file


def get_sum_of_differences(lines: Iterable[str]) -> int:
    first_list = []
    second_list = []

    for line in lines:
        first_number, second_number = line.split()
        first_list.append(int(first_number))
        second_list.append(int(second_number))

    return sum(
        map(lambda x: abs(x[0] - x[1]), zip(sorted(first_list), sorted(second_list)))
    )


def main():
    input_file = read_lines_from_file(Path(__file__).parent / "input.txt")
    print(get_sum_of_differences(input_file))


if __name__ == "__main__":
    main()
