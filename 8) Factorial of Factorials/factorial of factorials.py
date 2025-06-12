import math

def fact_of_fact(factorial):
    total = 1
    for i in range(1, factorial + 1):
        total *= math.factorial(i)
    return total

"""
meow?

weekly challenge - slothy bytesy - Factorial of Factorials

the challenge:
Factorial of Factorials
Create a function that takes an integer n and returns the factorial of factorials. See below examples for a better understanding:

Examples:
fact_of_fact(4)
output = 288
// 4! * 3! * 2! * 1! = 288

fact_of_fact(5)
output = 34560

fact_of_fact(6)
output = 24883200

"""