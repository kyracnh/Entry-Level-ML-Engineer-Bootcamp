import sys

if len(sys.argv) < 2:
    print("Usage : Python3 Program.py <Number>")
elif len(sys.argv) > 2:
    print("Error")
else:
    num = int(sys.argv[1])
    if num == 0:
        print("I am ZERO")
    elif num % 2 == 0:
        print("I am EVEN")
    else:
        print("I am ODD")