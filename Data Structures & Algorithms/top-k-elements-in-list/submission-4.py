from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1])

        top_k = sorted_freq[-k:]

        return [num for num, count in top_k]
