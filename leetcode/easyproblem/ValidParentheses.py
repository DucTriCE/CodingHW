if __name__ == '__main__':
    # Add your code here
    s = input()
    st = []
    for i in s:
        if i == '(' or i=='[' or i=='{':
            st.append(i)
        elif len(st)!=0:
            if i==')' and st[-1]=='(':
                st.pop()
            elif i=='}' and st[-1]=='{':
                st.pop()
            elif i ==']' and st[-1]=='[':
                st.pop()
            else:
                break
        else:
            print(False)
    if len(st)!=0:
        print(False)
    else:
        print(True)
