class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        index = 0
        for key in freq:
            nums[index] = key
            index += 1
            
        
        return index