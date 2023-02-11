#todos = []
while True:
    userAction = input("Type add or show or exit or edit: ").strip()
    match userAction:
        case "add" | "create":

            todo = input('Enter the todo items you would like to add: ')+'\n'
            with open('files/todos.txt' , 'a') as fObject :
                fObject.write(todo)
        case "show" | "display":

            fObject = open('files/todos.txt', 'r')

            with open('files/todos.txt', 'r') as file :
                todos = fObject.readlines()

            for index , item in enumerate(todos):
                #x = x + 1
                item=item.strip('\n')
                row = f"{index+1}.{item}"

                print(row)
        case "complete" :
            fObject = open('files/todos.txt', 'r')

            with open('files/todos.txt', 'r') as file :
                todos = fObject.readlines()

            for index , item in enumerate(todos):
                row = f"{index+1}.{item}"
                print(row)
            complete = int(input("which line number did you complete"))
            todos.pop(complete - 1)
            with open('files/todos.txt', 'w') as file:
                fObject.writelines()
        case "exit":
            break
        case "edit":
            fObject = open('files/todos.txt', 'r')
            with open('files/todos.txt', 'r') as file :
                todos = fObject.readlines()

            y = int(input("what line do you want to edit: "))
            x = input("Enter the new value of the todo items: ")
            todos[y-1] = x

            with open('files/todos.txt','w') as fObject :
                fObject.writelines(todos)

        case 'clear' :
            clear = input("Are you sure you want to clear all your todos ? press  'y' to confirm ").strip()
            if clear == "y" :
                todos=[]
                fObject = open('files/todos.txt', 'w')
                with open('files/todos.txt', 'r') as file:
                    todos = fObject.writelines(todos)
        case other:
            print("You have entered",other, "the only commands accepted are add show and exit")
print("Bye,See you soon")