# -----------------------------------------------------------------------------
# Problem : Running Sum of 1d Array
# Source  : LeetCode 1480
# Time    : O(n)
# Space   : O(1) auxiliary (excluding the returned array)
# -----------------------------------------------------------------------------

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        sum = 0
        for num in nums:
            sum += num
            result.append(sum)
        return result 

        