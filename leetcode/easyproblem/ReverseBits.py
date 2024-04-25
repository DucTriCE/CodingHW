if __name__ == '__main__':
    n = int(input())
    s = bin(n)[2:]
    while len(s)<32:
        s = '0'+ s
    print(s[::-1])
    print(int(s[::-1], 2))