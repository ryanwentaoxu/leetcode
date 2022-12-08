class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        recur_sign = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                recur_sign = 1
                break
        if recur_sign == 0:
            nums.sort()
        else:
            found = 0
            left = 0
            right = 0
            for i in range(len(nums)-2,-1,-1):
                if nums[i] < max(nums[i+1:]):
                    left = i
                    break
            rela_max = max(nums[left+1:])
            for i in range(left+1, len(nums)):
                if nums[i] > nums[left] and nums[i] <= rela_max:
                    right = i
                    rela_max = nums[i]
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            tmp = nums[left+1:]
            tmp.sort()
            for i in range(len(tmp)):
                nums[left + 1 + i] = tmp[i]
