from days.common.data_parser import read_lines_from_file


def get_first_and_last_digit_from_string(string: str) -> int:
    digits = tuple(filter(str.isdigit, string))
    return int(digits[0] + digits[-1])


def sum_of_calibration_values(lines: list) -> int:
    return sum(map(get_first_and_last_digit_from_string, lines))


def main():
    print(sum(map(get_first_and_last_digit_from_string, read_lines_from_file())))


if __name__ == "__main__":
    main()
