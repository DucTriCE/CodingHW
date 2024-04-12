s = ''
columnNumber = int(input())
while columnNumber>26:
    tmp = columnNumber%26
    if (tmp==0):
        tmp+=26
        columnNumber=columnNumber//26-1
    else:
        columnNumber=columnNumber//26
    s = chr(tmp+64) + s
s = chr(columnNumber+64) + s
print(s)