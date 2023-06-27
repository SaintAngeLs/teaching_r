import time
import sys
import signal
import math

def timeout_handler(signum, frame):
    raise TimeoutError()
# Task 1
def perform_operation(a, b, c=0, d=0, e=0, f=0, g=0, h=0, i=0, operator='+'):
    if operator == '+':
        return a + b + c + d + e + f + g + h + i
    elif operator == '-':
        return a - b - c - d - e - f - g - h - i
    elif operator == '*':
        return a * b * c * d * e * f * g * h * i
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero"
        else:
            return a / b / c / d / e / f / g / h / i

# Task 2
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Task 3
def calculate_iterated_integral(a, b, c, d, e, g):
    result = (b - a) * (d - c) * (g - e)
    return result

# Task 4
def is_palindrome(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    return s == s[::-1]

# Task 5
def get_month(day):
    if day <= 31:
        return "January"
    elif day <= 59:
        return "February"
    elif day <= 90:
        return "March"
    elif day <= 120:
        return "April"
    elif day <= 151:
        return "May"
    elif day <= 181:
        return "June"
    elif day <= 212:
        return "July"
    elif day <= 243:
        return "August"
    elif day <= 273:
        return "September"
    elif day <= 304:
        return "October"
    elif day <= 334:
        return "November"
    else:
        return "December"


def test_perform_operation():
    # Test case 1
    a = 5
    b = 3
    c = 2
    d = 4
    expected_result = 14
    result = perform_operation(a, b, c, d, operator='+')

    assert result == expected_result, "Test case 1 failed"

    # Test case 2 (additional test case)
    a = 10
    b = 2
    c = 3
    expected_result = 0
    result = perform_operation(a, b, c, operator='*')

    assert result == expected_result, "Test case 2 failed"

    # Test case 3 (additional test case)
    a = 5
    b = 0
    expected_result = "Error: Division by zero"
    result = perform_operation(a, b, operator='/')

    assert result == expected_result, "Test case 3 failed"

    print("All test cases for perform_operation passed")

def test_fibonacci():
    # Test case 1
    n = 10
    expected_result = 55
    result = fibonacci(n)
    assert result == expected_result, "Test case 1 failed"

    # Test case 2 (additional test case)
    n = 0
    expected_result = 0
    result = fibonacci(n)
    assert result == expected_result, "Test case 2 failed"

    # Test case 3 (additional test case)
    n = 1
    expected_result = 1
    result = fibonacci(n)
    assert result == expected_result, "Test case 3 failed"

    print("All test cases for fibonacci passed")

def test_calculate_iterated_integral():
    # Test case 1
    a = 1
    b = 3
    c = 2
    d = 4
    e = 0
    g = 5
    expected_result = 20

    result = calculate_iterated_integral(a, b, c, d, e, g)
    print(result)
    assert result == expected_result, "Test case 1 failed"

    # Test case 2 (additional test case)
    a = -2
    b = 2
    c = -3
    d = 3
    e = -4
    g = 4
    expected_result = 192
    result = calculate_iterated_integral(a, b, c, d, e, g)
    print(result)
    assert result == expected_result, "Test case 2 failed"

    print("All test cases for calculate_iterated_integral passed")

def test_is_palindrome():
    # Test case 1
    s = "racecar"
    expected_result = True
    result = is_palindrome(s)
    assert result == expected_result, "Test case 1 failed"

    # Test case 2 (additional test case)
    s = "Hello, World!"
    expected_result = False
    result = is_palindrome(s)
    assert result == expected_result, "Test case 2 failed"

    print("All test cases for is_palindrome passed")

def test_get_month():
    # Test case 1
    day = 75
    expected_result = "March"
    result = get_month(day)
    assert result == expected_result, "Test case 1 failed"

    # Test case 2 (additional test case)
    day = 365
    expected_result = "December"
    result = get_month(day)
    assert result == expected_result, "Test case 2 failed"

    print("All test cases for get_month passed")

def run_tests():
    test_functions = [
        ("perform_operation", test_perform_operation),
        ("fibonacci", test_fibonacci),
        ("calculate_iterated_integral", test_calculate_iterated_integral),
        ("is_palindrome", test_is_palindrome),
        ("get_month", test_get_month)
    ]
    blue_string = "\n==========================================\n"

    failed_tests = []

    print(blue_string)
    print("Specification testing...\n")
    for _ in range(10):
        for symbol in [". ", ".:", ":.", "::"]:
            time.sleep(0.1)
            print(f"\r{symbol} Running tests... ", end="")
            sys.stdout.flush()
            time.sleep(0.1)  # Add a delay of 0.1 seconds
    points = 50
    time.sleep(0.5)
    for test_name, test_function in test_functions:
        if test_name in globals() and callable(test_function):
            try:
                # Set the timeout to 5 seconds
                signal.signal(signal.SIGALRM, timeout_handler)
                signal.alarm(1000)
                result = test_function()
                signal.alarm(0)  # Reset the alarm
                if isinstance(result, str) and result.endswith(": Failed"):
                    failed_tests.append(result)
            except TimeoutError:
                print(f"\nTimeout occurred while running {test_name}")
                failed_tests.append(f"{test_name}: Failed (Timeout)")
                points -= 10
            except AssertionError:
                failed_tests.append(test_name + ": Failed")
            
            except Exception:
                print(f"{test_name} took too long to execute.")
                failed_tests.append(f"{test_name}: Failed")
                points -= 10
                print("Basic runtime error")
        else:
            print(f"Specification not met: {test_name}")
            failed_tests.append(f"Specification not met: {test_name}")
            points -= 10
            print("Basic runtime error")

    if len(failed_tests) == 0:
        print("All tests passed")
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


run_tests()
