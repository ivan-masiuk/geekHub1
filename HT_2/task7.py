# Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

n = int(input())
k = int(input())
d = input()

def calc(a,b,c):
    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '*':
        print(a * b)
    elif c == '/':
        if b == 0:
            print('на ноль ділити не можна')
        else:
            print(a / b)
    elif c == '**':
        print(a ** b)    
    else:
        print('поки таке не вмію :(')

calc(n,k,d)