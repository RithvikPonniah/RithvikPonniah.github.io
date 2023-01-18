todos = []
while True:
    userAction = input("Type add or show or exit: ").strip()
    match userAction:
        case "add" | "create":
            todo = input("Enter todo items you would like to add : ")
            todos.append(todo)
        case "show" | "display":
            x = 0
            for item in todos:
                x = x + 1
                print(x,".",item.title())
        case "exit":
            break
        case other:
            print("You have entered",other, "the only commands accepted are add show and exit")
print("Bye,See you soon")