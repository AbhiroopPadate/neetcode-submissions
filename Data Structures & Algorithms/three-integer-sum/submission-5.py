class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        op = []
        for i, val in enumerate(s):
            j = i+1
            k = len(s) - 1
            while j<k:
                if val + s[j] + s[k] == 0:
                    if [val, s[j], s[k]] not in op:
                        op.append([val, s[j], s[k]])
                    j += 1
                elif val + s[j] + s[k] < 0:
                    j += 1
                else:
                    k -= 1
        return op
                    
                    


        