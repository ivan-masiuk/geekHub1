# 2. Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» 
# та приймав кольор фігури при створенні екземпляру, а методи __init__ підкласів доповнювали його 
# та додавали початкові розміри.

class figure(): 
    def __init__(self, color):
        self.color = color
    def changeColor(self, new_color):
        self.color = new_color

class oval(figure):
    def __init__(self, color, radius):
        figure.__init__(self,color)
        self.radius = radius

class square(figure):
    def __init__(self, color, side):
        figure.__init__(self,color)
        self.side = side

# test
a = figure('Blue')
print(a.color)

classOval1 = oval('red',5)
print(classOval1.radius)
print(classOval1.color)