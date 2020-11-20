# Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#    P.S. Повинен вертатись генератор.
#    P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range


#не працює, дічь 

def myRange(*args):
    if len(args) == 1:
        print(obj for obj in range(args(0))
    if len(args) == 2:
        print(obj for obj in range(args(0),args(1))
    if len(args) == 3:
       print(obj for obj in range(args(0),args(1),args(2))

myRange(4)