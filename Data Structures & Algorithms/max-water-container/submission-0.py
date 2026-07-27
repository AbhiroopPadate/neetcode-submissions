class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        for i in range(len(heights)):
            v = heights[i]
            for j in range(i+1, len(heights)):
                if (j-i) * min(v, heights[j]) > m:
                    m = (j-i) * min(v, heights[j])
                    print(m)
        return m

        