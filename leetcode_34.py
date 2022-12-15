class Solution:
    def lowerBound(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right and left >= 0 and right < len(nums):
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == 0:
                    return 0
                elif nums[mid - 1] < target:
                    return mid
                else:
                    right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if left > right:
            return -1
        if left < 0:
            return -1
        if right >= len(nums):
            return -1
        if nums[left] == target:
            if left == 0:
                return 0
            elif nums[left - 1] < target:
                return left
        return -1


    def upperBound(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right and left >= 0 and right < len(nums):
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1:
                    return len(nums) - 1
                elif nums[mid + 1] > target:
                    return mid
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if left > right:
            return -1
        if left < 0:
            return -1
        if right >= len(nums):
            return -1
        if nums[left] == target:
            if left == len(nums) - 1:
                return len(nums) - 1
            elif nums[left + 1] > target:
                return left
            else:
                left = left + 1
        return -1


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.lowerBound(nums, target), self.upperBound(nums, target)]
