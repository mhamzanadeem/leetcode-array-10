# -----------------------------------------------------------------------------
# Problem : Shuffle the Array
# Source  : LeetCode 1470
# Time    : O(n)
# Space   : O(n) auxiliary
# -----------------------------------------------------------------------------

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        result = []
        for i in range(n):
            result.append(x[i])
            result.append(y[i])
        
        return result