import re

def actualMemorySize(ms):
    amount = re.findall("[0-9.]+", ms)[0]
    unit = re.findall("[a-zA-Z]+", ms)[0]
    
    if unit == "GB":
        amount = float(amount) * 1000 * 0.93
    elif unit == "MB":
        amount = float(amount) * 0.93
    
    if amount >= 1000:
        return str(round(amount / 1000, 2)) + "GB"
    else:
        return str(round(amount)) + "MB"

"""
meow

weekly challenge - slothful sin of bytes - The Actual Memory Size of Your USB Flash Drive

assumption:
- is given in correct format

the challenge:
Create a function that takes the memory size (ms) as an argument and returns the actual memory size.

Examples
actualMemorySize("32GB")
output = "29.76GB"

actualMemorySize("2GB")
output = "1.86GB"

actualMemorySize("512MB")
output = "476MB"

Notes:
The actual storage loss on a USB device is 7% of the overall memory size!

If the actual memory size was greater than 1 GB, round your result to two decimal places.

If the memory size after adjustment is smaller then 1 GB, return the result in MB.

For the purposes of this challenge, there are 1000 MB in a Gigabyte.
"""