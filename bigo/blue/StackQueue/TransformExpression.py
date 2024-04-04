if __name__ == '__main__':
    t = int(input())
    while t!=0:
        s = input()
        operators = []
        for i in s:
            if i==')':
                print(operators.pop(),end='')
            elif i>='a' and i<='z':
                print(i, end='')
            elif i=='+' or i=='-' or i=='*' or i=='/' or i=='^':
                operators.append(i)
        print()
        t-=1

