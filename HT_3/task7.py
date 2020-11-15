# Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.

lst = [1,2,3,4,4,4,4,1,3,1,1]

def elements(el):
    a = {}
    for i in el:
        if i in a.keys():
            b = a[i]
            a.pop(i)
            a[i] = b+1
        else:
            a[i] = 1
    print(a)
    return(a)

elements(lst)
