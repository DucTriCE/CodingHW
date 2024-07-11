

def test(lst, left, right):
    pivot = lst[(left+right)//2]

lst = [1,2,3,4,5]
pivot = test(lst, 0, 4)
print(pivot)