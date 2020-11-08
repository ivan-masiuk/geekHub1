# Write a script to concatenate N strings.
N = int(input())
a_str =''
for i in range(N):
	print ('введите строку ',i+1)
	b_str = input()
	a_str += b_str
print(a_str)