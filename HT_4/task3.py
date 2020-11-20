# На основі попередньої функції створити наступний кусок кода:
#    а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#    б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#       Name: vasya
#       Password: wasd
#       Status: password must have at least one digit
#       -----
#       Name: vasya
#       Password: vasyapupkin2000
#       Status: OK
#    P.S. Не забудьте використати блок try/except ;)


# мабуть словник, а не список..? 

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


# перші дві пари валідні, інші з помилками
whiteList = {'Ivan':'1asdf11i', 'Vitaliy':'22asdf2v', 'Anna':'aaaaaaaaaaa', 'Mi':'4asdf44m', 'Marina':'12' }


# тестим

for _ in whiteList:
    try:
        dataValidation(_, whiteList[_])
    except Exception as e:
        print('Name:', _)
        print('Password: ', whiteList[_])
        print('Status: ', e)
    else:
        print('Name:', _)
        print('Password: ', whiteList[_])
        print('Status: OK')
