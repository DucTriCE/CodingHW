# nums1 = list(map(int, input().split()))
# nums2 = list(map(int, input().split()))
# m, n = map(int, input().split())

with open('../input.txt', 'r') as f:
    lines = f.readlines()

nums1 = list(map(int, lines[0].split()))
nums2 = list(map(int, lines[1].split()))
m, n = map(int, lines[2].split())

# Easiest way
'''
for i in range(n):
    nums1[i+n] = nums2[i]
nums1.sort()
'''

i = m-1
j = n-1
k = m+n-1

while (i>=0 and j>=0):
    if nums2[j]>nums1[i]:
        nums1[k]=nums2[j]
        j-=1
        k-=1
    else:
        nums1[k]=nums1[i]
        i-=1
        k-=1

while j>=0:
    nums1[k]=nums2[j]
    k-=1
    j-=1

print(nums1)