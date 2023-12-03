from pathlib import Path


def read_lines_from_file(file_name="input.txt"):
    """Yields lines from file without trailing whitespace characters."""
    data_file = Path(__file__).parent / file_name
    with data_file.open() as f:
        for line in f:
            yield line.rstrip()
