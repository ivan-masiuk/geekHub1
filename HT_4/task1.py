# Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
#    Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
#    Логіка наступна:
#        якщо введено коректну пару ім'я/пароль - вертається <True>;
#        якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException




# мабуть словник, а не список..?

namee = input ('Input your name: ')
passw = input ('Input your password: ')

def checkPassword (username, password, silent = False):
    whiteList = {'Ivan':'111i', 'Vitaliy':'222v', 'Anna':'333a', 'Misha':'444m', 'Marina':'555m' }
    for _ in whiteList:
        if username in whiteList:
            if password == whiteList[_]:
              silent = True
    # print (silent)
    return silent

print(checkPassword(namee, passw))