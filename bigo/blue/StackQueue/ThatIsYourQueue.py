from collections import deque

if __name__ == '__main__':
    case = 1
    while True:
        p, c = map(int, input().split())
        q = deque()

        if p==0 and c==0:
            break
        for i in range(min(p, c)):
            q.append(i+1)
        print(f"Case {case}: ")
        case+=1

        for i in range(c):
            s=input()
            if s=='N':
                print(q[0])
                q.append(q.popleft())
            else:
                lst=s.split()
                current_length = len(q)
                q.append(int(lst[1]))
                for i in range(current_length):
                    tmp = q.popleft()
                    if tmp!=int(lst[1]):
                        q.append(tmp)

            
