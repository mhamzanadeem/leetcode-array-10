# -----------------------------------------------------------------------------
# Problem : Left Rotate an Array by One Place
# Source  : Coding Ninjas / GeeksforGeeks
# Time    : O(n)
# Space   : O(1) auxiliary
# -----------------------------------------------------------------------------

from typing import List

class Solution:
    def leftRotate(self, arr: List[int]) -> List[int]:
        """Left rotate the array by one place (in-place) and return it.

        Example: [1, 2, 3, 4, 5] -> [2, 3, 4, 5, 1]
        """
        n = len(arr)
        if n <= 1:
            return arr

        temp = arr[0]
        for i in range(1, n):
            arr[i - 1] = arr[i]
        arr[n - 1] = temp

        return arr