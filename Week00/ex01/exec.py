import sys

if len(sys.argv) < 2:
        print("Usage : Python program.py <string>")
else:
    text = " ".join(sys.argv[1:])
    result = text[::1].swapcase()
    print(result)