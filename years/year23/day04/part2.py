from pathlib import Path

from years.common.data_parser import read_lines_from_file


def get_total_cards_won(cards):
    cards_values = {idx: 1 for idx in range(1, len(cards) + 1)}
    for i, card in enumerate(cards, start=1):
        winning, our = map(str.split, card.split(":")[1].split("|"))
        number_of_common_numbers = len(set(winning) & set(our))
        for _ in range(cards_values[i]):
            for y in range(i + 1, i + number_of_common_numbers + 1):
                cards_values[y] += 1

    return sum(cards_values.values())


def main():
    input_values = list(read_lines_from_file(Path(__file__).parent / "input.txt"))
    print(get_total_cards_won(input_values))


if __name__ == "__main__":
    main()
