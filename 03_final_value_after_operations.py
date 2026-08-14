# -----------------------------------------------------------------------------
# Problem : Final Value of Variable After Performing Operations
# Source  : LeetCode 2011
# Time    : O(n)
# Space   : O(1) auxiliary
# -----------------------------------------------------------------------------

from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0 
        for i in range(len(operations)):
            if operations[i] == '--X':
                x = x - 1
            if operations[i] == 'X--':
                x = x - 1
            if operations[i] == 'X++':
                x = x + 1
            if operations[i] == '++X':
                x = x + 1
        
        return x