# Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
# -  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
# -  Повиннi опрацювати такi умови:
# -  x > y;       вiдповiдь - х бiльше нiж у на z
# -  x < y;       вiдповiдь - у бiльше нiж х на z
# -  x == y.      вiдповiдь - х дорiвнює z

x = int(input())
y = int(input())

def comparTwo (a,b):
    # if a != b:
    #     print(a - b)
    if a > b:
        z = a - b
        print(f'{a} бiльше нiж {b} на ',z)
    elif a < b:
        z = b - a
        print(f'{b} бiльше нiж {a} на ',z)
    else:
        print(f'{a} дорiвнює {b}')

comparTwo(x,y)