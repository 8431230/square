# test_data.py

from data import square_number

def test_square_case1():
    expected_output = 4
    assert square(2) == expected_output

def test_square_case2():
    expected_output = 25
    assert square(5) == expected_output

def test_square_case3():
    expected_output = 9
    assert square(-3) == expected_output
