list = ["Rithvik\n","Aadhi\n","Amma\n"]
print(list)
list2 = [item.replace('\n','') for item in list]
list1 = []
for item in list :
    item = item.replace("\n",'')
    list1.append(item)
print(list2)

list = ["1.Rithvik","2.Aadhi","3.Amma"]
list = [item.replace('.','-')+'.txt'  for item in list]
print(list)

