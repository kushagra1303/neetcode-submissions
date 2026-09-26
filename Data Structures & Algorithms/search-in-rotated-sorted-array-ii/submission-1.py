class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low,high = 0,len(nums)-1

        while low <= high:
            mid = (low + high)//2

            if nums[mid] == target:
                return True
            
            if nums[low] < nums[mid]:
                if nums[low] <= target and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            elif nums[low] > nums[mid]:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                low += 1
        
        return False
        