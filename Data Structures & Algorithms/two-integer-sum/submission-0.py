class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {} #vale:index
        for index, val in enumerate(nums):
            dif =  target - val
            if dif in visited:
                return sorted([index, visited[dif]])
            else:
                visited[val] = index