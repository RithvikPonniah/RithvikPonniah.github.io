import json

with open("Questions.json" , 'r') as fObject :
    fileContent = fObject.read()
questions = json.loads(fileContent)
#print(listOfDs[0]['Options'])
userAnswers = []

for question in questions :
    x=0
    print(question['questionText'])
    for option in question['Options'] :
        x= x+1
        print(f"{x}.{option}")
    ans = int(input('Please pick the correct option number : '))
    userAnswers.append(ans)
    print()

y=0
correctAnswer = 0
for answer in userAnswers :
    if answer == questions[y]['correctAnswer']:
        correctAnswer = correctAnswer + 1
    y=y+1
print("============================================")
print(f"You got {correctAnswer} correct answers out of {len(questions)} questions")
print("============================================")

z=0
for answer in userAnswers :
    print(f"The correct answer to question number {z+1} is option {questions[z]['correctAnswer']} you picked option {answer}")
    z = z + 1
print("============================================")
