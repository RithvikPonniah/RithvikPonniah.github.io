import glob

textFiles = glob.glob('files/*.txt')
print(textFiles)
for textFile in textFiles :
    print('************ Content of the file ' , textFile , '***************')
    with open(textFile , 'r') as fObject:
        print(fObject.read())