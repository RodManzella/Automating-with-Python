while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('files/subfiles/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('files/subfiles/todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show' | "display":
            file = open('files/subfiles/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # List comprehension
            new_todos = [item.strip('\n') for item in todos]  # iterate over todos list, store item.strip() in new_todos

            for index, item in enumerate(new_todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of todo to edit"))
            number = number - 1
            todos[number] = input("Enter new todo")
        case 'complete':
            number = int(input("Number of todo to complete"))
            todos.pop(number - 1)
        case 'exit':
            break

print("Bye!")