# Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат. 
# Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат. Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3


def def_1():
    print('Firs function output')
def def_2():
    print('Second function output')
def def_3():
    print('Third function output')
def def_4():
    def_1()
    def_2()
    def_3()

def_4()