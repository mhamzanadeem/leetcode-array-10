# -----------------------------------------------------------------------------
# Problem : Find the Highest Altitude
# Source  : LeetCode 1732
# Time    : O(n)
# Space   : O(1) auxiliary
# -----------------------------------------------------------------------------

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0

        for g in gain:
            altitude += g
            highest = max(highest , altitude)

        return highest