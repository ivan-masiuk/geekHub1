# Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.
n = int(input())

def square(a):
  l = []
  l.append (4 * a)
  l.append (a * a)
  l.append (a * (2 ** 0.5))
  print(tuple(l))
  return(tuple(l))

square(n) 