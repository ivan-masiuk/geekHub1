# Write a script to check whether a specified value is contained in a group of values.
#         Test Data :
#         3 -> [1, 5, 8, 3] : True
#         -1 -> (1, 5, 8, 3) : False
print('give me value')
n = input()
print('give me group of values, like 12,15,14')
s = input()

g = s.split(',')
if n in g:
  print('True')
else: 
  print('False')