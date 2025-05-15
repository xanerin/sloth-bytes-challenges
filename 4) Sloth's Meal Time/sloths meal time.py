import re

def timeToEat(timeString):
    timeRemaing = []
    split = re.split(r"[:\s]", timeString)

    if split[2] == "p.m." and split[0] != "12":
        split[0] = int(split[0]) + 12
    if split[2] == "a.m." and split[0] == "12":
        split[0] = "00"

    split.append(float(str(str(split[0]) + "." + str(split[1]))))

    if split[3] < 7.0:
        if int(split[1]) == 0:
            timeRemaing = [7 - int(split[0]), 0]
        else:
            timeRemaing = [6 - int(split[0]), 60 - int(split[1])]
    if split[3] == 7.0:
        timeRemaing = [0, 0]

    if split[3] < 12 and split[3] > 7.0:
        if int(split[1]) == 0:
            timeRemaing = [12 - int(split[0]), 0]
        else:
            timeRemaing = [11 - int(split[0]), 60 - int(split[1])]
    if split[3] == 12:
        timeRemaing = [0, 0]

    if split[3] < 19 and split[3] > 12:
        if int(split[1]) == 0:
            timeRemaing = [19 - int(split[0]), 0]
        else:
            timeRemaing = [18 - int(split[0]), 60 - int(split[1])]
    if split[3] == 19:
        timeRemaing = [0, 0]

    if split[3] < 24 and split[3] > 19:
        if int(split[1]) == 0:
            timeRemaing = [31 - int(split[0]), 0]
        else:
            timeRemaing = [30 - int(split[0]), 60 - int(split[1])]
    if split[3] == 24:
        timeRemaing = [7, 0]

    return timeRemaing

"""
meow

weekly challenge - slothy bytesy - Time to Eat

assumptions:
- the time given is valid and in the format "hour:minute a.m./p.m."

the challenge:
Sloth is a very habitual person. He eats breakfast at 7:00 a.m. each morning, lunch at 12:00 p.m. and dinner at 7:00 p.m. in the evening.

Create a function that takes in the current time as a string and determines the duration of time before Sloth's next meal.

Represent this as an array with the first and second elements representing hours and minutes, respectively.

Examples
timeToEat("2:00 p.m.")
#5 hours until the next meal, dinner
output = [5, 0]

timeToEat("5:50 a.m.")
# 1 hour and 10 minutes until the next meal, breakfast
output = [1, 10]

"""