while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('files/subfiles/todos.txt', 'r') as file:
                todos = file.readlines()
                # don´t need to close the file
                # helps to avoid problems with file handling

            todos.append(todo)

            with open('files/subfiles/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | "display":
            with open('files/subfiles/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of todo to edit: "))
            number = number - 1

            with open('files/subfiles/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo")
            todos[number] = new_todo + '\n'

            with open('files/subfiles/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of todo to complete"))

            with open('files/subfiles/todos.txt', 'r') as file:  # lê o arquivo e salva conteúdo em lista (todos)
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip()
            todos.pop(index)

            with open('files/subfiles/todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        case 'exit':
            break

print("Bye!")




