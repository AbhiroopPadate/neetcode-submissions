class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        cnts = Counter(s)
        cnts2 = Counter(t)
        return cnts == cnts2