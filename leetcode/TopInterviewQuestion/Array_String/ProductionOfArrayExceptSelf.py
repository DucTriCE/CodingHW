with open('../input.txt','r') as f:
    lines = f.readlines()
nums = list(map(int, lines[0].split(',')))

# Verbose code
'''
prefix_product = [0]*len(nums)
suffix_product = [0]*len(nums)

for i in range(len(nums)):
    if i==0:
        prefix_product[i]=nums[i]
    else:
        prefix_product[i]=nums[i]*prefix_product[i-1]

for i in range(len(nums)-1, -1, -1):
    if i==len(nums)-1:
        suffix_product[i]=nums[i]
    else:
        suffix_product[i]=nums[i]*suffix_product[i+1]

ans = [0]*len(nums)
for i in range(len(ans)):
    if i==0:
        ans[i]=suffix_product[1]
    elif i==len(ans)-1:
        ans[i]=prefix_product[len(ans)-2]
    else:
        ans[i]=prefix_product[i-1]*suffix_product[i+1]
'''

n = len(nums)
prefix = [1]*n
postfix = [1]*n
ans = [1]*n
prefix[0] = 1
postfix[n-1] = 1

for i in range(1, n):
    prefix[i] = prefix[i-1] * nums[i-1]

for i in range(n - 2, -1, -1):
    postfix[i] = postfix[i + 1] * nums[i + 1]
    ans[i] = postfix[i]*prefix[i]
ans[n-1] = prefix[n-1]

print(ans)

