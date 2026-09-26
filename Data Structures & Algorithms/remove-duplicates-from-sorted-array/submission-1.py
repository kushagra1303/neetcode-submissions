class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        writePos = 0

        for readPos in range(1,len(nums)):
            if nums[writePos] != nums[readPos]:
                writePos += 1
                nums[writePos] = nums[readPos]
        

        return writePos + 1