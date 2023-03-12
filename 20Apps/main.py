#todos = []
while True:
    userAction = input("Type add or show or exit or edit: ").strip()
    match userAction:
        case "add" | "create":
            todo = input('Enter the todo items you would like to add: ')+'\n'
            with open('files/todos.txt' , 'a') as fObject :
                fObject.write(todo)
        case "show" | "display":
            with open('files/todos.txt', 'r') as fObject :
                todos = fObject.readlines()

            for index , item in enumerate(todos):
                #x = x + 1
                item=item.strip('\n')
                row = f"{index+1}.{item}"

                print(row)
        case "complete" :

            with open('files/todos.txt', 'r') as fObject :
                todos = fObject.readlines()

            for index , item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}.{item}"
                print(row)
            complete = int(input("Pick the todo number you want to complete"))
            todos.pop(complete - 1)
            with open('files/todos.txt', 'w') as fObject:
                fObject.writelines(todos)
                print(f"You have completed the todo item'{item}'")
        case "exit":
            break
        case "edit":
            with open('files/todos.txt', 'r') as fObject :
                todos = fObject.readlines()

            y = int(input("what line do you want to edit: "))
            x = input("Enter the new value of the todo items: ")+'\n'
            z = todos[y-1]
            todos[y-1] = x
            with open('files/todos.txt','w') as fObject :
                fObject.writelines(todos)
            z=z.strip('\n')
            x=x.strip('\n')
            print(f"You have changed '{z}' into '{x}'")

        case 'clear' :
            clear = input("Are you sure you want to clear all your todos ? press  'y' to confirm ").strip()
            if clear == "y" :
                todos=[]
                with open('files/todos.txt', 'r') as fObject:
                    todos = fObject.writelines(todos)
        case other:
            print("You have entered",other, "the only commands accepted are add show and exit")
print("Bye,See you soon")