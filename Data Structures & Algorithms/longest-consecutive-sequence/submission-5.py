class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        mn = min(s, default = 0)
        mx = max(s, default = 0)
        seql = 0
        op = 0
        for i in s:
            print("i: ", i)
            if i-1 in s:
                continue
                print("prev in set: ", i-1)
            else:
                seql += 1
            while i+1 in s:
                print("next in set: ", i+1)
                seql += 1
                i += 1
            if op < seql:
                op = seql
            seql = 0
        return op