class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        for pos,speed in sorted(zip(position,speed),reverse = True):
            eta = (target-pos)/speed
            if not st or eta>st[-1]:
                st.append(eta)
        return len(st)
        