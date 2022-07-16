# Section 10 of ZtM course
# Created 7/15/2022

def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(1000):
    print(x)