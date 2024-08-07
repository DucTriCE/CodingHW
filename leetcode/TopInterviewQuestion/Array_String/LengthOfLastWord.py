with open('../input.txt','r') as f:
    lines = f.readlines()
s = lines[0]

# Use python function
'''
my_list = s.split()
print(len(my_list[-1]))
'''

length = 0
flag = False
for i in range(len(s)-1, -1, -1):
    if s[i]==' ':
        if not flag:
            continue
        else:
            break
    else:
        flag = True
        length+=1
print(length)

