class Solution:
    def shipWithinDays(self, weights: List[int], days: int):
        left = max(weights)
        right = sum(weights)

        ans = right

        while left <= right:
            mid = (left + right)//2

            daysNeeded = 1
            currentWeight = 0

            for weight in weights:
                if weight + currentWeight > mid:
                    daysNeeded += 1
                    currentWeight = weight
                
                else:
                    currentWeight += weight
                
            if daysNeeded <= days:
                ans = mid
                right = mid - 1
            
            else:
                left = mid + 1
        
        return ans