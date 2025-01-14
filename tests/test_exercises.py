from src.exercises import *
from io import StringIO
import sys


def test_find_opposite():
    # Helper function to capture output
    def capture_output(func, *args):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            func(*args)
            return sys.stdout.getvalue().strip()
        finally:
            sys.stdout = old_stdout

    # Test cases
    output = capture_output(find_opposite, 5)
    assert output == "the opposite of number 5 is -5"

    output = capture_output(find_opposite, -10)
    assert output == "the opposite of number -10 is 10"

    output = capture_output(find_opposite, 0)
    assert output == "the opposite of number 0 is 0"


def test_find_area_perimeter():
    # Helper function to capture output
    def capture_output(func, *args):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            func(*args)
            return sys.stdout.getvalue().strip()
        finally:
            sys.stdout = old_stdout

    # Test cases
    output = capture_output(find_area_perimeter, 5, 3)
    assert output == "The area is:  15 m2\nThe perimeter is:  16 m"

    output = capture_output(find_area_perimeter, 7, 4)
    assert output == "The area is:  28 m2\nThe perimeter is:  22 m"

    output = capture_output(find_area_perimeter, 10, 0)
    assert output == "The area is:  0 m2\nThe perimeter is:  20 m"

    output = capture_output(find_area_perimeter, 0, 0)
    assert output == "The area is:  0 m2\nThe perimeter is:  0 m"


def test_mul_div():
    # Helper function to capture output
    def capture_output(func, *args):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            func(*args)
            return sys.stdout.getvalue().strip()
        finally:
            sys.stdout = old_stdout

    # Test cases
    output = capture_output(mul_div, 6, 3)
    assert output == "6 * 3 = 18\n6 / 3 = 2.0"

    output = capture_output(mul_div, 10, 2)
    assert output == "10 * 2 = 20\n10 / 2 = 5.0"

    output = capture_output(mul_div, 7, 1)
    assert output == "7 * 1 = 7\n7 / 1 = 7.0"

    output = capture_output(mul_div, 0, 5)
    assert output == "0 * 5 = 0\n0 / 5 = 0.0"


def test_dog_sheep_gees():
    # Helper function to capture output
    def capture_output(func, *args):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            func(*args)
            return sys.stdout.getvalue().strip()
        finally:
            sys.stdout = old_stdout

    # Test cases
    output = capture_output(dog_sheep_gees, 3)
    assert output == "Dog\nSheep\nSheep\nSheep\nGoose\nGoose\nGoose\nGoose\nGoose\nGoose\nDog"

    output = capture_output(dog_sheep_gees, 1)
    assert output == "Dog\nSheep\nGoose\nGoose\nDog"

    output = capture_output(dog_sheep_gees, 0)
    assert output == "Dog\nDog"

    output = capture_output(dog_sheep_gees, 5)
    assert output == "Dog\nSheep\nSheep\nSheep\nSheep\nSheep\nGoose\nGoose\nGoose\nGoose\nGoose\nGoose\nGoose\nGoose\nGoose\nGoose\nDog"


def test_print_even_numbers_in_interval():
    # Helper function to capture output
    def capture_output(func, *args):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            func(*args)
            return sys.stdout.getvalue().strip()
        finally:
            sys.stdout = old_stdout

    # Test cases
    output = capture_output(print_even_numbers_in_interval, 1, 10)
    assert output == "2\n4\n6\n8\n10"

    output = capture_output(print_even_numbers_in_interval, 0, 5)
    assert output == "0\n2\n4"

    output = capture_output(print_even_numbers_in_interval, -3, 3)
    assert output == "-2\n0\n2"

    output = capture_output(print_even_numbers_in_interval, 5, 5)
    assert output == ""

    output = capture_output(print_even_numbers_in_interval, 2, 2)
    assert output == "2"


from src.exercises import near_fifty

def test_near_fifty():
    # Test cases
    assert near_fifty(45) == True
    assert near_fifty(140) == True
    assert near_fifty(55) == True
    assert near_fifty(62) == False
    assert near_fifty(150) == True
    assert near_fifty(169) == False
    assert near_fifty(60) == True
    assert near_fifty(100) == False


def test_discount_with_card():
    assert discount_with_card(16, True) == True
    assert discount_with_card(18, True) == True
    assert discount_with_card(60, True) == True
    assert discount_with_card(25, True) == False
    assert discount_with_card(70, False) == False
    assert discount_with_card(10, False) == False
    assert discount_with_card(30, False) == False


def test_almost_nice_division():
    # Helper function to capture output
    def capture_output(func, *args):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            func(*args)
            return sys.stdout.getvalue().strip()
        finally:
            sys.stdout = old_stdout

    # Test cases
    output = capture_output(almost_nice_division, 10, 3)
    assert output == "the remainder is:  1"

    output = capture_output(almost_nice_division, 12, 4)
    assert output == "the remainder is:  0"

    output = capture_output(almost_nice_division, 15, 4)
    assert output == "the division is not nice"

    output = capture_output(almost_nice_division, 25, 6)
    assert output == "the remainder is:  1"

    output = capture_output(almost_nice_division, 32, 5)
    assert output == "the division is not nice"

    output = capture_output(almost_nice_division, 11, 10)
    assert output == "the remainder is:  1"


def test_season():
    assert season(1) == "Winter"
    assert season(2) == "Winter"
    assert season(3) == "Spring"
    assert season(5) == "Spring"
    assert season(6) == "Summer"
    assert season(8) == "Summer"
    assert season(9) == "Autumn"
    assert season(11) == "Autumn"
    assert season(12) == "Winter"
    assert season(13) == "Invalid month"
    assert season(0) == "Invalid month"


def test_final_grade():
    assert final_grade(95, 95) == "A"
    assert final_grade(90, 70) == "B"
    assert final_grade(70, 90) == "B"
    assert final_grade(80, 80) == "C"
    assert final_grade(60, 60) == "D"
    assert final_grade(85, 60) == "D"
    assert final_grade(60, 85) == "D"