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

            new_todos = []

            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)
            print(todos)

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

# enumerate function returns an enumerate object (returns a list made of tuples)

# a = enumerate (["a", "b", "c"])
# a
# enumerate object at 0x102312500>
# list(a)
# [(0, 'a'), (1, 'b'), (2, 'c')]

# for i, item in enumerate(a):
#               |
# for i, item in [(0, 'a'), (1, 'b'), (2, 'c')]


# b = enumerate("Hello")
# list(b)    ---> converts to list
# [(0, 'H'), (1, 'e') ....]



