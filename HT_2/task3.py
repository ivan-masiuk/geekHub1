# Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
n = int(input())

def season (x):
    if x in [12,1,2]:
        print('Winter')
    elif x in [3,4,5]:
        print('Spring')
    elif x in [6,7,8]:
        print('Summer')
    elif x in [9,10,11]:
        print('Aughtum')
    else:
        print('12 місяців у році, спробуй ще раз!')

season(n)