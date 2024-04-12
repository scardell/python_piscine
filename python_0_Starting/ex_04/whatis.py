
import sys

def check_odd_or_even(number):
    if number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."

try:
    if len(sys.argv) < 2:
        sys.exit()
    number = int(sys.argv[1])
except ValueError:
    print("Argument is not an integer")
else:
    if len(sys.argv) > 2:
        print("more than one argument is provided")
    else:
        result = check_odd_or_even(number)
        print(result)
