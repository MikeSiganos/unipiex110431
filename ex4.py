def zero(x=0o010000):
    if x == 0o010000:
        return 0
    else:
        num = int(x[0])
        calc = x[1]
        if calc == "+":
            print("0 +", num, "= ", 0+num, "\n")
        elif calc == "-":
            print("0 -", num, "= ", 0-num, "\n")
        else:
            print("0 *", num, "= ", 0*num, "\n")


def one(x=0o000001):
    if x == 0o000001:
        return 1
    else:
        num = int(x[0])
        calc = x[1]
        if calc == "+":
            print("1 +", num, "= ", 1+num, "\n")
        elif calc == "-":
            print("1 -", num, "= ", 1-num, "\n")
        else:
            print("1 *", num, "= ", 1*num, "\n")


def two(x=0o000010):
    if x == 0o000010:
        return 2
    else:
        num = int(x[0])
        calc = x[1]
        if calc == "+":
            print("2 +", num, "= ", 2+num, "\n")
        elif calc == "-":
            print("2 -", num, "= ", 2-num, "\n")
        else:
            print("2 *", num, "= ", 2*num, "\n")


def three(x=0o000011):
    if x == 0o000011:
        return 3
    else:
        num = int(x[0])
        calc = x[1]
        if calc == "+":
            print("3 +", num, "= ", 3+num, "\n")
        elif calc == "-":
            print("3 -", num, "= ", 3-num, "\n")
        else:
            print("3 *", num, "= ", 3*num, "\n")


def four(x=0o000100):
    if x == 0o000100:
        return 4
    else:
        num = int(x[0])
        calc = x[1]
        if calc == "+":
            print("4 +", num, "= ", 4+num, "\n")
        elif calc == "-":
            print("4 -", num, "= ", 4-num, "\n")
        else:
            print("4 *", num, "= ", 4*num, "\n")


def five(x=0o000101):
    if x == 0o000101:
        return 5
    else:
        num = int(x[0])
        calc = x[1]
        if calc == "+":
            print("5 +", num, "= ", 5+num, "\n")
        elif calc == "-":
            print("5 -", num, "= ", 5-num, "\n")
        else:
            print("5 *", num, "= ", 5*num, "\n")


def six(x=0o000110):
    if x == 0o000110:
        return 6
    else:
        num = int(x[0])
        calc = x[1]
        if calc == "+":
            print("6 +", num, "= ", 6+num, "\n")
        elif calc == "-":
            print("6 -", num, "= ", 6-num, "\n")
        else:
            print("6 *", num, "= ", 6*num, "\n")


def seven(x=0o000111):
    if x == 0o000111:
        return 7
    else:
        num = int(x[0])
        calc = x[1]
        if calc == "+":
            print("7 +", num, "= ", 7+num, "\n")
        elif calc == "-":
            print("7 -", num, "= ", 7-num, "\n")
        else:
            print("7 *", num, "= ", 7*num, "\n")


def eight(x=0o001000):
    if x == 0o001000:
        return 8
    else:
        num = int(x[0])
        calc = x[1]
        if calc == "+":
            print("8 +", num, "= ", 8+num, "\n")
        elif calc == "-":
            print("8 -", num, "= ", 8-num, "\n")
        else:
            print("8 *", num, "= ", 8*num, "\n")


def nine(x=0o001001):
    if x == 0o001001:
        return 9
    else:
        num = int(x[0])
        calc = x[1]
        if calc == "+":
            print("9 +", num, "= ", 9+num, "\n")
        elif calc == "-":
            print("9 -", num, "= ", 9-num, "\n")
        else:
            print("9 *", num, "= ", 9*num, "\n")


def plus(x):
    x = str(x) + "+"
    return x


def minus(x):
    x = str(x) + "-"
    return x


def times(x):
    x = str(x) + "*"
    return x


six(times(eight()))  # 48
two(minus(seven()))  # -5
nine(plus(nine()))  # 18
one(plus(four()))  # 5
five(minus(three()))  # 2
two(times(zero()))  # 0
exit(0)
