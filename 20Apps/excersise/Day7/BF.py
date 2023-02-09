temperatures = [10, 12, 14]

file = open("file.txt", 'w')
temperatures = [str(item) for item in temperatures]
file.writelines(temperatures)
