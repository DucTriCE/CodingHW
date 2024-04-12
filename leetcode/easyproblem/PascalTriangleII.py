if __name__ == '__main__':
    rowIndex = int(input())
    ans = []
    i =  0
    while i!=rowIndex+1:
        lst = [1]*(i+1)
        for j in range(i+1):
            if j!=0 and j!=i:
                lst[j] = ans[i-1][j] + ans[i-1][j-1]
        i+=1
        ans.append(lst)
    print(ans[rowIndex])
    
        