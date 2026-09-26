class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        n = len(nums)
        res = []

        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        for key,count in freq.items():
            if count > n//3:
                res.append(key)
        
        return res