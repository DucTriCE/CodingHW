class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        tmp = ''

        for i in s:
            if i>='a' and i<='z' or i>='0' and i<='9':
                tmp+=i
        if tmp==tmp[::-1]:
            return True
        else:
            return False