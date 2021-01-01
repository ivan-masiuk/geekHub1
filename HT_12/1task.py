# Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color
# з початковим значенням white і метод для зміни кольору фігури, а його підкласи «овал» (oval) 
# і «квадрат» (square) містять методи __init__ для завдання початкових розмірів об'єктів при їх створенні.

class figure():
    color = 'white'
    def changeColor(self, new_color):
        self.color = new_color

class oval(figure):
    def __init__(self, radius):
        self.radius = radius

class square(figure):
    def __init__(self,side):
        self.side = side

# test
classOval1 = oval(5)
print(classOval1.color)