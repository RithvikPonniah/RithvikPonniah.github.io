import json

with open("Questions.json" , 'r') as fObject :
    fileContent = fObject.read()
questions = json.loads(fileContent)
#print(listOfDs[0]['Options'])
userAnswers = []

for question in questions :
    print(question['questionText'])
    for index , option in enumerate(question['Options']) :
        print(f"{index+1}.{option}")
    ans = int(input('Please pick the correct option number : '))
    userAnswers.append(ans)
    print()

correctAnswer = 0
for y,answer in enumerate(userAnswers) :
    if answer == questions[y]['correctAnswer']:
        correctAnswer = correctAnswer + 1
        ansMessage = "Correct Answer"
    else :
        ansMessage = "Wrong Answer"
    #print(f"The correct answer to question number {y + 1} is option {questions[y]['correctAnswer']} you picked option {answer}")
    print(f'{y+1}.{ansMessage}. The correct answer is {questions[y]["correctAnswer"]}. You picked {answer}')
#print("============================================")
print(f"You got {correctAnswer} correct answers out of {len(questions)} questions")
#print("============================================")



#for z, answer in enumerate(userAnswers) :
 #   print(f"The correct answer to question number {z+1} is option {questions[z]['correctAnswer']} you picked option {answer}")
#print("============================================")
