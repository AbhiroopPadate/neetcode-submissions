class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        for i in s:
            if i in ("(", "[", "{"):
                if i == "(":
                    stck.append(")")
                elif i == "[":
                    stck.append("]")
                else:
                    stck.append("}")
            elif i in (")", "]", "}"):
                if not stck:
                    return False
                if stck.pop(-1) == i:
                    continue
                else:
                    return False
            else:
                continue
        if not stck:
            return True
        else:
            return False
        