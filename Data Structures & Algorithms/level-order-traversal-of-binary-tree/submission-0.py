# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        #Empty Tree
        if not root:
            return []
        
        queue = deque()
        queue.append(root)

        temp = []
        tempop = []
        op = []

        while True:
            
            #Check if queue has any node, pop it into temp
            while queue:
                temp.append(queue.popleft())
            
            #store the val of each poped node in list
            for j in temp:
                tempop.append(j.val)
            
            op.append(tempop)
            tempop = []
            
            for i in temp:
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
            temp = []
            if not queue:
                break

        return op
            
            

        
        