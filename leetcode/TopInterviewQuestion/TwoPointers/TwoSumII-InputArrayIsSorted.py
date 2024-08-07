with open('../input.txt', 'r') as f:
    lines = f.readlines()
numbers = list(map(int, lines[0].split(',')))
target = int(lines[1])

# Two for loops O(n^2) --> Not optimized
'''
for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(i+1, j+1)
            exit()
'''
i = 0
j = len(numbers)-1
while i<j:
    if numbers[i] + numbers[j] == target:
        print([i+1, j+1])
        exit()
    elif numbers[i] + numbers[j] > target:
        j-=1
    else:
        i+=1
