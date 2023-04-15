
todos = []

while True:
    user_action = input("Type add, show, edit or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | "display":
            for item in todos:
                item = item.title()
                print(item)
        case 'edit':
            number = int(input("Number of todo to edit"))  #input function always returns a str
            number = number - 1
            todos[number] = input("Enter new todo")
        case 'exit':
            break
        case _:
            print("Invalid value")

print("Bye!")



