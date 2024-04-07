if __name__ == '__main__':
    # Add your code here
    n = int(input())
    for i in range(100000):
        if n==1:
            print("TRUE")
            exit()
        s=0
        m=n
        while m:
            s+=(m%10)*(m%10)
            m//=10
        n=s
    print("FALSE")