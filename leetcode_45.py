class Solution:
    def jump(self, nums: List[int]) -> int:
        sign = [-1 for i in nums]
        sign[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            for j in range(1, nums[i]+1):
                if i + j >= len(nums) - 1:
                    sign[i] = 1
                else:
                    if sign[i+j] >= 0:
                        if sign[i+j] + 1 < sign[i] and sign[i] != -1:
                            sign[i] = sign[i+j] + 1
                        elif sign[i] == -1:
                            sign[i] = sign[i+j] + 1
        return sign[0]
