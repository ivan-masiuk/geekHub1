# Write a script to remove duplicates from Dictionary.
dic1 = {} #початковий словник
result = {} #словник без duplicates

for key,value in dic1.items():
    if value not in result.values():
        result[key] = value

print (result)
