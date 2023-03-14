password = input("Enter your password : ")
result = {}
if len(password) > 7:
    result["Length"]=True
else:
    result['Length']=False

passwordContainsNumber = any([char.isdigit() for char in password])
result['Digits']=passwordContainsNumber

passwordContainsUpper = any([char.isupper() for char in password])
result["upperCase"]=passwordContainsUpper
print(result)
if all(result.values()) :
    print("Strong Password")
else:
    print("Weak Password")