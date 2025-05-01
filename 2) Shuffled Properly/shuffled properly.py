def isShuffledWell(numbers):
    previousNum = -1
    ascendingConsequent = 0
    descendingConsequent = 0

    for i, n in enumerate(numbers):
        if previousNum == -1:
            previousNum = n
            continue

        if n == previousNum + 1:
            previousNum = n
            if ascendingConsequent == 1:
                return False
            elif ascendingConsequent == 0:
                ascendingConsequent = 1

        elif n == previousNum - 1:
            previousNum = n
            if descendingConsequent == 1:
                return False
            elif descendingConsequent == 0:
                descendingConsequent = 1

        else:
            previousNum = n
            ascendingConsequent = 0
            descendingConsequent = 0
    

    return True

"""
meow

weekly challenge - sloth bytes - Shuffled Properly

Given an array of 10 numbers, return whether or not the array is shuffled enough.

In this case, if 3 or more numbers appear consecutively (ascending or descending), return false.

examples:
isShuffledWell([1, 2, 3, 5, 8, 6, 9, 10, 7, 4])
output = false
# 1, 2, 3 appear consecutively

isShuffledWell([3, 5, 1, 9, 8, 7, 6, 4, 2, 10])
output = false
# 9, 8, 7, 6 appear consecutively

isShuffledWell([1, 5, 3, 8, 10, 2, 7, 6, 4, 9])
output = true
# No consecutive numbers appear

isShuffledWell([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
output = true
# No consecutive numbers appear

Notes:
- Only steps of 1 in either direction count as consecutive (i.e. a sequence of odd and even numbers would count as being properly shuffled (see example #4)).
- You will get numbers from 1-10.
"""