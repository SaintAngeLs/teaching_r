import math
import time
import sys
import signal
import io

# Timeout handler function
def timeout_handler(signum, frame):
    raise TimeoutError()

# Task 1: Calculate Factorial
def calculate_factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Task 2: Print Fibonacci
def print_fibonacci(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

# Task 3: Check Prime
def is_prime(n):
    if not isinstance(n, int) or n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Task 4: Find Palindromes
def find_palindromes(words):
    palindromes = []
    for word in words:
        if word.lower() == word.lower()[::-1]:
            palindromes.append(word)
    return palindromes

# Task 5: Calculate Mean
def calculate_mean(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def run_tests():
    def test_calculate_factorial():
        # Test case 1
        n = 5
        expected_output = 120
        output = calculate_factorial(n)
        if output == expected_output:
            print("calculate_factorial: Passed")
        else:
            print("calculate_factorial: Failed")

    def test_print_fibonacci():
        # Test case 1
        n = 7
        expected_output = "0\n1\n1\n2\n3\n5\n8\n"
        print_output = capture_print_output(print_fibonacci, n)
        if print_output == expected_output:
            print("print_fibonacci: Passed")
        else:
            print("print_fibonacci: Failed")

    def test_is_prime():
        # Test case 1
        n = 7
        expected_output = True
        output = is_prime(n)
        if output == expected_output:
            print("is_prime: Passed")
        else:
            print("is_prime: Failed")

    def test_find_palindromes():
        # Test case 1
        words = ["level", "deed", "hello", "Madam", "world"]
        expected_output = ["level", "deed", "Madam"]
        output = find_palindromes(words)
        if output == expected_output:
            print("find_palindromes: Passed")
        else:
            print("find_palindromes: Failed")

    def test_calculate_mean():
        # Test case 1
        numbers = [1, 2, 3, 4, 5]
        expected_output = 3.0
        output = calculate_mean(numbers)
        if math.isclose(output, expected_output):
            print("calculate_mean: Passed")
        else:
            print("calculate_mean: Failed")

    def capture_print_output(func, *args):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        func(*args)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()

    test_functions = [
        ("calculate_factorial", test_calculate_factorial),
        ("print_fibonacci", test_print_fibonacci),
        ("is_prime", test_is_prime),
        ("find_palindromes", test_find_palindromes),
        ("calculate_mean", test_calculate_mean)
    ]
    blue_string = "\n==========================================\n"

    for _ in range(10):
        for symbol in [". ", ".:", ":.", "::"]:
            time.sleep(0.1)
            print(f"\r{symbol} Running tests... ", end="")
            sys.stdout.flush()
            time.sleep(0.1)  # Add a delay of 0.1 seconds

    time.sleep(0.5)
    print(blue_string)

    failed_tests = []
    points = 50
    print("\nSpecification testing...\n")
    sys.stdout.flush()
    to_wait(3, 0.4)

    for test_name, test_function in test_functions:
        if test_name in globals() and callable(test_function):
            try:
                # Set the timeout to 5 seconds
                signal.signal(signal.SIGALRM, timeout_handler)
                signal.alarm(5)
                test_function()
                signal.alarm(0)  # Reset the alarm
            except TimeoutError:
                print(f"{test_name}: Failed (Timeout)")
                failed_tests.append(f"{test_name}: Failed (Timeout)")
                points -= 10
            except Exception:
                print(f"{test_name}: Failed (Runtime Error)")
                failed_tests.append(f"{test_name}: Failed (Runtime Error)")
                points -= 10
        else:
            print(f"{test_name}: Failed (Function not found)")
            failed_tests.append(f"{test_name}: Failed (Function not found)")
            points -= 10

    print("\n")
    if len(failed_tests) == 0:
        print("All tests passed.\n")
    else:
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


if __name__ == "__main__":
    run_tests()
