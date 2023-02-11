from pathlib import Path
Path("journal").mkdir(parents=True,exist_ok=True)
date = input("Enter today's date: ")
input("How do you rate your mood today from 1 to 10: ")
thoughts = input("Let your thoughts flow: ")+'\n'
#fObject = open('journal/'+date+'.txt' , 'w')
#fObject.write(thoughts)
with open('journal/'+date+'.txt' , 'w') as fObject:
    fObject.write(thoughts)