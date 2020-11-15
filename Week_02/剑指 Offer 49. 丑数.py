# 1.暴力
# 2. heap
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = []
        ls = [1]
        heapq.heapify(ls)
        for _ in range(n):
            cur = heapq.heappop(ls)
            res.append(cur)
            cur1, cur2, cur3 = cur*2, cur*3, cur*5
            setls = set(ls)
            setTmp = {cur1,cur2,cur3}
            diff = setTmp.difference(setls)
            if diff:
                for item in diff:
                    heapq.heappush(ls,item)
        return res[-1]
#3. DP 还不会