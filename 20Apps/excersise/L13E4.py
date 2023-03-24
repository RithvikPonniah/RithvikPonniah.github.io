def listLen(list):
    x=0
    for item in list :
        x=x+1
    return x



Friends = input("Enter all your friends name with coma seperated without spaces : ")
friendsList=listLen(Friends.split(","))
print(f'You have {friendsList} Friends')
