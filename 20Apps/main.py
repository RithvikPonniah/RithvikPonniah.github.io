todos = []
while True:
    userAction = input("Type add or show or exit or edit: ").strip()
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
        case "edit":
            y = int(input("what line do you want to edit: "))
            x = input("Enter the new value of the todo items: ")
            todos[y-1] = x
        case other:
            print("You have entered",other, "the only commands accepted are add show and exit")
print("Bye,See you soon")