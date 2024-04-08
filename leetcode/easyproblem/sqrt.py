if __name__ == '__main__':
    # Add your code here
    x = int(input())
    if x<=1:
        print(x)
        exit()
    i=0
    for i in range(1, x//2+1):
        if i*i>x:
            print(i-1)
            break
        elif i*i<x:
            continue
        else:
            print(i)
            break
    print(i)