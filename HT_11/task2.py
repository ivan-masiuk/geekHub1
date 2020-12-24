# 2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів, 
# які зберігатиме в відповідні змінні. 
# Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
#    - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.

class Person(object):
    proffesion = ''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_age(self):
        print(self.age)
    
    def print_name(self):
        print(self.name)

    def show_all(self):
        print(self.name)
        print(self.age)

first_e = Person('Ivan', 18)
second_e = Person('Mishok', 18)

first_e.proffesion()