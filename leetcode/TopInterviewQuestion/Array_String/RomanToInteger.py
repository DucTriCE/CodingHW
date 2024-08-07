with open('../input.txt','r') as f:
    lines = f.readlines()
s = lines[0]

value = 0
Roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

for i in range(len(s)):
    if i!=len(s)-1 and Roman[s[i]]<Roman[s[i+1]]:
        value -= Roman[s[i]]
    else:
        value += Roman[s[i]]

print(value)