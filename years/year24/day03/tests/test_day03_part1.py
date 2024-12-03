from years.year24.day03.part1 import get_multiplication_result


def test_day01_part1():
    input_value = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    assert get_multiplication_result(input_value) == 161
