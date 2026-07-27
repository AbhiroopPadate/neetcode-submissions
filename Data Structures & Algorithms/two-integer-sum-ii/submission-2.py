class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, val in enumerate(numbers):
            for j in range(i+1, len(numbers)):
                val2 = numbers[j]
                if val + val2 == target:
                    return [i+1, j+1]
                else:
                    continue