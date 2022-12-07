class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        ret = 0
        left = 0
        right = 0
        freq_dict = {}
        while (left <= right and right < len(s) and left < len(s)):
            if freq_dict.get(s[right], 0) == 0:
                ans += 1
                if ans > ret:
                    ret = ans
                freq_dict[s[right]] = 1
                right += 1
            else:
                ans -= 1
                freq_dict[s[left]] -= 1
                left += 1

        return ret
