def age(year_of_birth, current_year=2023):
    user_age = current_year - year_of_birth
    return user_age


birth = int(input("What is your year of birth?"))

current_age = age(birth)

if current_age > 120:
    print("Bro how are you alive")

