import bisect

class Solution:
    def notInList(self, nums, target, ret):
        if ret > len(nums) or nums[ret-1] != target:
            return True
        return False
    
    def get_pivot(self, nums):
        # if rotated
        left = 0
        right = len(nums) - 1
        # find the pivot
        pivot = -1
        while (left < right):
            mid = (left + right) // 2
            if nums[mid] > nums[0]:
                left = mid + 1
            elif nums[mid] < nums[0]:
                if nums[mid - 1] > nums[mid]:
                    pivot = mid
                    break
                else:
                    right = mid - 1
            else:
                pivot = 1
                break

        if pivot == -1:
            pivot = left
        return pivot


    def search(self, nums: List[int], target: int) -> int:
        # if sorted
        if nums[0] <= nums[-1]:
            ret = bisect.bisect_right(nums, target)
            if self.notInList(nums, target, ret):
                return -1
            return ret-1
        # if rotated
        pivot = self.get_pivot(nums)
        
        if target < nums[0]:
            if self.search(nums[pivot:], target) == -1:
                return -1
            return pivot + self.search(nums[pivot:], target)
        else:
            return self.search(nums[:pivot], target)
            
