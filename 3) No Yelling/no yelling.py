def noYelling(phrase):
    lastIndex = -1000

    for i, n in enumerate(phrase):
        letter = phrase[len(phrase) - (i + 1)]

        if letter == "?" or letter == "!":
            lastIndex = len(phrase) - (i + 1)
        else:
            if lastIndex == -1000:
                return phrase
            else:
                return phrase[0:lastIndex+1]
        
    if phrase[0] == "!":
        return "!"
    elif phrase[0] == "?":
        return "?"
    else:
        return phrase

print(noYelling("!!!"))

"""
meow

weekly challenge - sloth bytes - No Yelling
assumptions:
- the input is a string

the challenge:
Create a function that transforms sentences ending with multiple question marks ? or exclamation marks ! into a sentence only ending with one without changing punctuation in the middle of the sentences.

examples:
noYelling("What went wrong?????????")
output = "What went wrong?"

noYelling("Oh my goodness!!!")
output = "Oh my goodness!"

noYelling("I just!!! can!!! not!!! believe!!! it!!!")
output = "I just!!! can!!! not!!! believe!!! it!"
# Only change repeating punctuation at the end of the sentence.

noYelling("Oh my goodness!")
output = "Oh my goodness!"
# Do not change sentences where there exists only one or zero exclamation marks/question marks.
"""