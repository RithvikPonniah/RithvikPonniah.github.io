input("what is your name : ")
age = input("how old are you? : ")

gender = input("Are you male or female? : ")
boys = ["Cars", "Harry Potter", "Sing"]
girls = ["Repunzel", "Frozen", "Barbie world"]
TeenBoys = ["transformers", "avengers", "Captain america", "The Dark Knight", "Iron man"]
TeenGirls = ["Tall Girl", "Mean Girl", "Instant Family"]
Adult = ["The Graduate", "Arjun Reddy", "Shawshank Redemption", "The forrest Grump"]
ageINT = int(age)
if (ageINT < 13):
    if (gender == 'male') :
        print("Here are some movies I think you will like : " , boys)
    if (gender == 'female') :
        print("Here are some movies I think you will like : " , girls)
elif (13 <= ageINT <=18) :
    if (gender == "male") :
        print("Here are some movies I think you will like" , TeenBoys)
    if (gender == "female") :
        print("Here are some movies I think you will like" , TeenGirls)
elif  (ageINT > 18) :
    print("Here are some movies I think you might like : " , Adult)

