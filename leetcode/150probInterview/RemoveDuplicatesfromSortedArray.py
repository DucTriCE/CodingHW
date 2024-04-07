lst = [1,2,3,3,3,4,5,5,6]

st = set()

i=0
for j in range(1, len(lst)):
    if lst[j]==lst[i]:
        continue
    else:
        lst[i+1]=lst[j]
        i+=1
print(i)
print(lst)