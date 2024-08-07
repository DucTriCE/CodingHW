with open('../input.txt','r') as f:
    lines = f.readlines()
num = int(lines[0])

# Using list way
'''
roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
i = 0
ans = ''
while num>0:
    while num>=val[i]:
        num -= val[i]
        ans += roman[i]
    i+=1
'''

symbols = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}


roman = ""

# Iterate through the symbols and values
for symbol, value in symbols.items():
    while num >= value:
        roman += symbol
        num -= value

print(roman)
