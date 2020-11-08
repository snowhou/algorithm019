# 1. 暴力： 不断replace匹配的括号
# a. ()[]{}
# b. ((([{}])))
# O(n^2)

# 2. Stack

class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dict: stack.append(c)
            elif dict[stack.pop()] != c: return False
            print(stack)
        return len(stack) == 1
        
class Solution2:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('[]','').replace('()','').replace('{}','')
        print(s)
        return True if s == '' else False


if __name__ == '__main__':
    import datetime
    start_time = datetime.datetime.now()
    nums = ['', ']', '{}', '((({[]})))', '((([[]})))']
    solu = Solution2()
    for i in range(len(nums)):
        out = solu.isValid(nums[i])
        # print("time cost:{}".format(datetime.datetime.now()-start_time))
        print("原始: {}".format(nums[i]))
        print("结果: {}".format(out))
