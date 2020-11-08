class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        lens = len(nums)
        for i in range(lens - 2):
            if nums[i] > 0: break # 1. because of r > l > i
            if i > 0 and nums[i] == nums[i - 1]: continue # 2. skip the same nums[i]
            l, r = i + 1, lens - 1
            while l < r: # double pointer
                tar = nums[i] + nums[l] + nums[r]
                if tar > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                elif tar < 0:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
        return res