# Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
#         Sample data : 1, 5, 7, 23
#         Output :
#         List : [‘1', ' 5', ' 7', ' 23']
#         Tuple : (‘1', ' 5', ' 7', ' 23')
a = input() 
a_list = a.split(',')
a_tuple = tuple(a_list)

print(a_list)
print(a_tuple)

# check type
# print(type(a_list))
# print(type(a_tuple))