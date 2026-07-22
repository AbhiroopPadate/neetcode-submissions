class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        nxt = 1
        op = [] 
        for i in range(len(nums)):
            op.append(prev)
            prev = prev * nums[i]
        for j in range(len(nums)-1, -1, -1):
            op[j] = op[j] * nxt
            nxt = nxt * nums[j]
        return op