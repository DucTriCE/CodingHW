with open('../input.txt','r') as f:
    lines = f.readlines()

s = lines[0]

my_list = s.split()
reverse_string = ' '.join(my_list[::-1])
print(reverse_string)