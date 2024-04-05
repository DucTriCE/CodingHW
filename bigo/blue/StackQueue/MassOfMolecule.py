if __name__ == '__main__':
    dict = {
        'C': 12,
        'H': 1,
        'O': 16
    }
    s = input()
    st = []
    mass = 0
    for ch in s:
        if ch=='C' or ch=='H' or ch=='O':
            st.append(int(dict[ch]))
        elif ch == '(':
            st.append(-1)
        elif ch>='1' and ch<='9':
            st.append(st.pop()*int(ch))
        else:
            sum=0
            while st[-1]!=-1:
                sum+=st.pop()
            st.pop()
            st.append(sum)
    while len(st)!=0:
        mass += st.pop()
    print(mass)
    