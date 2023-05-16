import PySimpleGUI as sg

label = sg.Text("Enter feet")
Input = sg.Input()
label1 = sg.Text("Enter inches")
Input1 = sg.Input()
button = sg.Button("Convert")

win = sg.Window("Convertor" , layout=[[label,Input],[label1,Input1],[button]])
win.read()
win.close()