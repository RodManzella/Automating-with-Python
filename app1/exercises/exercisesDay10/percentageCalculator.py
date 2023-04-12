try:
    totalValue = float(input("Enter total value: "))
    partialValue = float(input("Enter partial value: "))

    percentage = (partialValue / totalValue) * 100
    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number. Run the program again.")


