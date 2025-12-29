import string
import sys

def text_analyzer(text=None):
    if text is None:
        text = input("Please provide a string to analyze :\n")
    if not isinstance(text, str):
        print("Error: arg must be a string.")
        return
    printable_c = sum(1 for c in text if c in string.printable)
    upper_c = sum(1 for c in text if c.isupper())
    lower_c = sum(1 for c in text if c.islower())
    punct_c = sum(1 for c in text if c in string.punctuation)
    space_c = sum(1 for c in text if c == " ")

    print(f"The text contains {printable_c} printable Characters:")
    print(f"- {upper_c} Uppercase letters")
    print(f"- {lower_c} LowerCase letters")
    print(f"- {punct_c} Punctuation characters")
    print(f"- {space_c} Spaces")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("More than one arg provided brooooooo")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()