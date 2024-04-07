class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tmp = s.split()
        return len(tmp[len(tmp)-1])