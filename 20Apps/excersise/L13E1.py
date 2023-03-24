def age(YearBorn,CurrentYear =2023):
    return CurrentYear - YearBorn
userBorn = int(input("Enter year of birth : "))
userAge = age(userBorn)
if userAge>= 18 :
    print(userAge)
    print("You are old")