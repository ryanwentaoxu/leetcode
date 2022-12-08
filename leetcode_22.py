class Solution:
    def helper(self, left, right, s):
        if left == 0 and right == 0:
            return [s]
        if left == 0:
            return self.helper(0, right - 1, s+")")
        ans1 = self.helper(left - 1, right, s+"(")
        ans2 = []
        if left < right:
            ans2 = self.helper(left, right-1, s+")")
        return ans1 + ans2

    def generateParenthesis(self, n: int) -> List[str]:
        return self.helper(n, n, "")
