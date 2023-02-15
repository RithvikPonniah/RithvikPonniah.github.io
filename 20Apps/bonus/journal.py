# input
#   seek date as user input
#   seek mood of the user in scal of 1 to 10 &
#   request for his thoughts
#   Oput put#
#   Create a file with name of the date with the content as his thoughts




date = input("Please enter today's date : ")
mood = input("Rate your mood on a scale of 10 with 10 being the best : ")
thoughts = input("Let your thoughts flow : ")

with open('journal/'+ date + '.txt' , 'w') as fObject :
    fObject.write(thoughts)