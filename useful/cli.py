import functions
import time  # time module(contains code) but is located somewhere in the py install directory

# 4 important modules: csv, glob, webbrowser, shutil.
# these are demonstrated in codeExperiments directory.



now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        number = int(user_action[5:])

        number = number - 1

        todos = functions.get_todos()

        new_todo = input("Enter a new todo")
        todos[number] = new_todo + '\n'

        functions.write_todos(todos)

    elif user_action.startswith('complete'):
        number = int(user_action[9:])

        todos = functions.get_todos()

        index = number - 1
        todo_to_remove = todos[index].strip()
        todos.pop(index)

        functions.write_todos(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid!")

print("bye!")

#








