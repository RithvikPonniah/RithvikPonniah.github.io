
UserAction = input("Do you want to add,edit,show or complete : ")
UserInput = UserAction.split('-')
NewUserAct = [item.strip() for item in UserInput]

if NewUserAct[0] == 'add' :
    with open('Newtodo.txt','a') as fileObject :
        print(NewUserAct[1])
        fileObject.write(NewUserAct[1]+'\n')