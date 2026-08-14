# -----------------------------------------------------------------------------
# Problem : Concatenation of Array
# Source  : LeetCode 1929
# Time    : O(n)
# Space   : O(1) auxiliary (excluding the returned array)
# -----------------------------------------------------------------------------

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
