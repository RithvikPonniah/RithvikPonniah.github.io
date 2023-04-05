import time
print("MAC book time")
print(time.strftime('%a %b %d %I:%M %p'))

print("windows Desktop time")
print(time.strftime("%I:%M %p"))
print(time.strftime("%d/%m/%Y"))

print("Iphone time")
print(time.strftime("%A, %d %B"))
print(time.strftime('%I:%M'))

print('Samsung Time')
print(time.strftime("%I:%M"))
print(time.strftime("%a, %B %d"))

print("Gshock time")
print(time.strftime("%a %m- %d").upper())

print("Asus lock screen time")
print(time.strftime("%I:%M"))
print(time.strftime("%A, %B %d"))

print(time.CLOCK_MONOTONIC)