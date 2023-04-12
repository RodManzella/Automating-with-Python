while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]  # extracting all the characters of the String, starting from index 4

        with open('files/subfiles/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('files/subfiles/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('files/subfiles/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif 'edit' in user_action:
        try:
            number = int(user_action[5:])  # if user types "edit 2", we will get the 2(with slicing)

            number = number - 1

            with open('files/subfiles/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo")
            todos[number] = new_todo + '\n'

            with open('files/subfiles/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue  #goes to loop again

    elif 'complete' in user_action:
        try:
            number = int(user_action[9:])

            with open('files/subfiles/todos.txt', 'r') as file:  # lê o arquivo e salva conteúdo em lista (todos)
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip()
            todos.pop(index)

            with open('files/subfiles/todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid!")

print("bye!")








