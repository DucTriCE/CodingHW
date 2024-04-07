if __name__ == '__main__':
    # Add your code here
    while True:
        lst = list(map(int, input().split()))
        cnt = 0
        for num in lst:
            if num+1 in lst:
                cnt+=1
        print(cnt)