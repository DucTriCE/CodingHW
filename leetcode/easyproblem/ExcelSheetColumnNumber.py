if __name__ == '__main__':
    columnTitle = input()
    ans, pos = 0, 0
    for letter in reversed(columnTitle):
        digit = ord(letter)-64
        ans += digit * 26**pos
        pos += 1
    print(ans) 