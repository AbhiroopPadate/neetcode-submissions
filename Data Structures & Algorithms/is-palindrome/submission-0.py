class Solution:
    def isPalindrome(self, s: str) -> bool:
        inp = "".join([char for char in s if char.isalnum()]).lower()
        lft = 0
        rght = len(inp)-1
        while lft<rght:
            if inp[lft]  == inp[rght]:
                lft +=1 
                rght -=1
            else:
                return False
        return True
        