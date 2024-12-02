from pathlib import Path
from collections.abc import Iterable

from years.common.data_parser import read_lines_from_file


def is_safe_report(report: Iterable[int]) -> bool:
    is_increasing = False
    is_decreasing = False

    
    level_before = next(report)

    for level in report:
        if level < level_before:
            is_decreasing = True
        elif level > level_before:
            is_increasing = True
        else:
            return False
        
        if is_increasing and is_decreasing:
            return False
        
        if not (3 >= abs(level - level_before) >= 1):
            return False
        
        level_before = level

    return True


def get_number_of_safe_reports(lines: Iterable[str]) -> int:
    safe_reports_number = 0
    for line in map(str.split, lines):
        safe_reports_number += is_safe_report(map(int, line))

    return safe_reports_number

def main():
    input_file = read_lines_from_file(Path(__file__).parent / "input.txt")
    print(get_number_of_safe_reports(input_file))


if __name__ == "__main__":
    main()
