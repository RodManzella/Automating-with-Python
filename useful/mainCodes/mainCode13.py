def get_todos(filepath="files/subfiles/todos.txt"):  # docstrings are useful for documentation of functions
    """ Read a text file and return a list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
    # all get_todo() calls will have this argument(filepath) as default. (default args)


def write_todos(todos_arg, filepath="files/subfiles/todos.txt"):
    """ Write the to-do items list in the next file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

# it is not interesting for todos_arg to have a default arg, because todos_arg is always changing
# When provided with a default arg, the non-default arg should be put in first place.

# docstrings can also be used for multi-line strings(break-lines are recognized by default)


text = """
Principles of productivity.
Managing your inflow.
Systemizing.
"""


while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

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

        write_todos(todos)

    elif user_action.startswith('complete'):
        number = int(user_action[9:])

        todos = get_todos()  # lê o arquivo e salva conteúdo em lista (todos)

        index = number - 1
        todo_to_remove = todos[index].strip()
        todos.pop(index)

        write_todos(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid!")

print("bye!")

#








