import time
import sys
import signal
from tqdm import tqdm

def timeout_handler(signum, frame):
    raise TimeoutError()

def construct_course_list():
    course_list = [
        "Course 1 - Civil and Environmental Engineering",
        "Course 2 - Mechanical Engineering",
        "Course 3 - Materials Science and Engineering",
        "Course 4 - Architecture",
        "Course 5 - Chemistry",
        "Course 6 - Electrical Engineering and Computer Science",
        "Course 7 - Biology",
        "Course 8 - Physics",
        "Course 9 - Brain and Cognitive Sciences",
        "Course 10 - Chemical Engineering"
    ]
    
    return course_list


def get_course_name(number):
    course_list = construct_course_list()
    if 1 <= number <= 10:
        return course_list[number - 1]
    else:
        return "Number out of range."

def get_month(day):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    if 1 <= day <= 365:
        cumulative_days = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        for month, cumulative_day in enumerate(cumulative_days, start=0):
            if day <= cumulative_day:
                return months[month]
        return months[12]  # December (day 365)
    else:
        return "Invalid day."




def perform_operation(a, b, c=0, d=0, e=0, f=0, g=0, h=0, i=0, operator='+'):
    numbers = [a, b, c, d, e, f, g, h, i]

    if operator == '+':
        return sum(numbers)
    elif operator == '-':
        return a - b
    elif operator == '*':
        result = 1
        for num in numbers:
            result *= num
        return result
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator."

def divide_fraction(numerator, denominator):
    i = numerator
    answer = 0

    while i > 0:
        i = i - denominator
        answer = answer + 1

    if i == 0:
        return "Result: " + str(answer)
    else:
        return "Result: " + str(answer - 1) + "\nReminder: " + str(i + denominator)


def test_construct_course_list():
    course_list = construct_course_list()
    expected_list = [
        "Course 1 - Civil and Environmental Engineering",
        "Course 2 - Mechanical Engineering",
        "Course 3 - Materials Science and Engineering",
        "Course 4 - Architecture",
        "Course 5 - Chemistry",
        "Course 6 - Electrical Engineering and Computer Science",
        "Course 7 - Biology",
        "Course 8 - Physics",
        "Course 9 - Brain and Cognitive Sciences",
        "Course 10 - Chemical Engineering"
    ]
    if course_list == expected_list:
        return "construct_course_list: Passed"
    else:
        return "construct_course_list: Failed"


def test_get_course_name():
    tests = [
        (1, "Course 1 - Civil and Environmental Engineering"),
        (2, "Course 2 - Mechanical Engineering"),
        (3, "Course 3 - Materials Science and Engineering"),
        (4, "Course 4 - Architecture"),
        (5, "Course 5 - Chemistry"),
        (6, "Course 6 - Electrical Engineering and Computer Science"),
        (7, "Course 7 - Biology"),
        (8, "Course 8 - Physics"),
        (9, "Course 9 - Brain and Cognitive Sciences"),
        (10, "Course 10 - Chemical Engineering"),
        (15, "Number out of range.")
    ]

    failed_tests = []
    for number, expected_output in tests:
        output = get_course_name(number)
        if output == expected_output:
            print(f"get_course_name({number}): Passed")
        else:
            failed_tests.append(f"get_course_name({number}): Failed")

    return failed_tests


def test_get_month():
    failed_tests = []
    # Test valid input
    tests = [
        (75, "March"),
        (365, "December"),
        (150, "May"),
        (32, "February"),
        (0, "Invalid day."),
        (500, "Invalid day.")
    ]
    for day, expected_output in tests:
        output = get_month(day)

        if output == expected_output:
            print(f"get_month({day}): Passed")
        else:
            failed_tests.append(f"get_month({day}): Failed")

    return failed_tests

def test_perform_operation():
    failed_tests = []
    # Test addition
    a, b, c = 5, 3, 2
    expected_output = 10
    output = perform_operation(a, b, c, operator='+')
    if output == expected_output:
        print("perform_operation (addition): Passed")
    else:
        failed_tests.append("perform_operation (addition): Failed")

    # Test multiplication
    a, b, c = 10, 2, 3
    expected_output = 0
    output = perform_operation(a, b, c, operator='*')
    if output == expected_output:
        print("perform_operation (multiplication): Passed")
    else:
        failed_tests.append("perform_operation (multiplication): Failed")

    # Test division
    a, b = 5, 0
    expected_output = "Error: Division by zero"
    output = perform_operation(a, b, operator='/')
    if output == expected_output:
        print("perform_operation (division): Passed")
    else:
        failed_tests.append("perform_operation (division): Failed")

    return failed_tests

