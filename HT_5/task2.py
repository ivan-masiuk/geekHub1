    
#     # Програма-світлофор.
#    Створити програму-емулятор світлофора для авто і пішоходів.
#    Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
#    Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
#    Приблизний результат роботи наступний:   Red        Green
#       Red        Green
    #   Red        Green
    #   Red        Green
    #   Yellow     Green
    #   Yellow     Green
    #   Green      Red
    #   Green      Red
    #   Green      Red
    #   Green      Red
    #   Yellow     Red
    #   Yellow     Red

import time

def redCar():
    carLight = 'Red'
    walkerLight = 'Green'
    for _ in range(3):
        print('{0:10}  {1}'.format(carLight, walkerLight))
        time.sleep(1)

def greenCar():
    carLight = 'Green'
    walkerLight = 'Red'
    counter = 0
    for _ in range(3):
        print('{0:10}  {1}'.format(carLight, walkerLight))
        time.sleep(1)

def yellowCar():
    carLight = 'Yellow'
    walkerLight = 'Green'
    counter = 0
    for _ in range(2):
        print('{0:10}  {1}'.format(carLight, walkerLight))
        time.sleep(1)

while True:
    redCar()
    yellowCar()
    greenCar()