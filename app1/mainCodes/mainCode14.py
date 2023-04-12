# from functions import get_todos, write_todos  (this case is better if you have just a few functions)
import functions14  # importing module

# from modules import functions (if functions.py was inside 'modules' directory)

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions14.get_todos()  # using get_todos from functions module.

        todos.append(todo + "\n")

        functions14.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions14.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        number = int(user_action[5:])  # if user types "edit 2", we will get the 2(with slicing)

        number = number - 1

        todos = functions14.get_todos()

        new_todo = input("Enter a new todo")
        todos[number] = new_todo + '\n'

        functions14.write_todos(todos)

    elif user_action.startswith('complete'):
        number = int(user_action[9:])

        todos = functions14.get_todos()  # lê o arquivo e salva conteúdo em lista (todos)

        index = number - 1
        todo_to_remove = todos[index].strip()
        todos.pop(index)

        functions14.write_todos(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid!")

print("bye!")

#








