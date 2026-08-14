# Array Simulation — 10 Solved Problems

A collection of **10 classical Array Simulation problems** solved in Python. Each solution is self-contained (imports its own types), uses a `Solution` class, and follows a uniform header template so the code is easy to read, grade, and reuse.

## Problem List & Complexity Table

**Conventions**

- `n` is the size of the input array.
- **Space** in `Solution` methods is *auxiliary space*, i.e. extra space **excluding the returned result array** (the standard LeetCode convention).
- Time/Space headers in each `.py` file match the entries below exactly.

| # | File | Problem | Platform | Technique | Time | Space |
|---|------|---------|----------|-----------|------|-------|
| 1 | `01_running_sum.py` | [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) | LeetCode 1480 | Prefix sum (single pass) | O(n) | O(1) |
| 2 | `02_highest_altitude.py` | [Find the Highest Altitude](https://leetcode.com/problems/find-the-highest-altitude/) | LeetCode 1732 | Running maximum | O(n) | O(1) |
| 3 | `03_final_value_after_operations.py` | [Final Value of Variable After Performing Operations](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/) | LeetCode 2011 | Simulation | O(n) | O(1) |
| 4 | `04_squares_sorted_array.py` | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | LeetCode 977 | Two pointers | O(n) | O(1) |
| 5 | `05_number_of_good_pairs.py` | [Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/) | LeetCode 1512 | Nested loop (pair counting) | O(n^2) | O(1) |
| 6 | `06_shuffle_array.py` | [Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/) | LeetCode 1470 | Interleaving | O(n) | O(n) |
| 7 | `07_move_zeroes.py` | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | LeetCode 283 | Two pointers (in-place swap) | O(n) | O(1) |
| 8 | `08_max_consecutive_ones.py` | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | LeetCode 485 | Single pass | O(n) | O(1) |
| 9 | `09_left_rotate_array.py` | Left Rotate an Array by One Place | Coding Ninjas / GeeksforGeeks | In-place shift | O(n) | O(1) |
| 10 | `10_concatenation.py` | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | LeetCode 1929 | Concatenation | O(n) | O(1) |

## Standard Header Template

Every `.py` file starts with this standardized comment block. Use the blank template (below) when adding new solutions, or copy the filled examples inside each file.

**Blank template:**

```python
# -----------------------------------------------------------------------------
# Problem : <PROBLEM NAME>
# Source  : <PLATFORM> <PROBLEM ID>
# Time    : O(...)
# Space   : O(...) auxiliary
# -----------------------------------------------------------------------------
```

**Filled example:**

```python
# -----------------------------------------------------------------------------
# Problem : Move Zeroes
# Source  : LeetCode 283
# Time    : O(n)
# Space   : O(1) auxiliary
# -----------------------------------------------------------------------------

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
```

## Notes

- **Problem 4** (`Squares of a Sorted Array`) uses the **two-pointer** technique to achieve **O(n)** time — both pointers start at opposite ends and the larger square is placed at the back of the result.
- **Problem 9** (`Left Rotate an Array by One Place`) shifts every element one position to the left in place, saving the first element and placing it at the end (O(1) extra space).
- **Problem 7** (`Move Zeroes`) achieves **O(n)** time and **O(1)** space using a single in-place swap pass; no extra array is created.
- Each file imports `List` from `typing`, so it runs standalone with any Python 3 interpreter (no LeetCode editor needed).