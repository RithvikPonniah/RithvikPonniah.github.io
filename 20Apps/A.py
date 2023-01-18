while True :
    x=0
    name = input("enter your name : ")
    for alphabet in name:
        if (alphabet== "a" or alphabet== "A"):
            x=x+1
    print("The number of A's in your name is " , x)