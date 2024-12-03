from pathlib import Path
import re


def prepare_memory(program_memory: str) -> str:
    do_regex = r"do()"
    dont_regex = r"don't()"

    do_indexes = []
    dont_indexes = []

    for match in re.finditer(do_regex, program_memory):
        do_indexes.append(match.start())

    for match in re.finditer(dont_regex, program_memory):
        dont_indexes.append(match.start())

    ranges = zip(dont_indexes, do_indexes)

    for start, end in ranges:
        program_memory = program_memory[:start] + program_memory[end:]

    return program_memory


def get_multiplication_result(program_memory: str) -> int:
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
