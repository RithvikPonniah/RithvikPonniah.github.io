todos = []
while True:
    userAction = input("Type add or show or exit: ").strip()
    match userAction:
        case "add":
            todo = input("Enter todo items you would like to add : ")
            todos.append(todo)
        case "show":
            x = 0
            for item in todos:
                x = x + 1
                print(x,".",item)
        case "exit":
            break
        case other:
            print("Only supported actions are add and show")
print("Bye,See you soon")