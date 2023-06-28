import PySimpleGUI
from ZipExtractor import ExtractArchive


PySimpleGUI.theme("DarkBrown4")
Title= PySimpleGUI.Text("Archive Extractor")
File_Input_Text = PySimpleGUI.Text("File Name")
File_Input = PySimpleGUI.InputText("File Name" , key="ZipName")
ChooseButton1 = PySimpleGUI.FileBrowse("Choose")
File_Output_Text = PySimpleGUI.Text("Destination")
File_Output = PySimpleGUI.InputText("Destination",key="Destination")
ChooseButton2 = PySimpleGUI.FolderBrowse("Choose")
Extract = PySimpleGUI.Button("Extract")
OutputLabel = PySimpleGUI.Text(key='Output', text_color="green")

window = PySimpleGUI.Window(Title,layout=[[File_Input_Text,File_Input,ChooseButton1],
                                         [File_Output_Text,File_Output,ChooseButton2],
                                         [Extract,OutputLabel]])
while True:
    event , value = window.read()
    print(event,value)
    arhivepath = value["Choose"]
    dest_dir = value["Destination"]
    ExtractArchive(arhivepath,dest_dir)
    window['Output'].update(value="Extraction Succesful")
window.close()