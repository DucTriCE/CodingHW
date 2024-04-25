if __name__ == '__main__':
    nums = list(map(int, input().split()))
    st = set()
    for i in nums:
        if i not in st:
            st.add(i)
        else:
            print(False)
            exit()
    print(True) 