# Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.


#  Не працює!

f = int(input())
h = int(input())


def is_prime(n):
    if n < 2:
        q = False
        quit()
    elif n == 2:
        q = True
        quit()
    i = 2
    while i <= (n ** 0.5):
        if n % i == 0:
            q = False
            quit()
        i += 1
    q = True
    # print(q)
    return(q)


def prime_list(a,b):
    listOne = []
    for _ in range(a,b+1):
        if is_prime(_):
            listOne.append(_)
    print(listOne)
    return(listOne)


if h > f:
    prime_list(f,h)
else:
     print('Введіть правильні значення')