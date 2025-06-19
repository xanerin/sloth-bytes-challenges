def birthdayCakeCandles(candles):
    if candles == []:
        return 0
    
    count = 0
    maxHeight = 0

    for i in range(len(candles)):
        if candles[i] > maxHeight:
            maxHeight = candles[i]
            count = 1
        elif candles[i] == maxHeight:
            count += 1
    return count

"""
thank you gemini autocomplete for mostly reading my mind (meow)

weekly challenge - slothy bytesy - Birthday Cake Candles

the challenge:
Birthday Cake Candles
You are in charge of the cake for a child's birthday. It will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles.

Your task is to count how many candles are the tallest.

Examples:
birthdayCakeCandles([4,4,1,3])
output = 2
// The tallest candles are 4. There are 2 candles with this height, so the function should return 2.
birthdayCakeCandles([1, 1, 1, 1])
output = 4
// All candles are the same height, so all are the tallest.
birthdayCakeCandles([])
output = 0
// No candles, so nothing to blow out.
"""