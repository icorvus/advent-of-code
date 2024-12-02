from pathlib import Path
from collections.abc import Iterable

from years.common.data_parser import read_lines_from_file


def _remove_level_and_check_again(report: Iterable[int], without_index: int | None) -> bool:
    if without_index == len(report) - 1:
        # pointer is at the end of the list, return False, all possibilities checked
        return False
    
    # Increase the pointer or set it to start if its None
    without_index = without_index + 1 if without_index is not None else 0

    return is_safe_report(report, without_index=without_index)

def is_safe_report(report: Iterable[int], without_index: int | None = None) -> bool:
    """It's' a bruteforce solution, but it works for the given input size"""

    report = list(report)
    report_copy = report.copy()
    if without_index is not None:
        report.pop(without_index)
    
    is_increasing = False
    is_decreasing = False

    
    level_before = report[0]

    for level in report[1:]:
        if level < level_before:
            is_decreasing = True
        elif level > level_before:
            is_increasing = True
        else:
            return _remove_level_and_check_again(report_copy, without_index)
        
        if is_increasing and is_decreasing:
            return _remove_level_and_check_again(report_copy, without_index)
        
        if not (3 >= abs(level - level_before) >= 1):
            return _remove_level_and_check_again(report_copy, without_index)
        
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
