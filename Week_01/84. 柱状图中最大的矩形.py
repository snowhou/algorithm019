# 暴力1 固定宽
#   for i -> 0, n-2
#       for j -> i+1, n-1
#           (i, j) -> 最小高度， area
#           update max_area

# 暴力2 固定高
#   for i -> 0, n-1
#       找到 left bound, right bound, 
#       area = height[i] * (right - left)
#       update max_area

# Monotonic Stack  单调栈

# 1
import sys
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            min_height = sys.maxsize
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height * (j - i + 1))
        return max_area


class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            left = i
            cur_height = heights[i]
            while left > 0 and heights[left - 1] >= cur_height:
                left -= 1
            
            right = i
            while right < n -1 and heights[right + 1] >= cur_height:
                right += 1

            max_width = right - left + 1
            max_area = max(max_area, max_width * cur_height)
        return max_area


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        area = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return area
        


if __name__ == '__main__':
    example = [[2,1,5,6,2,3], [1], [], [5, 5, 5, 5, 2, 4, 4]]
    solu = Solution2()
    for i, height in enumerate(example):
        print(height)
        out = solu.largestRectangleArea(height)
        print('结果: {}'.format(out))