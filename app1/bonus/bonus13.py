feet_inches = input("Enter feet and inches")

def parse (feet_inches):
    parts = feet_inches.split(" ")  # creates a list using white-space as separation.
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}

    # when we return two variables, we get a tuple with both values.
    # we can also use dictionaries

    # ex: parse ("4 12")
    # (4.0, 12.0)

def convert (feet, inches):
    meters = (feet * 0.3048) + inches * 0.0254
    return meters


parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")

# How can we acess feet and inches local variables? (decoupling functions)

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use slide.")




