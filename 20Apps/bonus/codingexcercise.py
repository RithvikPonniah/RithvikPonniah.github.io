#filenames = ['document', 'report', 'presentation']
#for index,item in enumerate(filenames):
#    print(f"{index}-{item}.txt")

ips = ['100.122.133.105', '100.122.133.111']
ip = input("Enter the index of the IP you want: ")
match ip :
    case "1":
        print("you chose 100.122.133.111")
    case "0":
        print("you chose 100.122.133.105")