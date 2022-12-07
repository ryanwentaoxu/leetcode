# cannot use DP in this question, though the time complexity is the same

class Solution:
    def helper(self, pointer, s):
        if s[pointer] == s[pointer+1]:
            left = pointer
            right = pointer + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(self.ans):
                    self.ans = s[left: right + 1]
                left -= 1
                right += 1
        
        if pointer >  0 and s[pointer - 1] == s[pointer + 1]:
            left = pointer - 1
            right = pointer + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(self.ans):
                    self.ans = s[left: right + 1]
                left -= 1
                right += 1

    def longestPalindrome(self, s: str) -> str:
        self.ans = s[0]
        for i in range(len(s)-1):
            self.helper(i, s)
        return self.ans
