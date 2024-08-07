with open('../input.txt', 'r') as f:
    lines = f.readlines()

nums = list(map(int, lines[0].split()))

idx = 0
st = set()
for i in range(len(nums)):
    if nums[i] not in st:
        st.add(nums[i])
        nums[idx] = nums[i]
        idx+=1
print(nums[:idx])

