# 4. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.

class Test():
    counter = 0
    def __init__(self):
        self.__class__.counter += 1


# test

a = Test()
aasdn = Test()
aasd = Test()

print(Test.counter)