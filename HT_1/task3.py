# Write a script to sum of the first n positive integers.
n = int(input())
s = 0
for i in range(n+1):
	s += i
print(s)