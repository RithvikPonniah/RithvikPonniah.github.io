#todos = []
def addTodo(filePath,todoItem):
    with open(filePath, 'a') as fObject:
        fObject.write(todoItem)
def editTodo(filePath,todoNumber):
    try:
        with open(filePath, 'r') as fObject:
            todos = fObject.readlines()
        x = input("Enter the new value of the todo items: ") + '\n'
        z = todos[ todoNumber- 1]
        todos[todoNumber - 1] = x
        with open(filePath, 'w') as fObject:
            fObject.writelines(todos)
        z = z.strip('\n')
        x = x.strip('\n')
        print(f"You have changed '{z}' into '{x}'")
    except IndexError :
        print("The given todo number " ,todoNumber,'does not exist')
def completeTodo(filePath,todoNumber):
    try :
        with open('files/todos.txt', 'r') as fObject:
            todos = fObject.readlines()
        todos.pop(complete - 1)
        with open('files/todos.txt', 'w') as fObject:
            fObject.writelines(todos)
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)
    except IndexError:
        print('The Index you have given is invalid')
def showTodo(filePath) :
    with open('files/todos.txt', 'r') as fObject:
        todos = fObject.readlines()
    for index, item in enumerate(todos):
        # x = x + 1
        item = item.strip('\n')
        row = f"{index + 1}.{item}"
        print(row)
def clearTodo(filePath):
    clear = input("Are you sure you want to clear all your todos ? press  'y' to confirm ").strip()
    if clear == "y":
        todos = []
        with open('files/todos.txt', 'w') as fObject:
            todos = fObject.writelines(todos)


while True:
    userAction = input("Type add or show or exit or edit: ").strip()

    if userAction.startswith('add ') or userAction.startswith('new '):
        todo = userAction[4:]+ '\n'
        addTodo('files/todos.txt',todo)
    elif userAction.startswith('edit '):
        try :
            y = int(userAction[5:])
            editTodo('files/todos.txt',y)
        except ValueError :
            print("Your command was invalid. try again.")
            continue
    elif userAction.startswith('complete '):

        complete = int(userAction[9:])
        completeTodo('files/todos.txt',complete)

    else:

        match userAction:
            case "add" | "create":
                todo = input('Enter the todo items you would like to add: ')+'\n'
                addTodo('files/todos.txt',todo)
            case "show" | "display":
                showTodo('files/todos.txt')
            case "complete" :
                complete = int(input("Pick the todo number you want to complete"))
                completeTodo('files/todos.txt',complete)
            case "exit":
                break
            case "edit":
                try :
                    y = int(input("what line do you want to edit: "))
                    editTodo('files/todos.txt', y)
                except ValueError:
                    print("Your command was invalid.Try again.")
                    continue
            case 'clear' :
                clearTodo('files/todos.txt')
            case other:
                print("You have entered",other, "the only commands accepted are add show and exit")
print("Bye,See you soon")

