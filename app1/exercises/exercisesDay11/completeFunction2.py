def get_max():
    grades = [9.6, 9.2, 9.7]
    max_value = max(grades)
    min_value = min(grades)
    message = f"Max: {max_value}, Min: {min_value}"
    return message


maxMin = get_max()
print(maxMin)

