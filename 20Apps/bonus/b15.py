import json

with open('Questions.json' , 'r') as fObject :
    fileContent=fObject.read()
quesionAnswers = json.loads(fileContent)
Answers = []
x = 0
y = 0
correctAnswer = []
for question in quesionAnswers :
    print(question["questionText"])
    for index,option in enumerate(question["Options"]) :
        print(f"{index + 1}.{option}")
    userAnswer = int(input("State Your answer : "))
    question["userInput"] = userAnswer
    if userAnswer == question["correctAnswer"] :
        Answers.append([True,userAnswer,question["correctAnswer"]])
    else :
        Answers.append([False,userAnswer,question["correctAnswer"]])
    y=y+1

for index , question in enumerate(quesionAnswers) :
    if question["userInput"] == question["correctAnswer"] :
        x=x+1
        print(f"Q{index + 1} . Your answer is correct. The correct answer was was {question['correctAnswer']} and you answered {question['userInput']}")
    else :
        print(f"Q{index + 1} . Your answer is incorrect. The correct answer was was {question['correctAnswer']} and you answered {question['userInput']}")

print(f"You have got {x}/{y} questions right.")