import queue

if __name__ == '__main__':
    while True:
        n = int(input())
        qu = queue.Queue()
        if n==0:
            break

        print("Discarded cards:", end='')
        for i in range(1, n+1):
            qu.put(i)
        i=0
        while qu.qsize()!=1:
            if i%2==0:
                if qu.qsize()!=2:
                    print("", qu.get(), end=',')
                else:
                    print("", qu.get(), end='')
                i+=1
            else:
                qu.put(qu.get())
                i+=1
        print("\nRemaining card:", qu.get())
