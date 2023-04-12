import csv  # module to process csv files

# opened data.csv as file: the 'file' object is now in memory.
with open("weather.csv", 'r') as file:
    data = list(csv.reader(file))  # csv.reader(file) expects a file object as input
    # csv.reader(file) will give us something called an iterator obj instance
    # iterators are also types in python.
    #  iterators are not readable, so we need to convert it to a list.
print(data)  # list of lists, and each of these lists represent one row.

# How can you use this data in real life?
# you could create an algorithm to access the temperature of a given value.

city = input("Enter a city: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])

# Visualization of what 'data':
# data = [['Station', 'Temperature'], ['Kuala Lumpur', '45'], ['New York', '20']]

# if we do: for row in data[1:]
# data[1:] will be: [['Kuala Lumpur', '45'], ['New York', '20']]

# In the first iteration, row will be ['Kuala Lumpur', '45']: row[0] = 'Kuala Lumpur'; row[1] = 45........




