age = int(input("how old are you: "))
nation = input("Which country where you born")
if (18 <= age ) :
    if (nation.capitalize() == "India") :
        print("You Can vote in india: ")
    else :
        print("sorry you cannot vote in india")
else :
    print("Sorry you are too young to vote in india: ")