#todos = []
fObject = open('files/todos.txt', 'r')
todos = fObject.readlines()
fObject.close()
fObject = open('files/todos.txt', 'w')
todos.append('bike')
fObject.writelines(todos)
todos.append('bike')
fObject.writelines(todos)
fObject.close()

while False:
    userAction = input("Type add or show or exit or edit: ").strip()
    match userAction:
        case "add" | "create":
            todo = input("Enter todo items you would like to add : ")+'\n'
            todos.append(todo)
            fObject.writelines(todos)

        case "show" | "display":
            #x = 0
            for index , item in enumerate(todos):
                #x = x + 1
                row = f"{index+1}.{item}"
                print(row)
        case "complete" :
            for index , item in enumerate(todos):
                row = f"{index+1}.{item}"
                print(row)
            complete = int(input("which line number did you complete"))
            todos.pop(complete - 1)
        case "exit":
            break
        case "edit":
            y = int(input("what line do you want to edit: "))
            x = input("Enter the new value of the todo items: ")
            todos[y-1] = x
        case other:
            print("You have entered",other, "the only commands accepted are add show and exit")
#fObject = open('todos.txt' , 'w')
print("Bye,See you soon")