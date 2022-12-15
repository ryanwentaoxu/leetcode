class Solution:
    dic = {}
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if self.dic.get((text1, text2), -1) != -1:
            return self.dic[(text1, text2)]
        if len(text1) == 0:
            self.dic[(text1, text2)] = 0
            return 0
        if len(text2) == 0:
            self.dic[(text1, text2)] = 0
            return 0
        if text1[0] != text2[0]:
            ans = max(self.longestCommonSubsequence(text1[1:], text2), self.longestCommonSubsequence(text1, text2[1:]))
            self.dic[(text1, text2)] = ans
            return ans
        else:
            ans = 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
            self.dic[(text1, text2)] = ans
            return ans
