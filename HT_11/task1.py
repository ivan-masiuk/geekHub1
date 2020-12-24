# 1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з 2-ма числами, 
# а саме додавання, віднімання, множення, ділення.
#    - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
#    - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
#    - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )


class Calc(object):
    last_result = None

    """простая модель калькулятора"""
    # def __init__(self, a, b):
    #     """инициализация атрибутов"""
    #     self.a = a
    #     self.b = b

    #sum method
    def summm(self, a, b):
        self.last_result = a + b
        return self.last_result

    #defference method
    def difference(self, a, b):
        self.last_result = a - b
        return self.last_result

    #mulriplication method
    def multiplication(self, a, b):
        self.last_result = a * b
        return self.last_result

    #devision method
    def division(self, a, b):
        if not(b == 0):
            self.last_result = a / b
        else:
            print("b should != 0")
        return self.last_result