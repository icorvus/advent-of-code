from pathlib import Path

from days.common.data_parser import read_lines_from_file


def get_total_points_won(cards):
    result = 0
    for card in cards:
        winning, our = map(str.split, card.split(":")[1].split("|"))
        number_of_common_numbers = len(set(winning) & set(our))
        result += (
            2 ** (number_of_common_numbers - 1) if number_of_common_numbers > 0 else 0
        )
    return result


def main():
    input_values = read_lines_from_file(Path(__file__).parent / "input.txt")
    print(get_total_points_won(input_values))


if __name__ == "__main__":
    main()
