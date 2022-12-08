class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        sign = 1
        if x / -1 > 0:
            x = int(x / -1)
            sign = -1
        ans = str(x)
        ans = sign * int(ans[::-1])
        if ans > pow(2, 31) - 1 or ans < -1 * pow(2, 31):
            return 0
        return ans
        
