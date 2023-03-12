
while True :
    userIntput = input("Do you want to add or show or edit or exit: ").strip()
    match userIntput :
        case "add" :
            fileObject = open("todo.txt" , 'a')
            todo = input("Please enter what you want to do ")+'\n'
            fileObject.write(todo)
            fileObject.close()
        case "show" :
            fileObject = open('todo.txt' , 'r')
            todoList = fileObject.readlines()
            for index,todo in enumerate(todoList) :
                print(f"{index+1}. {todo.strip()}")
            fileObject.close()
        case "edit" :
            with open('todo.txt','r') as fileObject :
                todoList = fileObject.readlines()
            for index,todo in enumerate(todoList) :
                print(f"{index+1}. {todo.strip()}")
            line = int(input("which item number do you want to edit"))
            newValue = input("enter new todo")
            todoList[line - 1] = newValue.capitalize()+'\n'
            with open('todo.txt' , 'w') as fileObject :
                fileObject.writelines(todoList)
        case 'complete' :
            with open('todo.txt','r') as fileObject :
                todoList = fileObject.readlines()
            for index,todo in enumerate(todoList):
                print(f'{index +1}. {todo.strip()}')
            linenumber = int(input("What todo # did you complete ? : "))
            todoList.pop(linenumber-1)
            with open('todo.txt','w') as fileObject :
                fileObject.writelines(todoList)
        case "exit" :
            break



















