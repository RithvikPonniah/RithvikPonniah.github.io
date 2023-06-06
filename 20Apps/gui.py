import todosModule
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input = sg.InputText(tooltip="Useless fellow" , key = "todo")
add = sg.Button("Add")

win = sg.Window("My first window",
                layout=[[label],[input,add]],
                font=("Helvetica",20))
while True :
    event , values = win.read()
    print(event)
    print(values)
    match event :
        case "Add":
            todos = todosModule.getTodo()
            new_todo = values['todo']
            todos.append(new_todo)
            todosModule.addTodo(todos)
win.close()