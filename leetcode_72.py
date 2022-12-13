class Solution:
    dic = {}
    def minDistance(self, word1: str, word2: str) -> int:
        if self.dic.get((word1, word2), -1) != -1:
            return self.dic[(word1, word2)]
        if len(word1) == 0:
            self.dic[(word1, word2)] = len(word2)
            return len(word2)
        if len(word2) == 0:
            self.dic[(word1, word2)] = len(word1)
            return len(word1)
        
        if word1[0] == word2[0]:
            ans = self.minDistance(word1[1:], word2[1:])
            self.dic[(word1, word2)] = ans
            return ans
        else:
            a = self.minDistance(word1[1:], word2)
            b = self.minDistance(word1[1:], word2[1:])
            c = self.minDistance(word1, word2[1:])
            ans = 1 + min(a, b, c)
            self.dic[(word1, word2)] = ans
            return ans
