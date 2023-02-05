fObject = open('ESSAY.TXT' , 'r')
excercise = fObject.read()
print(excercise.title())

print(len(excercise[0]))

fileObject = open('members.txt' , 'r')
name = input("Add new name: ")+"\n"
members = fileObject.readlines()
fileObject.close()
members.append(name)
fileObject = open('members.txt' , 'w')
fileObject.writelines(members)

files = ['f1.txt','f2.txt','f3.txt']
for file in files :
    fileObject  = open(file , 'w')
    fileObject.write(f"am {file}")
    fObject.close()

for file in files :
    fileObject = open(file , 'r')
    read = fileObject.read()
    print(read)