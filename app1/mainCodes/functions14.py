def get_todos(filepath="files/subfiles/todos.txt"):
    """ Read a text file and return a list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="files/subfiles/todos.txt"):
    """ Write the to-do items list in the next file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())

# nothing inside this condition will be executed by main.
