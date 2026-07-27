class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        i, j = 0, len(heights)-1
        while i<j:
            w = (j-i) * min(heights[i], heights[j])
            if w > m:
                m = w
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return m

        