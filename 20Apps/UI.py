import PySimpleGUI
import todosModule
import time


PySimpleGUI.theme("DarkRed1")
clock = PySimpleGUI.Text('', key="Clock")
inputText = PySimpleGUI.InputText(tooltip='Input Todo here', key="todo")
add = PySimpleGUI.Button("Add")
ListTodos = PySimpleGUI.Listbox(values=todosModule.getTodo(), key='todos', enable_events=True, size=[45, 15])
completeTodo = PySimpleGUI.Listbox(values=todosModule.getTodo('complete.txt'), enable_events=True, size=[45, 15],
                                   key='CompleteTodos')
edit = PySimpleGUI.Button("Edit")
complete = PySimpleGUI.Button("Complete")
exit = PySimpleGUI.Button("Exit")

buttons = [add, edit, complete]
lay = []
for button in buttons:
    lay.append([button])
lay = [[inputText, add], [ListTodos, edit, complete,completeTodo],[exit,clock]]
window = PySimpleGUI.Window('Todo App', layout=lay, font=('Ariel', 20))
while True:
    event, value = window.read(timeout=200)
    window["Clock"].update(value=time.strftime("%b %d,%Y %H:%M:%S"))
    print(event)
    print(value)
    print(window)
    match event:
        case 'Add':
            todos = todosModule.getTodo()
            todos.append(value['todo'] + '\n')
            print(value['todo'])
            todosModule.addTodo(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try :
                oldTodo = value['todos'][0]
                newTodo = value['todo'] + '\n'
                todos = todosModule.getTodo()
                index = todos.index(oldTodo)
                todos[index] = newTodo
                todosModule.addTodo(todos)
                window['todos'].update(values=todos)
            except IndexError:
                PySimpleGUI.popup("Please select an item first",font=("Calibri",20))
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case 'Complete':
            try :
                oldTodo = todosModule.getTodo()
                removed = value['todos'][0]
                index = oldTodo.index(removed)
                todosModule.completeTodo(index + 1)
                completedTodos = todosModule.getTodo('complete.txt')
                completedTodos.append(removed)
                todosModule.addTodo(completedTodos, 'complete.txt')
                print(removed)
                window['todos'].update(values=todosModule.getTodo())
                window['CompleteTodos'].update(values=completedTodos)
                window['todo'].update(value='')
            except IndexError:
                PySimpleGUI.popup("Please select an item first",font=("Calibri",20))
        case "Exit" :
            break
        case PySimpleGUI.WIN_CLOSED:
            break
print("Jingunamani")
window.close()
