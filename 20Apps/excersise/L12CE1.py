def litreToMeterCube(litre):
    mCube = litre/1000
    return mCube
litre = int(input('Enter number of litres : '))
print(f'{litreToMeterCube(litre)} meter cube')