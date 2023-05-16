import todosModule
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input = sg.InputText(tooltip="Useless fellow")
add = sg.Button("Add")

win = sg.Window("My first window",layout=[[label],[input,add]])
win.read()