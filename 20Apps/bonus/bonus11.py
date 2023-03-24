def sumList(listA):
    sum = 0
    for number in listA :
        sum = sum + number
    return sum
def aadhiLang():
    return 'AAAA AAAA AAAAA AAA AAAA', 'SKADAPOP','SKIBIDI DOP'
with open('data.txt' , 'r') as fObject :
    data = fObject.readlines()
data = [int(item.strip('\n')) for item in data[1:]]
#print(sum(data)/len(data))
sum = sumList(data)
print(sum/len(data))
print(aadhiLang())

