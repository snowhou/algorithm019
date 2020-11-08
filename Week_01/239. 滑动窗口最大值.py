# 暴力 O((n-k+1)*k)

# 单调队列 Monotonic Queue O(n+k)
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        step = []
        for i in range(len(nums) - k + 1):
            max_num = nums[i]
            for j in range(i, i + k):
                max_num = max(max_num, nums[j]) 
            step.append(max_num)
        return step

# 单调队列 Monotonic Queue O(n+k)
