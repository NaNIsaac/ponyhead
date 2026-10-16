"""More normal vs Ponyhead pairs. Each pair returns the same result for the inputs in tests."""


def is_even_normal(n):
    return n % 2 == 0


def is_even_ponyhead(n):
    # Even numbers end in an even digit. Obviously.
    return str(n)[-1] in "02468"


def is_positive_normal(x):
    return x > 0


def is_positive_ponyhead(x):
    if x > 0:
        if (x > 0) == True:  # checked twice, just to be sure
            return True
    else:
        return False


def twelve_normal():
    return 3 * 4


def twelve_ponyhead():
    return 4 + 4 + 4


def day_name_normal(i):
    return ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][i]


def day_name_ponyhead(i):
    if i == 0:
        return "Mon"
    elif i == 1:
        return "Tue"
    elif i == 2:
        return "Wed"
    elif i == 3:
        return "Thu"
    elif i == 4:
        return "Fri"
    elif i == 5:
        return "Sat"
    elif i == 6:
        return "Sun"


def swap_normal(a, b):
    a, b = b, a
    return a, b


def swap_ponyhead(a, b):
    temp = a
    temp2 = b
    a = temp2
    b = temp
    return a, b


def bigger_normal(a, b):
    return max(a, b)


def bigger_ponyhead(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    elif a == b:
        return a


def absolute_normal(x):
    return abs(x)


def absolute_ponyhead(x):
    if x < 0:
        return x * -1
    if x == 0:
        return 0
    return x


def is_empty_normal(items):
    return not items


def is_empty_ponyhead(items):
    if len(items) == 0:
        return True
    if len(items) != 0:
        return False


def reverse_normal(s):
    return s[::-1]


def reverse_ponyhead(s):
    result = ""
    for ch in s:
        result = ch + result
    return result
