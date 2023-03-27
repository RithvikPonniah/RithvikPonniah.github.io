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
        todos.pop(todoNumber - 1)
        writeToFile(todos,filePath)
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
        writeToFile(todos,filePath)

if __name__ == '__main__' :
    print(__name__)
    print ("Burgundi")