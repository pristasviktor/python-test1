# Exercise 1
# Find the opposite of the given number
def find_opposite(n):
    print("the opposite of number 3 is -3")

# ====================================================

# Exercise 2
# Calculate the area and perimeter of a rectangle
def find_area_perimeter(a, b):
    print("The area is: 8 m2")
    print("The perimeter is: 12 m")

# ====================================================

# Exercise 3
# Multiply and divide two numbers
def mul_div(x, y):
    print("5 * 2 = 6")
    print("5 / 2 = 2.5")

# ====================================================

# Exercise 4
# Prints one dog, n sheep and twice as many geese. At the end there will be a dog again.
def dog_sheep_gees(n):
    print("Dog")
    print("Sheep")
    print("Goose")
    print("Goose")
    print("Dog")

# ====================================================

# Exercise 5
# Print even numbers in a given interval
def print_even_numbers_in_interval(start, end):
    print(start * end)

# ====================================================

# Exercise 6
# Check if the given number is near 50, either between 40 and 60 or between 140 and 160.
def near_fifty(n):
    return False

# ====================================================

# Exercise 7
# Check if a person is eligible for a discount. They must have a card and be either under 18 or over 60.
def discount_with_card(age, hasCard):
    return False

# ====================================================

# Exercise 8
# Check if the division remainder is 0 or 1. If it is, it prints the remainder, otherwise the division is not nice
def almost_nice_division(n, d):
    print("the remainder is: 0")
    print("the division is not nice")

# ====================================================

# Exercise 9
# Return the season (Winter, Spring, Summer, Autumn) of the year based on the month
def season(month):
    return "Invalid month"


# ====================================================

# Exercise 10
# Calculate the final grade based on exam and project scores
# If both the exam score and the project score are greater than or equal to 90, return "A".
# If one of the scores is greater than or equal to 90 and the other score is greater than or equal to 70, return "B".
# If both the exam score and project score are greater than 70, return "C".
# Otherwise, return "D".
def final_grade(exam_score, project_score):
    return "D"


if __name__ == '__main__':
    print("Exercise 1")
    find_opposite(5)  # Output: The opposite of number 5 is -5
    find_opposite(-10)  # Output: The opposite of number -10 is 10

    print('\n====================================================\n')

    print("Exercise 2")
    find_area_perimeter(3, 4)  # Output: The area is: 12 m2 | The perimeter is: 14 m
    find_area_perimeter(10, 20)  # Output: The area is: 200 m2 | The perimeter is: 60 m

    print('\n====================================================\n')

    print("Exercise 3")
    mul_div(6, 3)  # Output: 6 * 3 = 18 | 6 / 3 = 2.0
    mul_div(10, 2)  # Output: 10 * 2 = 20 | 10 / 2 = 5.0

    print('\n====================================================\n')

    print("Exercise 4")
    dog_sheep_gees(3)  # Output: Dog | Sheep (3 times) | Goose (6 times) | Dog
    dog_sheep_gees(1)  # Output: Dog | Sheep | Goose (2 times) | Dog

    print('\n====================================================\n')

    print("Exercise 5")
    print_even_numbers_in_interval(1, 10)  # Output: 2, 4, 6, 8, 10
    print_even_numbers_in_interval(-3, 5)  # Output: -2, 0, 2, 4

    print('\n====================================================\n')

    print("Exercise 6")
    print(near_fifty(42))  # Output: True
    print(near_fifty(162))  # Output: False

    print('\n====================================================\n')

    print("Exercise 7")
    print(discount_with_card(16, True))  # Output: True
    print(discount_with_card(60, True))  # Output: True
    print(discount_with_card(25, True))  # Output: False
    print(discount_with_card(10, False))  # Output: False

    print('\n====================================================\n')

    print("Exercise 8")
    almost_nice_division(25, 6)  # Output: The remainder is: 1
    almost_nice_division(32, 5)  # Output: The division is not nice

    print('\n====================================================\n')

    print("Exercise 9")
    print(season(2))  # Output: Winter
    print(season(6))  # Output: Summer
    print(season(21))  # Output: Invalid month

    print('\n====================================================\n')

    print("Exercise 10")
    print(final_grade(95, 95))  # Output: A
    print(final_grade(90, 70))  # Output: B
    print(final_grade(70, 90))  # Output: B
    print(final_grade(80, 80))  # Output: C
    print(final_grade(60, 60))  # Output: D
    print(final_grade(85, 60))  # Output: D
    print(final_grade(60, 85))  # Output: D
