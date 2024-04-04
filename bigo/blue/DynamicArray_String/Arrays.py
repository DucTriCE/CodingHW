
if __name__ == '__main__':
    na, nb = map(int, input().split())
    k, m = map(int, input().split())

    lstA = list(map(int , input().split()))
    lstB = list(map(int , input().split()))

    if lstA[k-1] < lstB[len(lstB)-m]:
        print("YES")
    else:
        print("NO")
