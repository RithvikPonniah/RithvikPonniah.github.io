import PySimpleGUI
import todosModule
inputText = PySimpleGUI.InputText(tooltip='Input Todo here',key="todo")
add = PySimpleGUI.Button("Add")
ListTodos = PySimpleGUI.Listbox(values=todosModule.getTodo(), key='todos',enable_events=True,size=[45,15])
edit = PySimpleGUI.Button("Edit")


buttons = [add,edit]
lay=[]
for button in buttons:
    lay.append([button])
lay =   [[inputText,add],[ListTodos,edit]]
window = PySimpleGUI.Window('Todo App',layout=lay,font=('Ariel',20))
while True:
    event,value = window.read()
    print(event)
    print(value)
    print(window)
    match event :
        case 'Add' :
            todos = todosModule.getTodo()
            todos.append(value['todo']+'\n')
            print(value['todo'])
            todosModule.addTodo(todos)
            window['todos'].update(values=todos)
        case 'Edit' :
            oldTodo = value['todos'][0]
            newTodo = value['todo'] + '\n'
            todos = todosModule.getTodo()
            index = todos.index(oldTodo)
            todos[index] = newTodo
            todosModule.addTodo(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case PySimpleGUI.WIN_CLOSED:
            exit('Bye')
print("Jingunamani")
window.close()
