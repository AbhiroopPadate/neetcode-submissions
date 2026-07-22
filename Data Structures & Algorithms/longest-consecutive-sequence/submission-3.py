class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        mn = min(s, default = 0)
        mx = max(s, default = 0)
        seql = 0
        op = 0
        for i in range(mn, mx+1):
            if i in s:
                seql+=1
                if op<seql:
                    op = seql
            elif i not in s:
                seql=0
        return op