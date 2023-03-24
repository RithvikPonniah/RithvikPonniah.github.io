def speed(distance, time=1):
    """Accepts two arguements that is distance and time and gives the speed"""
    speed = distance/time
    return speed
#print('the speed is ', speed(200,4))
#print('the speed is ', speed(75))
print(help(speed))
speed(8)

d = int(input())
t = int(input())

todayLearning    ="\
- any()  is a function which accepts a list and returns True or False.It returns true when any one item in the list is true and false when none of the item are true \n\
- all() is a function that returns true or false.It returns True when all the items in the list are true and returns false when not all the items are false\n\
- All strings are True except for empty ones\n\
- All numbers are true except 0\n\
- All lists, sets , tuples and dictionaries are true except for empty ones\n\
"

print(todayLearning)

#   print('the speed is ',speed(d,t))