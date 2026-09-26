class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        k_freq = sorted(count.keys(), key = lambda x: count[x], reverse = True)[:k]

        return k_freq
        