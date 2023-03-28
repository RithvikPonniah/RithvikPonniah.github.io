FreezingPoint = 0
BoilingPoint = 100
def StateOfMatter(temprature):
    if temprature<=FreezingPoint:
        return 'Solid'
    elif temprature>=BoilingPoint :
        return 'gas'
    else:
        return 'liquid'
