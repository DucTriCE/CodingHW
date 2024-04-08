if __name__ == '__main__':
    # Add your code here
    digits = list(map(int, input().split()))
    # s = 0
    # for i in range(len(digits)):
    #     s+=digits[i]*pow(10, len(digits)-i-1)
    # s+=1
    # ans = []
    # while s!=0:
    #     ans.append(s%10)
    #     s//=10
    # print(ans[::-1])
    tmp = ''.join(map(str, digits))
    print(list(map(int, list(str(int(tmp)+1)))))