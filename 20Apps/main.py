#todos = []
def writeToFile(todos,filePath='files/todos.txt'):
    with open(filePath, 'w') as fObject:
        fObject.writelines(todos)

def getTodo(filePath='files/todos.txt'):
    with open(filePath, 'r') as fObject:
        dodo =  fObject.readlines()
    return dodo

def addTodo(todoItem,filePath='files/todos.txt'):
    with open(filePath, 'a') as fObject:
        fObject.write(todoItem)
def editTodo(todoNumber,filePath='files/todos.txt'):
    try:
        todos = getTodo()
        x = input("Enter the new value of the todo items: ") + '\n'
        z = todos[ todoNumber- 1]
        todos[todoNumber - 1] = x
        writeToFile(todos)
        z = z.strip('\n')
        x = x.strip('\n')
        print(f"You have changed '{z}' into '{x}'")
    except IndexError :
        print("The given todo number " ,todoNumber,'does not exist')
def completeTodo(todoNumber,filePath='files/todos.txt'):
    try :
        todos = getTodo(filePath)
        todos.pop(complete - 1)
        writeToFile(filePath,todos)
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)
    except IndexError:
        print('The Index you have given is invalid')
def showTodo(filePath='files/todos.txt') :
    todos = getTodo(filePath)
    for index, item in enumerate(todos):
        # x = x + 1
        item = item.strip('\n')
        row = f"{index + 1}.{item}"
        print(row)
def clearTodo(filePath='files/todos.txt'):
    clear = input("Are you sure you want to clear all your todos ? press  'y' to confirm ").strip()
    if clear == "y":
        todos = []
        writeToFile(filePath,todos)


while True:
    userAction = input("Type add or show or exit or edit: ").strip()

    if userAction.startswith('add ') or userAction.startswith('new '):
        todo = userAction[4:]+ '\n'
        addTodo(todo)
    elif userAction.startswith('edit '):
        try :
            y = int(userAction[5:])
            editTodo(y)
        except ValueError :
            print("Your command was invalid. try again.")
            continue
    elif userAction.startswith('complete '):

        complete = int(userAction[9:])
        completeTodo(complete)

    else:

        match userAction:
            case "add" | "create":
                todo = input('Enter the todo items you would like to add: ')+'\n'
                addTodo(todo)
            case "show" | "display":
                showTodo()
            case "complete" :
                complete = int(input("Pick the todo number you want to complete"))
                completeTodo(complete)
            case "exit":
                break
            case "edit":
                try :
                    y = int(input("what line do you want to edit: "))
                    editTodo(y)
                except ValueError:
                    print("Your command was invalid.Try again.")
                    continue
            case 'clear' :
                clearTodo()
            case other:
                print("You have entered",other, "the only commands accepted are add show and exit")
print("Bye,See you soon")

