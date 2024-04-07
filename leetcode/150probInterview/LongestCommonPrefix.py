class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        mi = len(min(strs, key=len))

        for i in range(mi):
            s = strs[0][i]
            for j in range(len(strs)):
                if s==strs[j][i] and j==len(strs)-1:
                    result+=s
                elif s!=strs[j][i]:
                    return result
                else:
                    continue
        return result