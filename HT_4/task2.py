# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#    - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#    - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#    - щось своє :)
# Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.

namee = input ('Input your name: ')
passw = input ('Input your password: ')
       
# функція перевірки наявності чисел у паролі
def checkDigitPass(password, silentPass = False):
    for _ in password:
        if _.isdigit():
            silentPass = True
            break
    # рейз помилки якщо немає цифр
    if silentPass == False:
        raise Exception('any digits in password')
    return silentPass

# функція перевірки правильності написання імені та паролю
def dataValidation (username, password, silent = False):
    if 3 < len(username) < 50:
        if len(password) > 8 and checkDigitPass(password):
            silent = True
        # рейз помилки про довжину пароля
        if len(password) < 8:
            raise Exception('len password should be in (8;+00)')
    else:
        # рейз помилки про довжину імені
        raise Exception('len username should be in (3;50)')
    return silent

print(dataValidation(namee, passw))