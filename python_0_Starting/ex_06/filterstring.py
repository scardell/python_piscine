
import sys
from ft_filter import ft_filter

def main():
    """
Accepts only 2 arguments:
1. string
2. integer

Print a list of words that are longer than the integer.
"""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the argument are bad")
        
        text = sys.argv[1]
        n = sys.argv[2]

        if not isinstance(text, str):
            raise AssertionError("the argument are bad")
        if not n.isdigit():
            raise AssertionError("the argument are bad")
        
        n = int(n)
        
        filtered_words = list(ft_filter(lambda word: len(word) > n, text.split()))

        print(filtered_words)

    except ValueError as error:
        print("ValueError:", error)
    except AssertionError as error:
        print("AssertionError:", error)

if __name__ == "__main__":
    main()