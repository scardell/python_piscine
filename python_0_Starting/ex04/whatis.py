
import sys


def check_odd_or_even(number):
    """
    Determines whether a given number is odd or even.

    Parameters:
    - number (int): The number to be checked.

    Returns:
    - str: A message indicating whether the number is odd or even.

    Raises:
    - AssertionError: If the input is not an integer
    or if more than one argument is provided.
    """
    if number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."


try:
    try:
        if len(sys.argv) < 2:
            sys.exit()
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    result = check_odd_or_even(number)
    print(result)

except AssertionError as error:
    print(AssertionError.__name__ + ":", error)
