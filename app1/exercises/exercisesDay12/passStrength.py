def password_strength(password):
    result = {}
    default = "Weak password"

    if len(password) >= 8:
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

    if all(result.values()):
        default = "Strong password"

    return default
