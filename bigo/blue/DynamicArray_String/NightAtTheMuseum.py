s = input()

minimum_rotations = 0
current_char = 'a'

for i in s:
    minimum_rotations += min(26-abs(ord(i)-ord(current_char)), abs(ord(i)-ord(current_char)))
    current_char = i

print(minimum_rotations)