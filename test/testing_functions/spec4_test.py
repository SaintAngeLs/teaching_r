import time
import sys
import signal
import math

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

def calculate_poly_function_val(a, b, c, d, e, k, g):
    result = (10 * math.pow(a, 3) +
                11 * math.pow(b, 10) +
                12 * math.pow(c, 3) +
                3 * math.pow(d, 2) +
                6 * math.pow(e, 18) +
                67 * math.pow(k, 12) +
                22 * math.pow(g, 4) +
                127 / 168 * math.pow(a, 4) +
                4 * e +
                6/7 * math.pow(g, 2) +
                math.pow(3/2 * math.pow(a, 2), -3) -
                2/5 * d +
                10 * math.pow(e, 2) -
                math.pi * k +
                (c + d + k + g) * a * a / b)

    return result





def calculate_factorial(n):
    if not isinstance(n, int) or n < 0:
        raise Exception("Invalid input. The number must be a non-negative integer.")

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

def calculate_combination(n, r):
    if not isinstance(n, int) or not isinstance(r, int) or n < 0 or r < 0 or r > n:
        raise Exception("Invalid input. Both numbers must be non-negative integers and r must be less than or equal to n.")

    numerator = calculate_factorial(n)
    denominator = calculate_factorial(r) * calculate_factorial(n - r)
    result = numerator // denominator

    return result

def analyze_apple_weights(apple_weights):
    if not isinstance(apple_weights, list):
        raise Exception("Invalid input. The apple weights must be provided as a list.")

    if len(apple_weights) == 0:
        raise Exception("Invalid input. The list of apple weights is empty.")

    average_weight = sum(apple_weights) / len(apple_weights)
    max_weight = max(apple_weights)
    min_weight = min(apple_weights)

    analysis_results = {
        "average_weight": average_weight,
        "max_weight": max_weight,
        "min_weight": min_weight
    }

    return analysis_results

def get_course_name(number):
    course_list = construct_course_list()
    if 1 <= number <= len(course_list):
        return course_list[number - 1]
    else:
        return "Number out of range."


def test_calculate_poly_function_val():
    # Test case 1
    a = 1.5
    b = 2.3
    c = -0.7
    d = 4.2
    e = 0.8
    k = -1.1
    g = 3.6
    expected_result = (10 * math.pow(a, 3) +
                       11 * math.pow(b, 10) +
                       12 * math.pow(c, 3) +
                       3 * math.pow(d, 2) +
                       6 * math.pow(e, 18) +
                       67 * math.pow(k, 12) +
                       22 * math.pow(g, 4) +
                       127 / 168 * math.pow(a, 4) +
                       4 * e +
                       6/7 * math.pow(g, 2) +
                       math.pow(3/2 * math.pow(a, 2), -3) -
                       2/5 * d +
                       10 * math.pow(e, 2) -
                       math.pi * k +
                       (c + d + k + g) * a * a / b)
    result = calculate_poly_function_val(a, b, c, d, e, k, g)
    print(f"Result: {result} Expected Rersult: {expected_result}")
    assert result == expected_result, "Test case 1 failed"

    # Test case 2 (additional test case)
    a = 2.0
    b = 1.0
    c = 3.0
    d = 4.0
    e = 5.0
    k = 6.0
    g = 7.0
    expected_result = (10 * math.pow(a, 3) +
                       11 * math.pow(b, 10) +
                       12 * math.pow(c, 3) +
                       3 * math.pow(d, 2) +
                       6 * math.pow(e, 18) +
                       67 * math.pow(k, 12) +
                       22 * math.pow(g, 4) +
                       127 / 168 * math.pow(a, 4) +
                       4 * e +
                       6/7 * math.pow(g, 2) +
                       math.pow(3/2 * math.pow(a, 2), -3) -
                       2/5 * d +
                       10 * math.pow(e, 2) -
                       math.pi * k +
                       (c + d + k + g) * a * a / b)
    result = calculate_poly_function_val(a, b, c, d, e, k, g)

    print(f"Result: {result} Expected Rersult: {expected_result}")
    assert result == expected_result, "Test case 2 failed"

    print("All test cases for calculate_poly_function_val passed")

def test_calculate_factorial():
    # Test case 1
    n = 5
    expected_result = 5 * 4 * 3 * 2 * 1
    result = calculate_factorial(n)
    assert result == expected_result, "Test case 1 failed"

    # Test case 2 (additional test case)
    n = 0
    expected_result = 1
    result = calculate_factorial(n)
    assert result == expected_result, "Test case 2 failed"

    print("All test cases for calculate_factorial passed")

def test_calculate_combination():
    # Test case 1
    n = 5
    r = 2
    expected_result = 10
    result = calculate_combination(n, r)
    assert result == expected_result, "Test case 1 failed"

    # Test case 2 (additional test case)
    n = 10
    r = 5
    expected_result = 252
    result = calculate_combination(n, r)
    assert result == expected_result, "Test case 2 failed"

    print("All test cases for calculate_combination passed")

def test_analyze_apple_weights():
    # Test case 1
    apple_weights = [0.2, 0.5, 0.3, 0.6, 0.4]
    expected_result = {
        "average_weight": 0.4,
        "max_weight": 0.6,
        "min_weight": 0.2
    }
    result = analyze_apple_weights(apple_weights)
    assert result == expected_result, "Test case 1 failed"

    # Test case 2 (additional test case)
    apple_weights = [0.1, 0.8, 0.6, 0.4, 0.9, 0.3]
    expected_result = {
        "average_weight": 0.5166666666666666,
        "max_weight": 0.9,
        "min_weight": 0.1
    }
    result = analyze_apple_weights(apple_weights)
    assert result == expected_result, "Test case 2 failed"

    print("All test cases for analyze_apple_weights passed")

def test_get_course_name():
    # Test case 1
    number = 1
    expected_result = "Course 1 - Civil and Environmental Engineering"
    result = get_course_name(number)
    assert result == expected_result, "Test case 1 failed"

    # Test case 2 (additional test case)
    number = 10
    expected_result = "Course 10 - Chemical Engineering"
    result = get_course_name(number)
    assert result == expected_result, "Test case 2 failed"

    print("All test cases for get_course_name passed")

def run_tests():
    blue_string = "\n==========================================\n"
    test_functions = [
        ("calculate_poly_function_val", test_calculate_poly_function_val),
        ("calculate_factorial", test_calculate_factorial),
        ("calculate_combination", test_calculate_combination),
        ("analyze_apple_weights", test_analyze_apple_weights),
        ("get_course_name", test_get_course_name)
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
                signal.alarm(1000)
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
                points -= 10
                print("Basic runtime error")
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
