class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        cnts = {}
        for i in nums:
            if i in cnts:
                cnts[i] = cnts[i]+1
            else:
                cnts[i] = 1
        '''        
        if k>=1 and len(set(nums)) == 1:
            return [nums[0]]
        from collections import Counter
        cnts = Counter(nums)  #Value : count
        buck = [[] for _ in range(len(nums)+1)]  ## nums = [7, 7]  -> [[],[],[]]
        for i in cnts:
            buck[cnts[i]].append(i)
        op = []
        for j in reversed(buck):
            if j == []:
                pass
            else:
                while j != []:
                    if k > 0:
                        op.append(j.pop())
                        k-=1
                    else:
                        break
        return op
                