def test_divide_fraction():
    failed_tests = []
    # Test division without remainder
    numerator = 6
    denominator = 2
    expected_output = "Result: 3"
    output = divide_fraction(numerator, denominator)
    if output == expected_output:
        print("divide_fraction (no remainder): Passed")
    else:
        failed_tests.append("divide_fraction (no remainder): Failed")

    # Test division with remainder
    numerator = 7
    denominator = 3
    expected_output = "Result: 2\nReminder: 1"
    output = divide_fraction(numerator, denominator)
    if output == expected_output:
        print("divide_fraction (with remainder): Passed")
    else:
        failed_tests.append("divide_fraction (with remainder): Failed")

    return failed_tests

# def test_divide_fraction1():
#     # Test division without remainder
#     numerator = 6
#     denominator = 2
#     expected_output = "Result: 3"
#     output = divide_fraction(numerator, denominator)
#     if output == expected_output:
#         return "divide_fraction (no remainder): Passed"
#     else:
#         return "divide_fraction (no remainder): Failed"


# def test_divide_fraction2():
#     # Test division with remainder
#     numerator = 7
#     denominator = 3
#     expected_output = "Result: 2\nReminder: 1"
#     output = divide_fraction(numerator, denominator)
#     if output == expected_output:
#         return "divide_fraction (with remainder): Passed"
#     else:
#         return "divide_fraction (with remainder): Failed"


# def test_divide_fraction3():
#     # Test division with complex denominator
#     numerator = 7
#     denominator = 3
#     expected_output = "Result: 2\nReminder: 1"
#     output = divide_fraction(numerator, denominator)
#     if output == expected_output:
#         return "divide_fraction (with complex denominator): Passed"
#     else:
#         return "divide_fraction (with complex denominator): Failed"


# def test_specification():
#     # Specification test for construct_course_list()
#     course_list = construct_course_list()
#     expected_course_list = [
#         "Course 1 - Civil and Environmental Engineering",
#         "Course 2 - Mechanical Engineering",
#         "Course 3 - Materials Science and Engineering",
#         "Course 4 - Architecture",
#         "Course 5 - Chemistry",
#         "Course 6 - Electrical Engineering and Computer Science",
#         "Course 7 - Biology",
#         "Course 8 - Physics",
#         "Course 9 - Brain and Cognitive Sciences",
#         "Course 10 - Chemical Engineering"
#     ]
#     if course_list == expected_course_list:
#         construct_course_list_spec = "Specification 1 (construct_course_list) met: Passed"
#     else:
#         construct_course_list_spec = "Specification 1 (construct_course_list) not met: Failed"

#     # Specification test for get_course_name()
#     valid_input_number = 1
#     expected_output_valid = "Course 1 - Civil and Environmental Engineering"
#     output_valid = get_course_name(valid_input_number)
#     if output_valid == expected_output_valid:
#         get_course_name_valid_spec = "Specification 2 (get_course_name - valid input) met: Passed"
#     else:
#         get_course_name_valid_spec = "Specification 2 (get_course_name - valid input) not met: Failed"

#     invalid_input_number = 15
#     expected_output_invalid = "Number out of range."
#     output_invalid = get_course_name(invalid_input_number)
#     if output_invalid == expected_output_invalid:
#         get_course_name_invalid_spec = "Specification 2 (get_course_name - invalid input) met: Passed"
#     else:
#         get_course_name_invalid_spec = "Specification 2 (get_course_name - invalid input) not met: Failed"

#     # # Specification test for divide_fraction()
#     # numerator_no_remainder = 6
#     # denominator_no_remainder = 2
#     # expected_output_no_remainder = "Result: 3"
#     # output_no_remainder = divide_fraction(numerator_no_remainder, denominator_no_remainder)
#     # if output_no_remainder == expected_output_no_remainder:
#     #     divide_fraction_no_remainder_spec = "Specification 3 (divide_fraction - no remainder) met: Passed"
#     # else:
#     #     divide_fraction_no_remainder_spec = "Specification 3 (divide_fraction - no remainder) not met: Failed"

#     # numerator_with_remainder = 7
#     # denominator_with_remainder = 3
#     # expected_output_with_remainder = "Result: 2\nReminder: 1"
#     # output_with_remainder = divide_fraction(numerator_with_remainder, denominator_with_remainder)
#     # if output_with_remainder == expected_output_with_remainder:
#     #     divide_fraction_with_remainder_spec = "Specification 3 (divide_fraction - with remainder) met: Passed"
#     # else:
#     #     divide_fraction_with_remainder_spec = "Specification 3 (divide_fraction - with remainder) not met: Failed"

