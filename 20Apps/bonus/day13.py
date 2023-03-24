def convert(Feet,Inches):
    Feet2Inch = Feet*12
    NInches=Feet2Inch+Inches
    meters  = NInches * 0.0254
    return meters

def splitHeight(height):
    heightList = height.split()
    return heightList

Height1 = input("What is the Height : ")
Height = splitHeight(Height1)
print(convert(int(Height[0]),int(Height[1])))