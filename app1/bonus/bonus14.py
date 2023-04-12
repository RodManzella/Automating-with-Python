from bonus.converters14 import convert
from bonus.parsers14 import parse
# import parsers14    ---> parsers14.parse(feet_inches)

feet_inches = input("Enter feet and inches")

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")


if result < 1:
    print("Kid is too small")
else:
    print("Kid can use slide.")




