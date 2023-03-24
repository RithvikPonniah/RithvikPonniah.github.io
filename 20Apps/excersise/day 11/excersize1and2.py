while True:
    try :
        totalValue = int(input("Enter to total value : "))
        Value = int(input("Enter the value"))

        Percentage = (Value/totalValue)*100
        print(f"Your percentage is {Percentage}%")
    except (ValueError) :
        print("Please enter a valid number")
    except (ZeroDivisionError) :
        print("The total Value cannot be 0")
# ValueError, ZeroDivisionError