# Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.

n = int(input())

def fibonacci(a):
    last_fib = 1
    last_fib_1 = 1
    lst = [1,1]
    while last_fib_1 < a:
        s = last_fib_1
        last_fib_1  = last_fib + last_fib_1
        last_fib = s
        lst.append(last_fib_1)       
    print(lst)

fibonacci(n)