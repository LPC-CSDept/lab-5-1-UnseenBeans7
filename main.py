def getinput():
    # ******************************
    # Make your Code
    # ******************************
    num = int(input("Enter a number: "))
    return num

def getsum(v1, v2):
    # ******************************
    # Make your Code
    # ******************************
    sum = v1 + v2
    return sum


def printval(v1, v2, total):
    # ******************************
    # Make your Code
    # ******************************
    print(v1, v2, total)


def main():
    # ******************************
    # Make your Code
    # ******************************
    uval1 = getinput()
    uval2 = getinput()
    total = getsum(uval1, uval2)
    printval(uval1, uval2, total)


if __name__ == '__main__':
    main()
