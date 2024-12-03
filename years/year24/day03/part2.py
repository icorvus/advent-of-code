from pathlib import Path
import re


def prepare_memory(program_memory: str) -> str:
    do_regex = r"do\(\)"
    dont_regex = r"don't\(\)"

    do_indexes = []
    dont_indexes = []

    for match in re.finditer(do_regex, program_memory):
        do_indexes.append(match.end())

    for match in re.finditer(dont_regex, program_memory):
        dont_indexes.append(match.start())

    do_indexes.append(len(program_memory))  # handle don't() as the last instruction
    ranges = zip(dont_indexes, do_indexes)

    ranges = []

    for dont_index in dont_indexes:
        for do_index in do_indexes:
            if dont_index < do_index:
                ranges.append((dont_index, do_index))
                break

    return "".join(
        character
        for index, character in enumerate(program_memory)
        if not any(index in range(start, end) for start, end in ranges)
    )


def get_multiplication_result(program_memory: str) -> int:
    program_memory = prepare_memory(program_memory)

    regex = r"mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\)"
    multiplication_instructions = re.findall(regex, program_memory)

    result = 0
    for instruction in multiplication_instructions:
        a, b = map(int, instruction)
        result += a * b

    return result


def main():
    file = Path(__file__).parent / "input.txt"
    with file.open() as f:
        file_content = f.read()
    print(get_multiplication_result(file_content))


if __name__ == "__main__":
    main()
