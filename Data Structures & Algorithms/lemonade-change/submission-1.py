
from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        five = 0
        ten = 0

        for i in range(n):
            if bills[i] == 5:
                five += 1

            elif bills[i] == 10:
                if five == 0:
                    return False

                five -= 1
                ten += 1

            elif bills[i] == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1

                elif five >= 3:
                    five -= 3

                else:
                    return False

        return True