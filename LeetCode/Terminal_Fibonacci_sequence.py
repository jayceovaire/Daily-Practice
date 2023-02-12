# fibonacci

def main():
    """Runs get_number function and checks to
       make sure number is not negative"""
    number = get_number()
    if number > 1:
        fibonacci(number)
    else:
        print("enter a positive number larger than 1")
        main()


def get_number():
    """Asks for input and transmutes it to an int"""
    while True:
        try:
            text = input("Enter the sequence number you want to see: ")
            number = int(text)
            return number

        except ValueError:
            print("Error: Enter a number")


def fibonacci(number):
    """every new number is the sum of the previous two numbers
    appends new number to list then prints sequence up
    to the amount the user input"""
    fib = [0, 1]
    n1 = 0
    n2 = 1

    for i in range(number - 2):
        nth = n1 + n2
        fib.append(nth)
        n1 = n2
        n2 = nth
    print(fib)


main()
