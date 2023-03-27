#todos = []
#from todosModule import addTodo
#from todosModule import editTodo
#from todosModule import showTodo
#from todosModule import completeTodo
#from todosModule import clearTodo
import todosModule

while True:
    userAction = input("Type add or show or exit or edit: ").strip()

    if userAction.startswith('add ') or userAction.startswith('new '):
        todo = userAction[4:]+ '\n'
        todosModule.addTodo(todo)
    elif userAction.startswith('edit '):
        try :
            y = int(userAction[5:])
            todosModule.editTodo(y)
        except ValueError :
            print("Your command was invalid. try again.")
            continue
    elif userAction.startswith('complete '):

        complete = int(userAction[9:])
        todosModule.completeTodo(complete)

    else:

        match userAction:
            case "add" | "create":
                todo = input('Enter the todo items you would like to add: ')+'\n'
                todosModule.addTodo(todo)
            case "show" | "display":
                todosModule.showTodo()
            case "complete" :
                complete = int(input("Pick the todo number you want to complete"))
                todosModule.completeTodo(complete)
            case "exit":
                break
            case "edit":
                try :
                    y = int(input("what line do you want to edit: "))
                    todosModule.editTodo(y)
                except ValueError:
                    print("Your command was invalid.Try again.")
                    continue
            case 'clear' :
                todosModule.clearTodo()
            case other:
                print("You have entered",other, "the only commands accepted are add show and exit")
print("Bye,See you soon")

