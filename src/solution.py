# Exercise 1
# Find the opposite of the given number
def find_opposite(n):
    print("the opposite of number", n, "is", -1 * n)

# ====================================================

# Exercise 2
# Calculate the area and perimeter of a rectangle
def find_area_perimeter(a, b):
    print("The area is: ", a * b, "m2")
    print("The perimeter is: ", 2 * a + 2 * b, "m")

# ====================================================

# Exercise 3
# Multiply and divide two numbers
def mul_div(x, y):
    print(x, "*", y, "=", x * y)
    print(x, "/", y, "=", x / y)

# ====================================================

# Exercise 4
# Prints one dog, n sheep and twice as many geese. At the end there will be a dog again.
def dog_sheep_gees(n):
    print("Dog")
    for i in range(n):
        print("Sheep")
    for i in range(2 * n):
        print("Goose")
    print("Dog")

# ====================================================

# Exercise 5
# Print even numbers in a given interval
def print_even_numbers_in_interval(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)

# ====================================================

# Exercise 6
# Check if the given number is near 50, either between 40 and 60 or between 140 and 160.
def near_fifty(n):
    return 40 <= n <= 60 or 140 <= n <= 160

# ====================================================

# Exercise 7
# Check if a person is eligible for a discount. They must have a card and be either under 18 or over 60.
def discount_with_card(age, hasCard):
    return hasCard and (age <= 18 or 60 <= age)

# ====================================================

# Exercise 8
# Check if the division remainder is 0 or 1. If it is, it prints the remainder, otherwise the division is not nice
def almost_nice_division(n, d):
    if (n % d == 0) or (n % d == 1):
        print("the remainder is: ", n % d)
    else:
        print("the division is not nice")

# ====================================================

# Exercise 9
# Return the season of the year based on the month
def season(month):
    if month == 12 or month == 1 or month == 2:
        return "Winter"
    elif month == 3 or month == 4 or month == 5:
        return "Spring"
    elif month == 6 or month == 7 or month == 8:
        return "Summer"
    elif month == 9 or month == 10 or month == 11:
        return "Autumn"
    else:
        return "Invalid month"


# ====================================================

# Exercise 10
# Calculate the final grade based on exam and project scores
# If both the exam score and the project score are greater than or equal to 90, return "A".
# If one of the scores is greater than or equal to 90 and the other score is greater than or equal to 70, return "B".
# If both the exam score and project score are greater than 70, return "C".
# Otherwise, return "D".
def final_grade(exam_score, project_score):
    if exam_score >= 90 and project_score >= 90:
        return "A"
    elif (exam_score >= 90 and project_score >= 70) or (exam_score >= 70 and project_score >= 90):
        return "B"
    elif exam_score > 70 and project_score > 70:
        return "C"
    else:
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
