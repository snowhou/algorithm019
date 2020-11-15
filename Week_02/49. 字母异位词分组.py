# 当且仅当它们的排序字符串相等时，两个字符串是字母异位词。
from typing import List
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            ans[tuple(sorted(s))] = ans.get(tuple(sorted(s)), []) +[s]
        return ans.values()


# 当且仅当它们的字符计数（每个字符的出现次数）相同时，两个字符串是字母异位词。
class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] *26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

class Solution4:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)] = ans.get(tuple(count), []) + [s]
        return ans.values()