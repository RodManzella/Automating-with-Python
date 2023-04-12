def get_todos():
    with open('files/subfiles/todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]  # extracting all the characters of the String, starting from index 4

        todos = get_todos()

        todos.append(todo + "\n")

        with open('files/subfiles/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        number = int(user_action[5:])  # if user types "edit 2", we will get the 2(with slicing)

        number = number - 1

        todos = get_todos()

        new_todo = input("Enter a new todo")
        todos[number] = new_todo + '\n'

        with open('files/subfiles/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('complete'):
        number = int(user_action[9:])

        todos = get_todos()  # lê o arquivo e salva conteúdo em lista (todos)

        index = number - 1
        todo_to_remove = todos[index].strip()
        todos.pop(index)

        with open('files/subfiles/todos.txt', 'w') as file:
            file.writelines(todos)
        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid!")

print("bye!")

# String slicing:

#   user_action = 'add clean the bag'

#   user_action[4:] -->  clean the bag

#   user_action[4:8] --> clea    (4 to 8) 8 not included

#   user_action[4:9] --> clean






