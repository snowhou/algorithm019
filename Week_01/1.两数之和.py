# two-sum
from typing import List
# 1. 穷举  time：O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
# 2. hash-table
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in ans:
                return [ans[m], i]
            else:
                ans[n] = i