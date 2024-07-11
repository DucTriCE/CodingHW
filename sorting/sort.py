def selection_sort(lst):
    for i in range(len(lst)-1):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j]<lst[min_idx]:
                min_idx = j
        if i!=j:
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst 

def insertion_sort(lst):
    for i in range(len(lst)):
        while i>0 and lst[i-1] >= lst[i]:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i-=1
    return lst 

def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i]>lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst 

def quick_sort(lst):
    def partition(lst, left, right):
        pivot = lst[(left+right)//2]
        i = left
        j = right
        while True:
            while lst[i]<pivot:
                i+=1
            while lst[j]>pivot:
                j-=1
            if i>=j:
                return j
            
            lst[i], lst[j] = lst[j], lst[i]

    def qs(lst, left, right):
        if left < right:
            pivot = partition(lst, left, right)
            qs(lst, left, pivot-1)
            qs(lst, pivot+1, right)
    
    qs(lst, 0, len(lst)-1)
        
    return lst 

def merge_sort(lst):
    def merge(lst, left, mid, right):
        sublstOne = mid - left + 1
        sublstTwo = right - mid

        # Create temp lsts
        leftlst = [0] * sublstOne
        rightlst = [0] * sublstTwo

        # Copy data to temp lsts leftlst[] and rightlst[]
        for i in range(sublstOne):
            leftlst[i] = lst[left + i]
        for j in range(sublstTwo):
            rightlst[j] = lst[mid + 1 + j]

        indexOfSublstOne = 0  # Initial index of first sub-lst
        indexOfSublstTwo = 0  # Initial index of second sub-lst
        indexOfMergedlst = left  # Initial index of merged lst

        # Merge the temp lsts back into lst[left..right]
        while indexOfSublstOne < sublstOne and indexOfSublstTwo < sublstTwo:
            if leftlst[indexOfSublstOne] <= rightlst[indexOfSublstTwo]:
                lst[indexOfMergedlst] = leftlst[indexOfSublstOne]
                indexOfSublstOne += 1
            else:
                lst[indexOfMergedlst] = rightlst[indexOfSublstTwo]
                indexOfSublstTwo += 1
            indexOfMergedlst += 1

        # Copy the remaining elements of left[], if any
        while indexOfSublstOne < sublstOne:
            lst[indexOfMergedlst] = leftlst[indexOfSublstOne]
            indexOfSublstOne += 1
            indexOfMergedlst += 1

        # Copy the remaining elements of right[], if any
        while indexOfSublstTwo < sublstTwo:
            lst[indexOfMergedlst] = rightlst[indexOfSublstTwo]
            indexOfSublstTwo += 1
            indexOfMergedlst += 1

    def ms(lst, left, right):
        if left >= right:
            return
        mid = (left+right)//2
        ms(lst, left, mid)
        ms(lst, mid+1, right)
        merge(lst, left, mid, right)

    ms(lst, 0, len(lst)-1)

    return lst

if __name__ == '__main__':
    sorting_algo = ['selection_sort', 'insertion_sort', 'bubble_sort', 'quick_sort', 'merge_sort']
    input = [1, 6, 2, 9, 14, 10, 3, 7, 4, 8, 5, 11, 12, 13]
    for algo in sorting_algo:
        print(globals()[algo](input.copy()))