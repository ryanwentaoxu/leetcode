class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        visited = set()
        ans = []
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            else:
                visited.add(nums[i])
                for n in self.permuteUnique(nums[:i] + nums[i+1:]):
                    ans.append([nums[i]] + n)
        return ans
