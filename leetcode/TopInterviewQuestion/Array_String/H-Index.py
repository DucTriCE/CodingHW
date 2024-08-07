with open('../input.txt','r') as f:
    lines = f.readlines()
citations = list(map(int, lines[0].split(',')))

citations.sort(reverse=True)

i=0
for i in range(len(citations)):
    if citations[i]<i+1:
        print(i)
        exit()
print(i+1)