content = ["Sohan and lakshya are comming to hayden tomorrow",
           "aadithya might also come to hayden tomorrow",
           "I will go to hayden tomorrrow"]
files = ["friends.txt","family.txt","Monkey.txt"]
for fileName , fileContent in zip(files , content):
    fObject = open(f'files/{fileName}' , 'w')
    fObject.writelines(fileContent)