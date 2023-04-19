# Test accepts a number to list Tests, function, arguments, expected result
# will run assertion and let you know if it passed or failed each test

# Example test(1, add, 1, 1, result=2)
# Example test(2, add, 1, 1, result=3)
# output -> Test 1 Passed
# output -> Test 2 Failed expected 3, but got 2


def test(test_num, function, *args, result):
    if not callable(function):
        print(f"Function {function} is not callable")
        return

    try:
        actual_result = function(*args)
    except Exception as e:
        print(f"Function {function} raised an exception: {e}")
        return

    try:
        assert actual_result == result
        print(f"{function.__name__} Test {test_num} Passed")
    except AssertionError:
        print(f"{function.__name__} Test {test_num} Failed: "
              f"Expected {result}, but got {actual_result}")
