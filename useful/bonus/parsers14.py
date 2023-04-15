def parse (feet_inches):
    parts = feet_inches.split(" ")  # creates a list using white-space as separation.
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}
