class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0
        stack = []
        score = []
        for i in range(len(s)):
            if i == 0:
                if s[i] == "(":
                    stack.append(s[i])
                    score.append(0)
            else:
                if s[i] == ")" and len(stack) >= 1 and stack[-1] == "(":
                    tmp = score.pop()
                    stack.pop()
                    tmp += 2
                    if len(score) == 0:
                        score.append(tmp)
                    elif score[-1] == -1:
                        score.append(tmp)
                    else:
                        score[-1] += tmp
                elif s[i] == "(":
                    stack.append("(")
                    score.append(0)
                elif s[i] == ")":
                    score.append(-1)
        if score == []:
            return 0
        ans = max(score)
        if ans < 0:
            return 0
        else:
            return ans
