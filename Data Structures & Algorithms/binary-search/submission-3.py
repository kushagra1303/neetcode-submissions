from typing import List

class Solution:
    @staticmethod
    def binarySearch(nums, low, high, target):
        if low > high:
            return -1
        
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return Solution.binarySearch(nums, mid + 1, high, target)
        else:
            return Solution.binarySearch(nums, low, mid - 1, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)
