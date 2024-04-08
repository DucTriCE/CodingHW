if __name__ == '__main__':
    # Add your code here
    n = int(input())
    if n<=1:
        print(max(0, n))
    else:
        lst = [1, 1]
        for i in range(2, n+1):
            lst.append(lst[i-1]+lst[i-2])
        print(lst[n])

