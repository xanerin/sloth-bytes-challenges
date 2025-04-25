def split_into_buckets(phrase, n):
    splitString = phrase.split(" ")
    bucket = []
    currentAdd = ""
    firstWord = True
    nTotal = 0

    for i in splitString:
        print(i, nTotal, 1 + nTotal + len(i) >= n)
        if 1 + nTotal + len(i) > n:
            nTotal = 0
            bucket.append(currentAdd)
            firstWord = True
            currentAdd = ""

        print(len(i) < n and nTotal + len(i) < n)
        if len(i) < n and nTotal + len(i) < n:
            if firstWord == True:
                currentAdd += i
                firstWord = False
                nTotal = len(currentAdd)
            elif firstWord == False:
                currentAdd += " " + i
                nTotal = len(currentAdd)
        print(currentAdd)

    if len(currentAdd) <= n and currentAdd != "":
        bucket.append(currentAdd)
    
    return bucket

"""
meow

weekly challenge - sloth bytes - Word Buckets
assumptions:
- phrases start with a letter
- there is no punctuation
- there does not exist more than one space per word

the challenge:
Write a function that divides a phrase into word buckets, with each bucket containing n or fewer characters. Only include full words inside each bucket.

examples:
split_into_buckets("she sells sea shells by the sea", 10)
output = ["she sells", "sea shells", "by the sea"]

split_into_buckets("the mouse jumped over the cheese", 7)
output = ["the", "mouse", "jumped", "over", "the", "cheese"]

split_into_buckets("fairy dust coated the air", 20)
output = ["fairy dust coated", "the air"]

split_into_buckets("a b c d e", 2)
output = ["a", "b", "c", "d", "e"]

notes:
- Spaces count as one character.
- Trim beginning and end spaces for each word bucket (see final example).
- If buckets are too small to hold a single word, return an empty list: []
- The final goal isn't to return just the words with a length equal (or lower) to the given n, but to return the entire given phrase bucketized (if possible).
"""