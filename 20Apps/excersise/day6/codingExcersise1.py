#Please download the essay.txt file from the resources of this article.
# Then, create a program that reads that file and prints out its text.
# The first letter of each word in the output should be uppercase.
fObject = open('ESSAY.TXT' , 'r')
excercise = fObject.read()
print(excercise.title())

#Write a program that reads the essay.txt file and
# returns the number of characters contained in the file.
print(len(excercise[0]))

#Please download the members.txt file from the resources of this article.
#Then, create a program that, whenever executed,
# asks the user to enter a new member in the command line:
#Then, the member is added to members.txt. In this case, the text file content would be:

#John Smith
#Sen Lakmi
#Sono Octonot
#Solomon Right


fileObject = open('members.txt' , 'r')
name = input("Add new name: ")+"\n"
members = fileObject.readlines()
fileObject.close()
members.append(name)
fileObject = open('members.txt' , 'w')
fileObject.writelines(members)

#Create a program that generates multiple text files by iterating over the filenames list.
#The text Hello should be written inside each generated text file.
files = ['f1.txt','f2.txt','f3.txt']
for file in files :
    fileObject  = open(file , 'w')
    fileObject.write(f"am {file}")
    fObject.close()
#Please download the three text files a.txt, b.txt, and c.txt from the resources.
# Then, create a program that reads each text file and
# prints out the content of each in the command line.
# The expected output would be like the following:


for file in files :
    fileObject = open(file , 'r')
    read = fileObject.read()
    print(read)