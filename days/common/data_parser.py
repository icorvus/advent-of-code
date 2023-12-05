def read_lines_from_file(path):
    """Yields lines from file without trailing whitespace characters."""
    with path.open() as f:
        for line in f:
            yield line.rstrip()
