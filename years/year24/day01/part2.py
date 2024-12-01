from pathlib import Path
from collections import Counter
from collections.abc import Iterable

from years.common.data_parser import read_lines_from_file


def get_sum_of_similarities(lines: Iterable[str]):
    first_list = []
    second_list = []

    for line in lines:
        first_number, second_number = line.split()
        first_list.append(int(first_number))
        second_list.append(second_number)

    counter = Counter(second_list)

    return sum(map(lambda x: x * counter[str(x)], first_list))


def main():
    input_file = read_lines_from_file(Path(__file__).parent / "input.txt")
    print(get_sum_of_similarities(input_file))


if __name__ == "__main__":
    main()
