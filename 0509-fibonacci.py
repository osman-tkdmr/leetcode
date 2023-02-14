def fibonacci(num):
    fib = [0, 1]
    for i in range(num-2):
        fib.append(fib[i]+fib[i+1])
    return fib

fib = fibonacci(int(input("please enter your input number:")))
for i in fib:
    print(i)
