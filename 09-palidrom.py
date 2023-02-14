def palidrom_num(num):
    n = num
    reverse = 0
    while num > 0:
        r = num % 10
        reverse = (reverse * 10) + r
        num = num//10
    
    if reverse == n:
        return True 
    else:
        return False
    """

    n = str(num)[::-1]#this is more easily
    n = int(n)

    if num == n:
        print("this number is polidrom")
    else:
        print("this number isn't polidrom")
"""
print(palidrom_num(int(input("enter a number:")))) 