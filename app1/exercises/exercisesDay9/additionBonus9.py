password = input("Enter new password")

result = {}


if len(password) >= 7:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digits"] = digit

uppercase = False

for i in password:
    if i.isupper():
        upper = True
result["upper-case"] = uppercase

print(result)

if all(result.values()):
    if len(password) == 7:
        print("Password is OK, but not too strong")
    else:
        print("Strong Password")
else:
    print("Weak Password")

# all(result) is going to return False, if at least one of the elements is False

# Dictionaries are lists, but with a classification(key) on each index

# normal list: a = [14, 20, 30]

# Dictionary: b = {"height":14, "width": 200, "depth:30"}

# b ["width] = 200

# height is the key, 14 is the value...

# Lists are useful when grouping similar items, Dictionaries are useful when grouping different items(label)

# result in the last if looks at key, to check the values, use a function: result.values()