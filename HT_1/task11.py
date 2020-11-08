# Write a script to remove duplicates from Dictionary.

result = {}

for key,value in dic1.items():
    if value not in result.values():
        result[key] = value

print result