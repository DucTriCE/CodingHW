

if __name__ == '__main__':

    n, k = map(int, input().split())
    totalPasswdLength = [0]*101
    for i in range(n):
        s = input()
        totalPasswdLength[len(s)]+=1
    passwd = input()

    worstCase=0
    for i in range(len(passwd)):
        worstCase+=totalPasswdLength[i+1]
    
    worstCase-=1
    bestCase = worstCase-totalPasswdLength[len(passwd)]+1

    worstCase+=(worstCase//k)*5
    bestCase+=(bestCase//k)*5
    
    print(bestCase+1, worstCase+1)


