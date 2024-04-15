
import sys
from ft_filter import ft_filter

def main():
    try:
        if len(sys.arg) != 3:
            raise AssertionError("the argument are bad")
        
        text = sys.arg[1]
        n = int(sys.arg[2])

        if not isinstance(text, str) or not isinstance(n, int):
            raise AssertionError("the argument are bad")
        
        filtered_words = list(ft_filter(lambda word: len(word) >n, text.split()))

        print(filtered_words)

    except ValueError as error:
        print("ValueError:", error)
    except AssertionError as error:
        print("AssertionError:", error)

if __name__ == "main":
    main()