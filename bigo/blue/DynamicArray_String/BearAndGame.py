
if __name__ == '__main__':

    # n = int(input())
    # lst = list(map(int, input().split()))

    # current_minute = lst[0]

    # if current_minute > 15:
    #     print("15")
    # else:
    #     lst[1:]
    #     for i in lst:
    #         if i > current_minute+15:
    #             print(current_minute+15)
    #             exit()
    #         else:
    #             current_minute=i

    #     if current_minute<75:
    #         print(current_minute+15)
    #     else:
    #         print("90")

    n = int(input())
    lst = list(map(int, input().split()))

    current_minute=0
    for i in range(len(lst)):
        if lst[i]>current_minute+15:
            print(current_minute+15)
            exit()
        else:
            current_minute = lst[i]
    
    if current_minute<75:
        print(current_minute+15)
    else:
        print("90")

