class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, val in enumerate(numbers):
            for j, val2 in enumerate(numbers):
                if val + val2 == target:
                    return [i+1, j+1]
                else:
                    continue