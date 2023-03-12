
while True :
    userIntput = input("Do you want to add or show or edit or exit: ").strip()
    Useraction = userIntput.split('-')
    NuserAction = [item.strip() for item in Useraction]
    print (Useraction)
    print (NuserAction)
    if NuserAction[0] == 'add':
        with open('todo.txt','a') as fileObject :
            fileObject.write(NuserAction[1]+'\n')
    if NuserAction[0] == 'show' :
        with open('todo.txt' , 'r') as fileObject:
            ShowLines = fileObject.readlines()
        for index,item in enumerate(ShowLines) :
                print(f'{index+1}. {item}')
    if NuserAction[0] == 'edit':
        with open('todo.txt' , 'r') as fileObject:
            ShowLines = fileObject.readlines()
        for index,item in enumerate(ShowLines) :
                print(f'{index-1}. {item}')
        line = input('Which line number do you want to edit : ')
        Newvalue = input("Enter new value : ")
        ShowLines[line-1] = Newvalue
    if NuserAction[0] == 'complete':
        with open('todo.txt' , 'r') as fileObject:
            ShowLines = fileObject.readlines()
        for index,item in enumerate(ShowLines) :
                print(f'{index-1}. {item}')
        line = input('Which todo number do you want to complete : ')
        ShowLines.pop(line-1)