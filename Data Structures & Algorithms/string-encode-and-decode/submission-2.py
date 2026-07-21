class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            cnt = len(i)
            encoded = encoded + "#*#" + str(cnt) + "#*#" + i
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i<len(s):
            if s[i:i+3] == "#*#":
                i += 3
                j = 1
                while s[i: i+j+1].isdigit():
                    j += 1
                length = int(s[i:i+j])
                i += j
                if s[i:i+3] == "#*#":
                    i += 3
                    word = s[i:i+length]
                    decoded.append(word)
                    i += length
            else: 
                break 
        return decoded

