class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k = len(s1)

        i,j = 0,0
        freq = {}

        for ch in s1:
            freq[ch] = freq.get(ch,0) + 1
        
        count = len(freq)

        while j < n:
            if s2[j] in freq:
                freq[s2[j]] -= 1
                if freq[s2[j]] == 0:
                    count -= 1
            
            if (j-i+1) < k:
                j += 1
            
            elif (j-i+1) == k:
                if count == 0:
                    return True
                if s2[i] in freq:
                    freq[s2[i]] += 1
                    if freq[s2[i]] == 1:
                        count += 1
                i += 1
                j += 1
        return False

