import PySimpleGUI as sg

label = sg.Text("Select files to compress")
Input = sg.Input()
choose_button = sg.FileBrowse("Choose")
label1 = sg.Text("Select destination")
input1 = sg.Input()
choose_button1 = sg.FolderBrowse('Choose')
compress = sg.Button("Compress")

win = sg.Window("File compressing" , layout=[[label,Input,choose_button],[label1,input1,choose_button1]])
win.read()
win.close()