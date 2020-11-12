# Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).

startYear = int(input())
endYear = int(input())
vYears = []

for i in range(startYear, endYear+1):
    if (i%400==0 or (i%4==0 and i%100!=0 )):
        vYears.append(str(i))
# print(vYears)   список років (тип список)

# гарний output
print(', '.join(vYears))