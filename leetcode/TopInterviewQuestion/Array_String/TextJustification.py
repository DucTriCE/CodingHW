with open('../input.txt','r') as f:
    lines = f.readlines()

words = [word.strip().strip('"') for word in lines[0].split(',')]
maxWidth = int(lines[1])

print(words)