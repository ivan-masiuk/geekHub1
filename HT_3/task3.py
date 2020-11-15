# Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте, и False - якщо ні.

a = int(input())

def is_prime(n):
    if n < 2:
        print("Число повинно бути більше ніж 2")
        quit()
    elif n == 2:
        print(True)
        quit()

    i = 2
    while i <= (n ** 0.5):
        if n % i == 0:
            print(False)
            quit()
        i += 1

    print(True)

if 0 <= a <= 1000:
    is_prime(a)
else:
    print('Число в іншому проміжку')

#https://pythoner.name/prime-number за основу брав цей код