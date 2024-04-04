n = int(input())

l = list(map(int, input().split()))

if n==1:
    if l[0]!=1:
        print("NO")
    else:
        print("YES")
else:
    count=0
    for i in l:
        if i==0:
            count+=1
            if count>1:
                print("NO")
                exit()
    if count!=0:
        print("YES")
    else:
        print("NO")