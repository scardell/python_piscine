
import sys

def analyze_text(text):
	total_chars = len(text)
	upper_count = sum(1 for char in text if char.isupper())
	lower_count = sum(1 for char in text if char.islower())
	punctuation_marks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
	punctuation_count = sum(1 for char in text if char in punctuation_marks)
	space_count = sum(1 for char in text if char.isspace())
	digit_count = sum (1 for char in text if char.isdigit())

	print(f"The text contains {total_chars} characters:")
	print(f"{upper_count} upper letters")
	print(f"{lower_count} lower letters")
	print(f"{punctuation_count} punctuation marks")
	print(f"{space_count} spaces")
	print(f"{digit_count} digits")

def main():
	try:
		if len(sys.argv) < 2:
			try:
				s = input("What is the text to count?\n")
				s += "\n"
			except EOFError:
				pass
		elif len(sys.argv) == 2:
			s = sys.argv[1]
		elif len(sys.argv) > 2:
			raise AssertionError("Too many arguments provided")
		analyze_text(s)
	except AssertionError as error:
		print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()