# Test accepts a number to list Tests, function, arguments, expected result
# will run assertion and let you know if it passed or failed each test

# Example test(1, add, 1, 1, result=2)
# Example test(2, add, 1, 1, result=3)
# output -> Test 1 Passed
# output -> Test 2 Failed

def test(test_num, function, *args, result):
    try:
        assert function(*args) == result
        print(function, f"Test {test_num} Passed")
    except AssertionError:
        print(function, f"Test {test_num} Failed")