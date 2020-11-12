# Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#    Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя

n = input()

def potiziavPoKlavi (x):
    if len(x) in range(30,50+1):
        print ('Довжина тицьки: ',len(x))
        ctNumber = 0
        ctStr = 0
        for obj1 in x:  
          if obj1.isdigit():
            ctNumber +=1
          else:
            ctStr +=1   
        print('Кількість цифр: ', ctNumber)
        print('Кількість не цифр: ', ctStr)

    elif len(x) in range(31):
        print ('Довжина тицьки: ',len(x))
        ctNumber = 0
        newStr = ''
        for obj1 in x:  
          if obj1.isdigit():
            ctNumber +=1
          else:
            newStr += obj1
        print('Кількість цифр: ', ctNumber)
        print('Строка без цифр', newStr)
        
    else:
        print(f'ого, {len(x)} раз тицьнув')

potiziavPoKlavi(n)