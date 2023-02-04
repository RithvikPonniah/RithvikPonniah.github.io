dollars = int(input("how many dollars have you got: "))
euros = dollars * 0.95
print("you have got " , euros , "euros")
rank = ["john","sen","lisa"]
name = int(input("type the rank you want to knowout of 1, 2 or 3 "))
print(rank[name-1])

rank = ['John', 'Sen', 'Lisa']
name = input("Enter a name: ").capitalize()
rank1 = rank.index(name) + 1
print(rank1)