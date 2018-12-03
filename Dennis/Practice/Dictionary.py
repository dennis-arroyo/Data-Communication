dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['School'] = "DPS School";  # Add new entry

print("Name" in dict)

result = [key for key, value in dict.items() if key not in "Age"]

print("--")

for c in result:
    print("\t", c)

a = [["Dennis:10"], ["Elba:2"]]

b, c = a.split(":")

print(b)
print(c)

lst = []

lst.append([b, c])

print(lst)
