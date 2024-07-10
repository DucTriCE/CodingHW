def selection_sort(input):
    lst = input.copy()
    for i in range(len(lst)-1):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j]<lst[min_idx]:
                min_idx = j
        if i!=j:
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst 

def insertion_sort(input):
    lst = input.copy()
    for i in range(len(lst)):
        while i>0 and lst[i-1] >= lst[i]:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i-=1
    return lst 

def bubble_sort(input):
    lst = input.copy()
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i]>lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst 

def quick_sort(input):
    lst = input.copy()
    left = 0
    right = len(lst)-1

    def partition(input, left, right):
        pivot = input[(left+right)//2]

    while left <= right:
        pivot = (left+right)//2

    return lst 

if __name__ == '__main__':
    sorting_algo = ['selection_sort', 'insertion_sort', 'bubble_sort', 'quick_sort']
    input = [1, 6, 2, 9, 14, 10, 3, 7, 4, 8, 5, 11, 12, 13]
    for algo in sorting_algo:
        print(globals()[algo](input))