#todos = []
while True:
    userAction = input("Type add or show or exit or edit: ").strip()
    match userAction:
        case "add" | "create":
            #fObject = open('files/todos.txt', 'r')
            #todos = fObject.readlines()
            #fObject.close()

            # todo = input("Enter todo items you would like to add : ")+'\n'
            #todos.append(todo)
            #fObject = open('files/todos.txt', 'w')
            #fObject.writelines(todos)
            #fObject.close()
            todo = input('Enter the todo items you would like to add: ')+'\n'
            fObject = open('files/todos.txt' , 'a')
            fObject.write(todo)
            fObject.close()
        case "show" | "display":
            #x = 0
            fObject = open('files/todos.txt', 'r')
            todos = fObject.readlines()
            fObject.close()
            todos1 = [item.strip('\n') for item in todos]

            #for item1 in todos :
            #    new_item = item1.strip('\n')
            #    todos1.append(new_item)
            for index , item in enumerate(todos1):
                #x = x + 1
                row = f"{index+1}.{item}"
                print(row)
        case "complete" :
            fObject = open('files/todos.txt', 'r')
            todos = fObject.readlines()
            fObject.close()
            for index , item in enumerate(todos):
                row = f"{index+1}.{item}"
                print(row)
            complete = int(input("which line number did you complete"))
            todos.pop(complete - 1)
            fObject = open('files/todos.txt', 'w')
            fObject.writelines(todos)
            fObject.close()
        case "exit":
            break
        case "edit":
            fObject = open('files/todos.txt', 'r')
            todos = fObject.readlines()
            fObject.close()
            y = int(input("what line do you want to edit: "))
            x = input("Enter the new value of the todo items: ")
            todos[y-1] = x
            fObject = open('files/todos.txt', 'w')
            fObject.writelines(todos)
            fObject.close()

        case 'clear' :
            clear = input("Are you sure you want to clear all your todos ? press  'y' to confirm ").strip()
            if clear == "y" :
                #fObject = open('files/todos.txt', 'r')
                #todos = fObject.readlines()
                #fObject.close()
                #todos.clear()
                todos=[]
                fObject = open('files/todos.txt', 'w')
                fObject.writelines(todos)
                fObject.close()
        case other:
            print("You have entered",other, "the only commands accepted are add show and exit")
print("Bye,See you soon")