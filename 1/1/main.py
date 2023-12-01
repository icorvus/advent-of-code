from pathlib import Path


def get_first_and_last_digit_from_string(string: str) -> int:
    digits = tuple(filter(str.isdigit, string))
    return int(digits[0] + digits[-1])


def main():
    data_file_name = "input.txt"
    data_file = Path(__file__).parent / data_file_name

    with data_file.open() as f:
        lines = f.read().splitlines()

    print(sum(map(get_first_and_last_digit_from_string, lines)))


if __name__ == "__main__":
    main()
