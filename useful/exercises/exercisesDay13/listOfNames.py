def name_list_maker(names_local):
    names_list = names_local.split(',')
    return len(names_list)


names = input("Enter names separated by commas (no spaces): ")

name_amount = name_list_maker(names)
print(name_amount)