#     # Combine all specifications into a single string
#     specification_results = [
#         construct_course_list_spec,
#         get_course_name_valid_spec,
#         get_course_name_invalid_spec,
#         # divide_fraction_no_remainder_spec,
#         # divide_fraction_with_remainder_spec
#     ]

#     return "\n".join(specification_results)


# def test_basic_accuracy():
#     # Test get_course_name()
#     number = 1
#     expected_output = "Course 1 - Civil and Environmental Engineering"
#     output = get_course_name(number)
#     if output == expected_output:
#         return "get_course_name: Passed"
#     else:
#         return "get_course_name: Failed"

#     # Test divide_fraction()
#     numerator = 6
#     denominator = 2
#     expected_output = "Result: 3"
#     output = divide_fraction(numerator, denominator)
#     if output == expected_output:
#         return "divide_fraction: Passed"
#     else:
#         return "divide_fraction: Failed"

#     # Test divide_fraction() with large numbers
#     numerator = 1000000000
#     denominator = 3
#     expected_output = "Result: 333333333\nReminder: 1"
#     output = divide_fraction(numerator, denominator)
#     if output == expected_output:
#         return "divide_fraction (large numbers): Passed"
#     else:
#         return "divide_fraction (large numbers): Failed"

def plus_success():
    time.sleep(0.4)
    print("+")

def specification_not_met(construct_course_list):
    print(f"\n Specification of {construct_course_list} not met :(")

def run_tests():
    blue_string = "\n==========================================\n"
    test_functions = [
        ("construct_course_list", test_construct_course_list),
        ("get_course_name", test_get_course_name),
        ("get_month", test_get_month),
        ("perform_operation", test_perform_operation),
        ("divide_fraction", test_divide_fraction)
    ]

    failed_tests = []
    points = 50
    print(blue_string)
    print("Specification testing...\n")
    for _ in range(10):
        for symbol in [". ", ".:", ":.", "::"]:
            time.sleep(0.1)
            print(f"\r{symbol} Running tests... ", end="")
            sys.stdout.flush()
            time.sleep(0.1)  # Add a delay of 0.1 seconds

    time.sleep(0.5)
    for test_name, test_function in test_functions:
        if test_name in globals() and callable(test_function):
            try:
                # Set the timeout to 5 seconds
                signal.signal(signal.SIGALRM, timeout_handler)
                signal.alarm(5)
                result = test_function()
                signal.alarm(0)  # Reset the alarm
                if isinstance(result, str) and result.endswith(": Failed"):
                    failed_tests.append(result)
            except TimeoutError:
                print(f"\nTimeout occurred while running {test_name}")
                failed_tests.append(f"{test_name}: Failed (Timeout)")
                points -= 10
            except Exception:
                print(f"{test_name} took too long to execute.")
                failed_tests.append(f"{test_name}: Failed")
                points -= 50
                print("Basic runtime error")
            # except Exception:
            #     print(blue_string)
            #     print(f"An error occurred while running {test_name}")
            #     failed_tests.append(f"{test_name}: Failed")
            #     points -= 10
            #     print("Basic runtime error")
        else:
            print(f"Specification not met: {test_name}")
            failed_tests.append(f"Specification not met: {test_name}")
            points -= 10
            print("Basic runtime error")
        time.sleep(0.5)

    print("\n")
    if len(failed_tests) == 0:
        print("All tests passed. \n")
    else:
        points -= len(failed_tests)*10
        print("Failed tests:")
        for test in failed_tests:
            print(test)

    if points < 0:
        points = 0  # Minimum points is 0
    print(blue_string)
    print("\nGrading: ", end="")
    sys.stdout.flush()
    to_wait(20, 0.2)
    
    total_tests = len(test_functions)
    total_failed_tests = len(failed_tests)
    points_pers = ((total_tests - total_failed_tests) / total_tests) * 50
    points_pers_n = ((total_tests - total_failed_tests) / total_tests) * 45
    test_percentage = ((total_tests - total_failed_tests) / total_tests) * 115
    print(f"\nAccuracy approximation: {test_percentage:.2f}% ")
    print("\n         ", end="")
    sys.stdout.flush()
    to_wait(10, 0.2)
    print("\n")
    print(f"Final grade: {points_pers_n:.2f} points (or {points_pers:.2f} if provided code is nice)\n")

def to_wait(a, c):
    for _ in range(a):
        time.sleep(c)
        print(".", end="")
        sys.stdout.flush()

def main():
    print("Starting program...")
    run_tests()
    print("Program completed.")


if __name__ == "__main__":
    main()
