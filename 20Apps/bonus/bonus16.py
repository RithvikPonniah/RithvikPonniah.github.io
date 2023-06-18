import PySimpleGUI as sg
from zip_creator import make_Archive

label = sg.Text("Select files to compress")
Input = sg.Input()
choose_button = sg.FileBrowse("Choose" , key="files")
label1 = sg.Text("Select destination")
input1 = sg.Input()
choose_button1 = sg.FolderBrowse('Choose' , key="folder")
compress = sg.Button("Compress")
Output = sg.Text(key="output", text_color="green")

win = sg.Window("File compressing" , layout=[[label,Input,choose_button],[label1,input1,choose_button1],[compress,Output]])
while True :
    event , value = win.read()
    print(event,value)
    filepath = value["files"].split(';')
    Folder =  value['folder']
    make_Archive(filepath, Folder)
    win["output"].update(values="Compression Successful")
win.close()