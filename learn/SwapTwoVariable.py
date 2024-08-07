a = 5
b = 6
print(f"Before: a={a}, b={b}")

# First method: using python variable exchange
a, b = b, a

# Second method: using temporary variable
c = a
a = b
b = c

# Third method: using add and subtract
a = a + b
b = a - b
a = a - b

#Fourth method: using xor
a = a ^ b
b = a ^ b 
a = a ^ b

print(f"After: a={a}, b={b}")