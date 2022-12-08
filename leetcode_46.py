class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        ans = []
        for i in range(len(nums)):
            for n in self.permute(nums[:i] + nums[i+1:]):
                ans.append([nums[i]] + n)
        return ans
