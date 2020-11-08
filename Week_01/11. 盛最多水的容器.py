# 两次遍历 O(n^2)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                if area > max_area:
                    max_area = area
        return max_area
# 左右指针
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] < height[r]:
                area = (r - l) * height[l]
                l += 1
            else:
                area = (r - l) * height[r]
                r -= 1
            max_area = max(area, max_area)
        return max_area

# fancy 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            max_area, l, r = max(h * (r - l), max_area), l + (h == height[l]), r - (h  == height[r])
        return max_area