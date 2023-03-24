def passwordCheck(PWD):
    password = []
    if len(PWD) >= 8:
        password.append(True)
    else:
        password.append(False)
    passWordDigit = [item.isdigit() for item in PWD]
    password.append(any(passWordDigit))
    passWordUpper = [item.isupper() for item in PWD]
    password.append(any(passWordUpper))
    if '@' in PWD :
        password.append(True)
    elif '!' in PWD :
        password.append(True)
    elif '_' in PWD:
        password.append(True)
    elif '-' in PWD :
        password.append(True)
    else:
        password.append(False)
    return password


password = input('Enter Password : ')
passCheck = passwordCheck(password)
if all(passCheck) :
    print("Your password is strong.")
else:
    print("Your wassword is too weak")
    error=''
    if passCheck[0] == False :
        error=error+"Your password does not have 8 characters. " + '\n'
    if passCheck[1] == False :
        error = error+"Your password does not have any digits."+'\n'
    if passCheck[2] == False :
        error=error+"Your password does not have any uppercase characters.""\n"
    if passCheck[3] == False :
        error=error+"Your password does not contain any special characters.""\n"
    exit(error)