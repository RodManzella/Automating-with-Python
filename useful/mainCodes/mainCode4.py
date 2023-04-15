while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('files/subfiles/todos.txt', 'r')  # file referencia objeto tipo file
            todos = file.readlines()  #file.readLines() retorna uma lista de itens do txt e salva em todos
            file.close()  # fecha o arquivo

            todos.append(todo)  # adiciona novo elemento em todos

            file = open('files/subfiles/todos.txt', 'w')   # file referencia objeto tipo file
            file.writelines(todos)  # file.writeLines() adiciona lista no txt
            file.close()  # fecha o arquivo

        case 'show' | "display":
            file = open('files/subfiles/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
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



