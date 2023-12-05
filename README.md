# Advent of code

This repository contains my solutions to the [Advent of Code](https://adventofcode.com/) 2023 programming challenges.


## Installation
1. Clone the repository:
    ```
    git clone https://github.com/your-username/advent-of-code.git
    cd advent-of-code
    ```
1.
    (Optional) Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
1. Install the package:
    ```
    pip install -e .
    ```

## Usage

To run a specific day's solution, navigate to the corresponding day's directory and execute the Python scripts for `part1.py` and `part2.py`. For example:

```
cd days/day01
python part1.py
python part2.py
```

## Testing

Project includes unit tests to ensure correctness of solutions. To run the tests, use the following command:
```
pytest
```