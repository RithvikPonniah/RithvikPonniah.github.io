import glob
import csv
stateName = input("Enter your two letter state name : ")
cityName = input("Enter the city name for temprature : ")

states = glob.glob('files/*.csv')
for state in states :
    if state == 'files/'+stateName+'.csv' :
        with open(state , 'r') as fObject:
            cities = list(csv.reader(fObject))
        for city in cities[1:] :
            if city[0] == cityName:
                print(f'The weather in your city is {city[1]}')