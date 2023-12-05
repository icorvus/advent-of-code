from pathlib import Path

from days.common.data_parser import read_lines_from_file


def get_first_and_last_digit_from_string(string: str) -> int:
    # I know it probably isn't the most efficient way to do it,
    # but it doesn't have to be and gets the job done.
    word_to_digit_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    minimum = {"index": len(string), "digit": None}
    maximum = {"index": -1, "digit": None, "word_length": 1}
    for word, digit in word_to_digit_map.items():
        left_index = string.find(word)
        right_index = string.rfind(word)
        if -1 < left_index < minimum["index"]:
            minimum["index"] = left_index
            minimum["digit"] = digit
        if right_index > maximum["index"]:
            maximum["index"] = right_index
            maximum["digit"] = digit
            maximum["word_length"] = len(word)

    digits_left = tuple(filter(str.isdigit, string[: minimum["index"]]))
    digits_right = tuple(
        filter(str.isdigit, string[maximum["index"] + maximum["word_length"] :])
    )
    left = digits_left[0] if digits_left else minimum["digit"]
    right = digits_right[-1] if digits_right else maximum["digit"]

    return int(left + right)


def sum_of_calibration_values(lines):
    return sum(map(get_first_and_last_digit_from_string, lines))


def main():
    print(
        sum(
            map(
                get_first_and_last_digit_from_string,
                read_lines_from_file(Path(__file__).parent / "input.txt"),
            )
        )
    )


if __name__ == "__main__":
    main()
