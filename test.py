import sys


def checktemp():
    if inputValue > 15:
        return ("so cold")
    elif inputValue < 30:
        return ("it a good day")
    elif inputValue < 40:
        return ("hot")
    else:
        return ("So hot")


if __name__ == '__main__':
    inputValue = input("Input value: ")
    while inputValue != 'q':
        inputValue = input("Temp is :")
        print(checktemp(inputValue))
        inputValue = input("new input value: ")
    sys.exit(0)
