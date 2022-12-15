class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(s) + 1):
            dp[i][0] = False
        for j in range(1, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j-1]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if p[j - 1] == "?":
                        dp[i][j] = dp[i - 1][j - 1]
                    elif p[j - 1] == "*":
                        a = dp[i - 1][j - 1]
                        b = dp[i][j - 1]
                        c = dp[i - 1][j]
                        if a or b or c:
                            dp[i][j] = True
                        else:
                            dp[i][j] = False
                    else:
                        dp[i][j] = False
        return dp[len(s)][len(p)]
