import time
import sys
import signal
import io

def timeout_handler(signum, frame):
    raise TimeoutError()

# Task 1
def calculate_the_sum_of_n_numbers(n):
    return n * (n + 1) // 2

# Task 2
def nums_to_n(n):
    for i in range(1, n+1):
        if i % 2 != 0:
            if i % 5 == 0:
                print(f"{i} is divisible by 5;")
            else:
                print(f"{i};")

# Task 3
def analyse_the_number(x, a_less, b_greater):
    if x % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

    if x >= b_greater:
        print("The number is greater than or equal to", b_greater)
    else:
        print("The number is not greater than or equal to", b_greater)

    if x <= a_less:
        print("The number is less than or equal to", a_less)
    else:
        print("The number is not less than or equal to", a_less)

    factorial = 1
    for i in range(1, x+1):
        factorial *= i
    print("Factorial of", x, "is", factorial)

    print("Number:", x*b_greater, a_less)

    if -2 <= x <= 2:
        if x == 0:
            print("zero")
        elif x == 1:
            print("one")
        elif x == 2:
            print("two")
        elif x == -1:
            print("minus one")
        elif x == -2:
            print("minus two")

# Task 4
def solve_system(a1, b1, c1, a2, b2, c2):
    determinant = a1 * b2 - a2 * b1

    if determinant != 0:
        x = (c1 * b2 - c2 * b1) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        return (x, y)
    else:
        if a1/a2 == b1/b2 and a1/a2 == c1/c2:
            return "No unique solution"
        else:
            return "No solution"

# Task 5
def is_palindrome(s):
    s = s.lower().replace(" ", "").replace(",", "").replace("!", "")
    return s == s[::-1]




def run_tests():
    def test_calculate_the_sum_of_n_numbers():
        # Test case 1
        n = 100
        expected_sum = 5050
        output_sum = calculate_the_sum_of_n_numbers(n)
        if output_sum == expected_sum:
            print("calculate_the_sum_of_n_numbers: Passed")
        else:
            print("calculate_the_sum_of_n_numbers: Failed")

    def test_nums_to_n():
        # Test case 1
        n = 10
        expected_output = "1;\n3;\n5 is divisible by 5;\n7;\n9;\n"
        print_output = capture_print_output(nums_to_n, n)
        print(print_output)
        if print_output == expected_output:
            print("nums_to_n: Passed")
        else:
            print("nums_to_n: Failed")

    def test_analyse_the_number():
        # Test case 1
        x = 6
        a_less = 4
        b_greater = 8
        expected_output = "The number is even.\nThe number is greater than or equal to 8\nThe number is not less than or equal to 4\nFactorial of 6 is 720\nNumber: 48 4\n"
        print_output = capture_print_output(analyse_the_number, x, a_less, b_greater)
        if print_output == expected_output:
            print("analyse_the_number: Passed")
        else:
            print("analyse_the_number: Failed")

    def test_solve_system():
        # Test case 1
        a1, b1, c1 = 2, 3, 7
        a2, b2, c2 = 4, -2, 10
        expected_output = (2.0, 1.0)
        output = solve_system(a1, b1, c1, a2, b2, c2)
        if output == expected_output:
            print("solve_system: Passed")
        else:
            print("solve_system: Failed")

    def test_is_palindrome():
        # Test case 1
        s = "racecar"
        expected_output = True
        output = is_palindrome(s)
        if output == expected_output:
            print("is_palindrome: Passed")
        else:
            print("is_palindrome: Failed")

    def capture_print_output(func, *args):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        func(*args)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()
    
    

    test_functions = [
        ("calculate_the_sum_of_n_numbers", test_calculate_the_sum_of_n_numbers),
        ("nums_to_n", test_nums_to_n),
        ("analyse_the_number", test_analyse_the_number),
        ("solve_system", test_solve_system),
        ("is_palindrome", test_is_palindrome)
    ]
    
    blue_string = "\n==========================================\n"

    for _ in range(10):
        for symbol in [". ", ".:", ":.", "::"]:
            time.sleep(0.1)
            print(f"\r{symbol} Running tests... ", end="")
            sys.stdout.flush()
            time.sleep(0.1)  # Add a delay of 0.1 seconds

    time.sleep(0.5)

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

    print("\n")
    if len(failed_tests) == 0:
        print("All tests passed. \n")
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
    
    print("\n\nFinal grade: ", end="")
    sys.stdout.flush()
    to_wait(3, 0.2)
    print(" ", points, "points \n\n")
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
    

# Rest of the code...


if __name__ == "__main__":
    run_tests()
