# -----------------------------------------------------------------------------
# Problem : Move Zeroes
# Source  : LeetCode 283
# Time    : O(n)
# Space   : O(1) auxiliary
# -----------------------------------------------------------------------------

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            if nums[right]!=0:
               nums[left], nums[right] = nums[right], nums[left]
               left+=1
                  
        