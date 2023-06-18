import todosModule
import PySimpleGUI as sg

label       = sg.Text("Type in a todo")
input       = sg.InputText(tooltip="Useless fellow" , key = "todo")
add         = sg.Button("Add")
list_box    = sg.Listbox(values=todosModule.getTodo(),key='todos',
                      enable_events=True,size=[45, 10])
edit = sg.Button("Edit")
win = sg.Window("My first window",layout=[[label],[input,add],[list_box,edit]],font=("Helvetica",20))
while True :
    event , values = win.read()
    print(event)
    print(values)
    match event :
        case "Add":
            todos = todosModule.getTodo()
            print (todos)
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            print (todos)
            todosModule.addTodo(todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = todosModule.getTodo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            todosModule.addTodo(todos)
        case sg.WIN_CLOSED:
            break
win.close()