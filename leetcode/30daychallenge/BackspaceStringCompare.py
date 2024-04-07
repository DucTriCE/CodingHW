def compare(s):
    lst = []
    for ch in s:
        if ch!='#':
            lst.append(ch)
        else:
            if(len(s)!=0):
                lst.pop()
    return ''.join(lst)

if __name__ == '__main__':
    # Add your code here
    s, t = map(str, input().split())
    print(compare(s)==compare(t))
