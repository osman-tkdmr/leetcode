def addToArrayForm(num: list, k):
    return [int(e) for e in (str(int("".join(str(i) for i in num))+ k))]

