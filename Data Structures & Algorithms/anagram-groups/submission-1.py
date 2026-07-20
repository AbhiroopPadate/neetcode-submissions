class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        {[a:1, c:1, t:1] -> [act, cat], ....}
        '''
        hsh = {} #counts : words
        for i in strs:
            s = "".join(sorted(i))
            if s not in hsh:
                hsh[s] = [i]
            else:
                hsh[s].append(i)
        return list(hsh.values())

        