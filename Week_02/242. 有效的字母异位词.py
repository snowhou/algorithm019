# 1. 暴力, sort, sorted_str 相等？O(NlogN)
# 2. hash, map --> 统计每个字符的频次


# s = 'whcisd'
# sorted(s) -> ['c', 'd', 'h', 'i', 's', 'w']
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # 先判断长度是否相等
            return False
        return sorted(s) == sorted(t)


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = {}
        if len(s) != len(t): return False

        for char in s:
            if char not in tracker:
                tracker[char] = 1
            else: 
                tracker[char] += 1

        for char in s:
                tracker[char] = tracker.get(char, 1) + 1
            
        for char in t:
            if char in tracker:
                tracker[char] -= 1
            else: 
                return False
        
        for val in tracker.values():
            if val != 0:
                return False

        return True


import collections
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = collections.defaultdict(int)
        for x in s: tracker[x] += 1
        for x in t: tracker[x] -= 1
        return all(x == 0 for x in tracker.values())